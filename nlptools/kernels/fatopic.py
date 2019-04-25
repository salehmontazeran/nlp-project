from nlptools.kernels.Toolstopicfa import Read_data, evaluate, vectorizer

folder = 'models/data'
Data = Read_data(folder)

X, Y = vectorizer(Data)

# split the data so we will have 2 documents as test data for each category
# X_train, X_test, y_train, y_test = Split_data(X, Y)


def name(dec):
    if dec == 1:
        return "اجتماعی"
    if dec == 2:
        return "ادیان"
    if dec == 3:
        return "اقتصادی"
    if dec == 4:
        return "سیاسی"
    if dec == 5:
        return "فناوری"
    if dec == 6:
        return "مسایل راهبردی ایران"
    if dec == 7:
        return "ورزشی"
    return dec


def predict(sample):
    return name(evaluate(X, Y, sample)[0])
