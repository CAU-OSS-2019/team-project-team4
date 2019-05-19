import os
import time
import datetime
from tensorflow import flags
import tensorflow as tf
import numpy as np
from konlpy.tag import Okt
import csv
import gensim
import sys

class TextCNN(object):
    """
    A CNN for text classification.
    Uses an embedding layer, followed by a convolutional, max-pooling and softmax layer.
    <Parameters>
        - sequence_length: 최대 문장 길이 - 문장에 단어 최대 몇 개?
        - num_classes:     클래스 개수    - 미션 / 노미션
        - vocab_size:      등장 단어 수   - 총 학습시키려는
        - embedding_size:  각 단어에 해당되는 임베디드 벡터의 차원 - 100
        - filter_sizes:    convolutional filter들의 사이즈 (= 각 filter가 몇 개의 단어를 볼 것인가?) (예: "3, 4, 5")
        - num_filters:     각 filter size 별 filter 수
        - l2_reg_lambda:   각 weights, biases에 대한 l2 regularization 정도
    """

    def __init__(self, sequence_length = 6, num_classes = 2,
        embedding_size = 100, filter_sizes = [3,4,5], num_filters = 128, l2_reg_lambda = 0.0):

        # Placeholders for input, output and dropout
        self.input_x: object = tf.placeholder(tf.float32, [None, sequence_length, embedding_size, 1], name="input_x")
        #                                                             = 6             = 100
        self.input_y = tf.placeholder(tf.int32, [None, num_classes], name="input_y")
        #                                                  = 2
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # Keeping track of l2 regularization loss (optional)
        l2_loss = tf.constant(0.0)

        # Create a convolution + maxpool layer for each filter size
        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            #                           = [ 3, 4, 5 ] 단어씩 보기로
            with tf.name_scope("conv-maxpool-%s" % filter_size):
                # Convolution Layer
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                #               = [ 3, 4, 5 ] 중 하나   = 100       = 128
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
                b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name="b")
                conv = tf.nn.conv2d(
                    self.input_x,
                    W,
                    strides=[1, 1, 1, 1],
                    padding="VALID",
                    name="conv")
                # Apply nonlinearity
                h = tf.nn.relu(tf.nn.bias_add(conv, b), name="relu")
                # Maxpooling over the outputs
                pooled = tf.nn.max_pool(
                    h,
                    ksize=[1, sequence_length - filter_size + 1, 1, 1],
                    strides=[1, 1, 1, 1],
                    padding='VALID',
                    name="pool")
                pooled_outputs.append(pooled)
        # Combine all the pooled features
        num_filters_total = num_filters * len(filter_sizes)
        self.h_pool = tf.concat(pooled_outputs, 3)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1, num_filters_total])

        # Add dropout
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)

        # Final (unnormalized) scores and predictions
        with tf.name_scope("output"):
            W = tf.get_variable(
                "W",
                shape=[num_filters_total, num_classes],
                initializer=tf.contrib.layers.xavier_initializer())
            b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name="b")
            l2_loss += tf.nn.l2_loss(W)
            l2_loss += tf.nn.l2_loss(b)
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            self.predictions = tf.argmax(self.scores, 1, name="predictions")

        # Calculate Mean cross-entropy loss
        with tf.name_scope("loss"):
            losses = tf.nn.softmax_cross_entropy_with_logits_v2(self.input_y, self.scores)
            self.loss = tf.reduce_mean(losses) + l2_reg_lambda * l2_loss

        # Accuracy
        with tf.name_scope("accuracy"):
            correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y, 1)) # tf.argmax(self.input_y, 1)
            self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")


# data loading
w2v_model = gensim.models.Word2Vec.load('w2v_model')
okt = Okt()
cnn_x_train = []
cnn_y_train = []
cnn_x_test = []
cnn_y_test = []
train_data_file = 'cnn_train_data.csv'
test_data_file = 'cnn_test_data.csv'

f = open(train_data_file, 'r', encoding='utf-8-sig')    # load train data
rdr = csv.reader(f)
for line in rdr:
    x_data = line[0]
    y_data = line[1]
    if '> ' in x_data:
        tokens = okt.pos( x_data[x_data.find('> ') + 2:] )
    else:
        tokens = okt.pos(x_data)
    count = 0
    lineList = []
    for keyword, type in tokens:
        if type == 'Noun' or type == 'Verb' or type == 'Adjective' or type == 'Adverb':
            try: lineList.append(w2v_model.wv.get_vector(keyword))
            except: lineList.append([0] * 100)
    while len(lineList) < 6:
        lineList.append([0] * 100)
    while len(lineList) > 6:
        lineList.pop()
    if lineList:
        cnn_x_train.append(lineList[:])
        if y_data == '1':
            cnn_y_train.append([1, 0])
        else:
            cnn_y_train.append([0, 1])
    lineList.clear()
f.close()

f = open(test_data_file, 'r', encoding='utf-8-sig')     # load test data
rdr = csv.reader(f)
for line in rdr:
    x_data = line[0]
    y_data = line[1]
    tokens = okt.pos( x_data[x_data.find('> ') + 2:] )
    count = 0
    lineList = []
    for keyword, type in tokens:
        if type == 'Noun' or type == 'Verb' or type == 'Adjective' or type == 'Adverb':
            try: lineList.append(w2v_model.wv.get_vector(keyword))
            except: lineList.append([0] * 100)
    while len(lineList) < 6:
        lineList.append([0] * 100)
    while len(lineList) > 6:
        lineList.pop()
    if lineList:
        cnn_x_test.append(lineList[:])
        if y_data == 1:
            cnn_y_test.append([1, 0])
        else:
            cnn_y_test.append([0, 1])
    lineList.clear()
f.close()

cnn_x_train = np.expand_dims(cnn_x_train, axis=3)
# cnn_y_train = np.expand_dims(cnn_y_train, axis=1)
cnn_x_test = np.expand_dims(cnn_x_test, axis=3)
# cnn_y_test = np.expand_dims(cnn_y_test, axis=1)
print("finished loading data")
print(np.shape(cnn_x_train))
print(np.shape(cnn_y_train))
print(np.shape(cnn_x_test))
print(np.shape(cnn_y_test))

'''
# Model Hyperparameters
flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of embedded vector (default: 128)")
flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-separated filter sizes (default: '3,4,5')")
flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
flags.DEFINE_float("l2_reg_lambda", 0.1, "L2 regularization lambda (default: 0.0)")
'''

# Training parameters
flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
flags.DEFINE_integer("num_epochs", 100, "Number of training epochs (default: 200)")
flags.DEFINE_integer("evaluate_every", 100, "Evaluate model on dev set after this many steps (default: 100)")
flags.DEFINE_integer("checkpoint_every", 100, "Save model after this many steps (default: 100)")
flags.DEFINE_integer("num_checkpoints", 5, "Number of checkpoints to store (default: 5)")

# Misc Parameters
flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
# FLAGS._parse_flags()
FLAGS(sys.argv)
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")

# 3. train the model and test
with tf.Graph().as_default():
    init_op = tf.global_variables_initializer()
    sess = tf.Session()
    with sess.as_default():
        cnn = TextCNN(sequence_length = 6,
                      num_classes = 2,
                      embedding_size = 100,
                      filter_sizes= [3,4,5],
                      num_filters = 128,
                      l2_reg_lambda = 0.1)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)
        saver = tf.train.Saver();

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            if g is not None:
                grad_hist_summary = tf.summary.histogram("{}".format(v.name), g)
                sparsity_summary = tf.summary.scalar("{}".format(v.name), tf.nn.zero_fraction(g))
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
        grad_summaries_merged = tf.summary.merge(grad_summaries)

        # Output directory for models and summaries
        timestamp = str(int(time.time()))
        out_dir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp))
        print("Writing to {}\n".format(out_dir))

        # Summaries for loss and accuracy
        loss_summary = tf.summary.scalar("loss", cnn.loss)
        acc_summary = tf.summary.scalar("accuracy", cnn.accuracy)

        # Train Summaries
        train_summary_op = tf.summary.merge([loss_summary, acc_summary, grad_summaries_merged])
        train_summary_dir = os.path.join(out_dir, "summaries", "train")
        train_summary_writer = tf.summary.FileWriter(train_summary_dir, sess.graph)

        # Dev summaries
        dev_summary_op = tf.summary.merge([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
        dev_summary_writer = tf.summary.FileWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        saver = tf.train.Saver(tf.global_variables(), max_to_keep=FLAGS.num_checkpoints)

        # Initialize all variables
        sess.run(tf.global_variables_initializer())

        # train step function
        def train_step(x_batch, y_batch):
            """
            A single training step
            """
            feed_dict = {
                cnn.input_x: x_batch,
                cnn.input_y: y_batch,
                cnn.dropout_keep_prob: 0.5
            }
            _, step, summaries, loss, accuracy = sess.run(
                [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            train_summary_writer.add_summary(summaries, step)

        # test step function
        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            feed_dict = {
                cnn.input_x: x_batch,
                cnn.input_y: y_batch,
                cnn.dropout_keep_prob: 1.0
            }
            step, summaries, loss, accuracy = sess.run(
                [global_step, dev_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            if writer:
                writer.add_summary(summaries, step)

        # divide data into batch and shuffle
        def batch_iter(data, batch_size, num_epochs, shuffle=True):
            """
            Generates a batch iterator for a dataset.
            """
            data = np.array(data)
            data_size = len(data)
            num_batches_per_epoch = int((len(data) - 1) / batch_size) + 1
            for epoch in range(num_epochs):
                # Shuffle the data at each epoch
                if shuffle:
                    shuffle_indices = np.random.permutation(np.arange(data_size))
                    shuffled_data = data[shuffle_indices]
                else:
                    shuffled_data = data
                for batch_num in range(num_batches_per_epoch):
                    start_index = batch_num * batch_size
                    end_index = min((batch_num + 1) * batch_size, data_size)
                    yield shuffled_data[start_index:end_index]

        # Generate batches
        batches = batch_iter(
            list(zip(cnn_x_train, cnn_y_train)), FLAGS.batch_size, FLAGS.num_epochs)

        testpoint = 0
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)
            train_step(x_batch, y_batch)
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                if testpoint + 100 < len(cnn_x_test):
                    testpoint += 100
                else:
                    testpoint = 0
                print("\nEvaluation:")
                dev_step(cnn_x_test[testpoint:testpoint+100], cnn_y_test[testpoint:testpoint+100], writer=dev_summary_writer)
                print("")
            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))

        saver.save(sess, 'saved_model')

