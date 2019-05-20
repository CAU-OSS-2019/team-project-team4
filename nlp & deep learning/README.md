# NLP & Deep Learning

This code mainly represents the **deep learning model** which classifies whether a specific **Twitch** chat log is a **mission** or not.

It is slightly simplified implementation of Prof. >Yoon Kim's Convolutional Neural Networks for Sentence Classification< paper in Tensorflow.

Paper link : http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf

Github link : https://github.com/yoonkim/CNN_sentence

## Requirements
* Python 3.7 or above
* Tensorflow 0.12 or above
* Numpy
* KoNLPy - Okt
* Word2Vec

## NLP
The **natural language processing(NLP)** is done by using **KoNLPy**(pronounced “ko en el PIE”) which is a python package for Korean language.

Input data(pubg chat logs in txt format) is processed to tokens through the **Okt module** in KoNLPy and saved as a list variable.

Then the list variable is used as a training data of the newly created **Word2Vec model** and the training occurs.

After the word tokens of the training data are vectorized and trained in the Word2Vec model then the model is saved as a file.

## Deep Learning(CNN Model)
Customizing the existing and performance-proven CNN model created by Prof. Yoon Kim, the model uses pre-trained Word2Vec model for its training.

The training chat logs(sentences) are mined from various **Twitch streamer channels** that focuses on the game **PlayerUnknown's Battlegrounds**(aka. Pubg).

Ex) 우주하마, 윤루트, 실프 and so on

### Training & Accuracy

**Total of 1000 chat logs** are used which 500 of them are valid mission chats and the other 500 are not.

800 chats logs are used in training and the other 200 are used in testing.

Accuracy converges to nearly **100%** but the model is not yet applied to real circumstances.

'''
./cnn_model
'''

### Evaluating

You can input your own sentence and find out the result.

'''
./load_model_and_predict
'''
