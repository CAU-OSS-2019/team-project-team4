import tensorflow as tf
import numpy as np
from konlpy.tag import Okt
import gensim


# data loading
w2v_model = gensim.models.Word2Vec.load('w2v_model')
okt = Okt()
tokens = okt.pos("진짜 못하네. 치킨 먹으면 5억 줄게^^")
cnn_x_input = []
for keyword, type in tokens:
    if type == 'Noun' or type == 'Verb' or type == 'Adjective' or type == 'Adverb':
        try:
            cnn_x_input.append(w2v_model.wv.get_vector(keyword))
        except:
            cnn_x_input.append([0] * 100)
while len(cnn_x_input) < 6:
    cnn_x_input.append([0] * 100)
while len(cnn_x_input) > 6:
    cnn_x_input.pop()
cnn_x_input = np.array(cnn_x_input)   # 차원 증가
cnn_x_input = cnn_x_input[:, :, np.newaxis]
cnn_x_input = cnn_x_input[np.newaxis]


#First let's load meta graph and restore weights
sess = tf.Session()
saver = tf.train.import_meta_graph('saved_model.meta')
saver.restore(sess,tf.train.latest_checkpoint('./'))

graph = tf.get_default_graph()
input_x = graph.get_tensor_by_name("input_x:0")
input_y = graph.get_tensor_by_name("input_y:0")
predict = graph.get_tensor_by_name("output/predictions:0")
scores = graph.get_tensor_by_name("output/scores:0")
dropout_keep_prob = graph.get_tensor_by_name("dropout_keep_prob:0")

feed_dict = {input_x: cnn_x_input, input_y: [[1, 0]], dropout_keep_prob: 1.0}


# predict: 0 -> CORRECT, 1 -> INCORRECT
print(sess.run(scores, feed_dict= feed_dict))
print(sess.run(predict, feed_dict= feed_dict))