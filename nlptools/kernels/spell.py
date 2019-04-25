from collections import defaultdict


class Spell():
    def __init__(self):
        base = r''
        self.engFile = base + r'corpus/eng-new.txt'
        self.faFile = base + r'corpus/eng-new.txt'
        self.faDicPath = base + r'db/dic-fa.txt'
        self.enDicPath = base + r'db/dic-en.txt'
        self.faTwowPath = base + r'db/en-twow.txt'
        self.enTwowPath = base + r'db/fa-twow.txt'
        self.enCor = base + r'db/fa-twow.txt'
        self.enCorOut = base + r'db/fa-twow.txt'
        self.faCor = base + r'db/fa-twow.txt'
        self.faCorOut = base + r'db/fa-twow.txt'
        self.parseDic()

    def parseDic(self):
        self.dictFa = defaultdict(lambda: False)
        self.dictEn = defaultdict(lambda: False)
        self.dictFaTwow = defaultdict(lambda: False)
        self.dictEnTwow = defaultdict(lambda: False)

        with open(self.faDicPath, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    self.dictFa[w] = True
                line = f.readline()

        with open(self.enDicPath, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    self.dictEn[w] = True
                line = f.readline()

        with open(self.faTwowPath, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    if w:
                        self.dictFaTwow[w] = True
                line = f.readline()

        with open(self.enTwowPath, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    if w:
                        self.dictEnTwow[w] = True
                line = f.readline()

    def existFa(self, word):
        return self.dictFa[word]

    def existEn(self, word):
        return self.dictEn[word]

    def existFaTwow(self, word):
        return self.dictFaTwow[word]

    def existEnTwow(self, word):
        return self.dictEnTwow[word]

    def findCorrectEn(self, word):

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                t = word[:i] + str(c) + word[i + 1:]
                if self.dictEn[t]:
                    return [word[i], c]
        return [0, 0]

    def findCorrectFa(self, word):

        for i in range(len(word)):
            for c in "ضصثقفغعهخحجچشسیبلاتنمکگپظطزرذدئوژ":
                t = word[:i] + str(c) + word[i + 1:]
                if self.dictFa[t]:
                    return [word[i], c]

        return [0, 0]

    def keyboardFa(self, inList):

        n = {}
        n['ض'] = 1
        n['ص'] = 2
        n['ث'] = 3
        n['ق'] = 4
        n['ف'] = 5
        n['غ'] = 6
        n['ع'] = 7
        n['ه'] = 8
        n['خ'] = 9
        n['ح'] = 10
        n['ج'] = 11
        n['چ'] = 12
        n['ش'] = 20
        n['س'] = 21
        n['ی'] = 22
        n['ب'] = 23
        n['ل'] = 24
        n['ا'] = 25
        n['ت'] = 26
        n['ن'] = 27
        n['م'] = 28
        n['ک'] = 29
        n['گ'] = 30
        n['پ'] = 31
        n['ظ'] = 40
        n['ط'] = 41
        n['ز'] = 42
        n['ژ'] = 43
        n['ر'] = 44
        n['ذ'] = 45
        n['د'] = 46
        n['ئ'] = 47
        n['و'] = 48

        return abs(n[inList[0]] - n[inList[1]]) == 1

    def keyboardEn(self, inList):

        n = {}
        n['q'] = 1
        n['w'] = 2
        n['e'] = 3
        n['r'] = 4
        n['t'] = 5
        n['y'] = 6
        n['u'] = 7
        n['i'] = 8
        n['o'] = 9
        n['p'] = 10
        n['a'] = 20
        n['s'] = 21
        n['d'] = 22
        n['f'] = 23
        n['g'] = 24
        n['h'] = 25
        n['j'] = 26
        n['k'] = 27
        n['l'] = 28
        n['z'] = 40
        n['x'] = 41
        n['c'] = 42
        n['v'] = 43
        n['b'] = 44
        n['n'] = 45
        n['m'] = 46
        return abs(n[inList[0]] - n[inList[1]]) == 1

    def hamAvaFa(self, inList):

        n = {}
        n['ض'] = 1
        n['ز'] = 1
        n['ذ'] = 1
        n['ظ'] = 1

        n['س'] = 2
        n['ص'] = 2
        n['ث'] = 2

        n['ت'] = 3
        n['ط'] = 3

        n['ق'] = 4
        n['غ'] = 4

        return abs(n[inList[0]] - n[inList[1]]) == 0

    def hamAvaEn(self, inList):

        n = {}
        n['g'] = 1
        n['j'] = 2

        n['s'] = 2
        n['c'] = 2

        n['v'] = 3
        n['w'] = 3

        return abs(n[inList[0]] - n[inList[1]]) == 0

    def sameEn(self, inList):

        n = {}
        n['i'] = 1
        n['l'] = 1

        n['v'] = 2
        n['u'] = 2

        return abs(n[inList[0]] - n[inList[1]]) == 0

    def checkSpellFa(self, word):

        if self.existFaTwow(word):
            return 5

        outList = self.findCorrectFa(word)

        if self.keyboardFa(outList):
            return 1

        if self.hamAvaFa(outList):
            return 3

        return 2

    def checkSpellEn(self, word):

        if self.existEnTwow(word):
            return 6

        outList = self.findCorrectEn(word)

        if self.keyboardEn(outList):
            return 1

        if self.hamAvaEn(outList):
            return 3

        if self.sameEn(outList):
            return 4

        return 2

    def findFa(self):

        q = defaultdict(lambda: 0)

        with open(self.faCor, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                words = line.split(' ')
                for w in words:
                    q[w] = self.checkSpellFa(w)
                line = f.readline()

        with open(self.faCorOut, 'w', encoding='utf8') as w:
            t = ""
            for key in q:
                t = str(key) + '\t\t' + str(q[key])

                w.write(t)
                w.write("\n")

    def findEn(self):

        q = defaultdict(lambda: 0)

        with open(self.enCor, 'r', encoding='utf8') as f:
            line = f.readline()
            while line:
                words = line.split(' ')
                for w in words:
                    q[w] = self.checkSpellEn(w)
                line = f.readline()

        with open(self.enCorOut, 'w', encoding='utf8') as w:
            t = ""
            for key in q:
                t = str(key) + '\t\t' + str(q[key])

                w.write(t)
                w.write("\n")
