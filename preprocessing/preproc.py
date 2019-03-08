import string

ENG_INPUT = "corpus/eng.txt"
ENG_OUTPUT = "corpus/eng-new.txt"
FA_INPUT = "corpus/fa.txt"
FA_OUTPUT = "corpus/fa-new.txt"


def punctuationRemover(outputFile, inputFile):
    punc = string.punctuation.replace("'", "؟")
    with open(outputFile, 'w', encoding='utf8') as o:
        with open(inputFile, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.translate(str.maketrans('', '', punc))
                line = line.lstrip()
                o.write(line)
                line = f.readline()


punctuationRemover(ENG_OUTPUT, ENG_INPUT)
punctuationRemover(FA_OUTPUT, FA_INPUT)
