from hazm import (
    POSTagger, word_tokenize, Lemmatizer, Stemmer, Normalizer
    )


class POS():
    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile
        self.normalizer = Normalizer()
        self.tagger = POSTagger(model='resources/postagger.model')
        self.lemmatizer = Lemmatizer()
        self.stemmer = Stemmer()

    def posTaggerTXT(self):
        with open(self.outFile, 'w', encoding="utf8") as o:
            with open(self.inFile, 'r', encoding="utf8") as f:
                line = f.readline()
                while line:
                    line = line.strip()
                    line = self.normalizer.normalize(line)
                    tags = self.tagger.tag(word_tokenize(line))
                    for li in tags:
                        t = '{:20s} {:20s} {:20s} {:20s}\n'.format(
                            li[0],
                            self.nameTag(li[1]),
                            self.lemmatizer.lemmatize(li[0]),
                            self.stemmer.stem(li[0])
                            )
                        o.write(t)
                    line = f.readline()

    def posTaggerHTML(self):
        with open(self.outFile, 'w', encoding="utf8") as o:
            with open(self.inFile, 'r', encoding="utf8") as f:
                o.write(self.preHTML())
                line = f.readline()
                while line:
                    line = line.strip()
                    line = self.normalizer.normalize(line)
                    tags = self.tagger.tag(word_tokenize(line))
                    for li in tags:
                        t = '{:s} -//- {:s} -//- {:s} -//- {:s}\n'.format(
                            li[0],
                            self.nameTag(li[1]),
                            self.lemmatizer.lemmatize(li[0]),
                            self.stemmer.stem(li[0])
                            )
                        o.write(self.divHTML(
                            self.colorTag(li[1]),
                            t
                            ))
                        o.write("\n")
                    line = f.readline()
                o.write(self.posHTML())

    def nameTag(self, tag):
        if tag == "V":
            return "فعل"
        elif tag == "N":
            return "اسم"
        elif tag == "ADV":
            return "قید"
        elif tag == "PRO":
            return "ضمیر"
        elif tag == "PUNC":
            return "نشانه نگارشی"
        elif tag == "Ne":
            return "غیر قابل تشخیص"
        elif tag == "NUM":
            return "عدد"
        elif tag == "CONJ":
            return "حرف ربط"
        elif tag == "POSTP":
            return "نشانه مفعولی"
        elif tag == "P":
            return "حرف اضافه"
        elif tag == "AJ":
            return "صفت"
        elif tag == "DET":
            return "ضمیر اشاره"
        else:
            return tag

    def colorTag(self, tag):
        if tag == "V":
            return "red"
        elif tag == "N":
            return "hotpink"
        elif tag == "ADV":
            return "blue"
        elif tag == "PRO":
            return "gold"
        elif tag == "PUNC":
            return "lightblue"
        elif tag == "Ne":
            return "darkgray"
        elif tag == "NUM":
            return "white"
        elif tag == "CONJ":
            return "lightgreen"
        elif tag == "POSTP":
            return "white"
        elif tag == "P":
            return "aqua"
        elif tag == "AJ":
            return "teal"
        elif tag == "DET":
            return "slateblue"
        else:
            return "white"

    def preHTML(self):
        return """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
</head>
<body>
"""

    def posHTML(self):
        return """
    </body>
</html>"""

    def divHTML(self, color, text):
        return """
        <div style="background-color:""" + color + """">
        """ + """<h4>""" + text + """</h4>
        """ + """</div>
        """
