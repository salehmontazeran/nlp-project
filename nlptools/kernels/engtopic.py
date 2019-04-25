# from sklearn.datasets import fetch_20newsgroups
from sklearn.externals import joblib

# from nlptools.kernels.toolstopicen import text_mnb_stemmed

# twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
# twenty_test = fetch_20newsgroups(subset='test', shuffle=True)


# text_mnb_stemmed = text_mnb_stemmed.fit(
#     twenty_train.data, twenty_train.target
#     )
# joblib.dump(text_mnb_stemmed, 'models/saved_modelen.pkl')
text_mnb_stemmed = joblib.load('models/saved_modelen.pkl')


def name(dec):
    if dec in [1, 2, 3, 4, 5]:
        return "computer"
    if dec == 7:
        return "autos"
    if dec == 8:
        return "motorcycles"
    if dec in [9, 10]:
        return "sport"
    if dec in [11, 12, 13, 14]:
        return "science"
    if dec in [16, 17, 18]:
        return "politics"
    return dec


def predict(sample):
    global text_mnb_stemmed
    return name(text_mnb_stemmed.predict([sample, ])[0])


# print(predict(text))

# print(np.mean(predicted_mnb_stemmed == twenty_test.target))
