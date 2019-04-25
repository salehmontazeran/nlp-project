import string

ENG_INPUT = "corpus/eng.txt"
ENG_OUTPUT = "corpus/eng-new.txt"
FA_INPUT = "corpus/fa.txt"
FA_OUTPUT = "corpus/fa-new.txt"


def punctuationRemover(outputFile, inputFile):
    punc = string.punctuation.replace("'", "؟،;0123456789؛")
    with open(outputFile, 'w', encoding='utf8') as o:
        with open(inputFile, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.translate(str.maketrans('', '', punc))
                line = line.lstrip()
                o.write(line)
                line = f.readline()


def englishRemover(outputFile, inputFile):
    lines = []
    with open(inputFile, 'r', encoding='utf8') as f:
        line = f.readline()
        i = 0
        while line:
            ++i
            for w in line:
                if w in "AaBbCcDdEeFfGgHhIiJjKkLlMmN \
                        nOoPpQqRrSsTtUuVvWwXxYyZz0123456789":

                    lines.append(i)
                    break
    print("****************************")
    with open("temp.txt", 'w', encoding='utf8') as t:
        with open(outputFile, 'r', encoding='utf8') as o:
            line = o.readline()
            i = 0
            while line:
                ++i
                if i not in lines:
                    t.write(line)

    with open("temp.txt", 'r', encoding='utf8') as t:
        with open(outputFile, 'w', encoding='utf8') as o:
            o.write(t.readlines())


punctuationRemover(ENG_OUTPUT, ENG_INPUT)
punctuationRemover(FA_OUTPUT, FA_INPUT)
# englishRemover(ENG_OUTPUT, FA_OUTPUT)
