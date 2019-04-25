import math
import os
import re
from collections import Counter

import numpy as np
from sklearn.externals import joblib

# from sklearn.metrics import accuracy_score
# from sklearn.neural_network import MLPClassifier

Vocabulary = []
fn = 1000


# read all the data from the given directory
def Read_data(folder):
    Data = []
    labels_name = 0
    # go over each file directory and read all the text
    for filename in os.listdir(folder):
        # add a class to each file
        labels_name += 1
        path1 = os.path.join(folder, filename)
        for i in os.listdir(path1):
            path2text = os.path.join(path1, i)
            # read the text file and add it to Data
            with open(path2text, "r", encoding="utf8") as myfile:
                sample = myfile.read()
                Data.append([sample, labels_name])

    return Data


# tokenize the text
def TOK(text):
    # remove all the numbers
    text = re.sub("[0-9]", " ", text)
    # remove all english character
    text = re.sub("[a-zA-Z]", " ", text)
    # split the text to its words
    return text.split()


# extracting BOW features from the Data
def vectorizer(Data):
    global Vocabulary
    global fn

    stop = []
    with open('models/fastop.txt', 'r', encoding="utf8") as f:
        file = f.read()
        lines = file.split('\n')
        for line in lines:
            line = line.split()
            stop.append(line[0])

    # print(stop)

    Corpus = []
    dict = {}
    # add all the text to Coprus
    for i in Data:
        Corpus.append(i[0])
    # for each text we  tokenize it and create the vocabulary using all
    # the words
    for i in Corpus:
        text = TOK(i)
        for j in text:
            # check if the word is in the vocabulary
            if j not in stop:
                if j in dict:
                    dict[j] += 1
                else:
                    dict[j] = 1
    # count the number of accurance of each word and take the 1000
    # most frequent words
    Vocabulary = Counter(dict).most_common(fn)
    # print(len(Vocabulary))
    # seperqate the words
    Vocabulary = [x[0] for x in Vocabulary]

    data_vectors = []
    # define a feature vectors for each document
    vector = np.zeros(fn, dtype=float)

    # doing the same thing for test data
    for i in Data:
        text = TOK(i[0])
        for j in text:
            if j in Vocabulary:
                vector[Vocabulary.index(j)] += 1
        vector = np.asanyarray([math.log(x + 1) for x in vector])
        data_vectors.append([vector, i[1]])
        vector = np.zeros(fn, dtype=float)
    # seperate the features and theit labels
    X, Y = np.asanyarray([i[0] for i in data_vectors]), \
        np.asanyarray([i[1] for i in data_vectors])

    return X, Y


# spliting the data fairly so test and traing
# data have sample of all the classes
def Split_data(X, Y):
    X_test = []
    X_train = []
    y_train = []
    y_test = []

    # for each class we select the 2 sample to the test
    # and the rest to the train data
    for i in range(7):
        # find class with lable equal to (i+1)
        indecis = np.where(Y == i + 1)
        test_index = indecis[0][0:2]
        train_index = indecis[0][2:]
        # append the test data
        for te in test_index:
            X_test.append(X[te, :])
            y_test.append(Y[te])
        # append the train data
        for tr in train_index:
            X_train.append(X[tr, :])
            y_train.append(Y[tr])

    # print(y_train)

    return np.asanyarray(X_train), np.asanyarray(X_test), \
        np.asanyarray(y_train), np.asanyarray(y_test)


# evaluate using MLP and naive bayes
def evaluate(X, Y, sample):

    t = amadeh(sample)

    # print("\n\nRunning neural network...")
    # nn_clf = MLPClassifier(
    #     solver='adam', activation='tanh',
    #     early_stopping=True, learning_rate='adaptive',
    #     alpha=1e-5, hidden_layer_sizes=(500, 300)
    # )
    # traing MLP
    # nn_clf.fit(X, Y)
    # joblib.dump(nn_clf, 'saved_modelfa.pkl')

    nn_clf = joblib.load('models/saved_modelfa.pkl')
    return nn_clf.predict(np.array([t, ]))

    # predict the test data
    # y_pred = nn_clf.predict(X_test)

    # y = nn_clf.predict(np.array([t, ]))
    # print(y)

    # print(type(X_test))
    # print('accuracy on test data :',accuracy_score(y_test, y_pred))
    # print(y_test)
    # print(y_pred)

    # predict the train data
    # y_pred = nn_clf.predict(X_train)
    # print("accuracy on train data : ",accuracy_score(y_train, y_pred))


def amadeh(sample):
    global fn
    # with open('test.txt', "r", encoding="utf8") as f:
    vector = np.zeros(fn, dtype=float)
    # data = f.read()
    data = sample
    lines = data.split('\n')

    for line in lines:
        text = TOK(line)
        for j in text:
            if j in Vocabulary:
                vector[Vocabulary.index(j)] += 1

    vector = np.asanyarray([math.log(x + 1) for x in vector])
    # print(vector)
    return vector
