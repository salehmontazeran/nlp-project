from collections import defaultdict
from os import path
from threading import Thread


class Tokenization():
    def __init__(self, inFile="", outPath=""):
        self.inFile = inFile
        self.outPath = outPath

    def token(self):
        output = path.join(self.outPath, 'token.txt')
        with open(output, 'w', encoding='utf8') as o:
            with open(self.inFile, 'r', encoding='utf8') as i:
                line = i.readline()
                while line:
                    line = line.strip()
                    words = line.split(' ')
                    for w in words:
                        o.write(w)
                        o.write('\n')
                    line = i.readline()

    def tokenType(self):
        s = set()
        with open(self.inFile, 'r', encoding='utf8') as i:
            line = i.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    s.add(w)
                line = i.readline()

        output = path.join(self.outPath, 'tokenType.txt')
        with open(output, 'w', encoding='utf8') as o:
            for e in s:
                o.write(e)
                o.write('\n')

    def tokenNumber(self):
        h = defaultdict(lambda: 0)
        with open(self.inFile, 'r', encoding='utf8') as i:
            line = i.readline()
            while line:
                line = line.strip()
                words = line.split(' ')
                for w in words:
                    h[w] = h[w] + 1
                line = i.readline()

        output = path.join(self.outPath, 'tokenNumber.txt')
        with open(output, 'w', encoding='utf8') as o:
            for e in h:
                t = '{:20s} {:6d}'.format(e, h[e])
                o.write(t)
                o.write('\n')

    def run(self):
        threads = []
        threads.append(Thread(target=self.token, name='t1'))
        threads.append(Thread(target=self.tokenType, name='t2'))
        threads.append(Thread(target=self.tokenNumber, name='t3'))

        for t in threads:
            t.start()
        for t in threads:
            t.join()


# inp = r'D:\workspace\python\nlp-project\corpus\fa-new.txt'
# out = r'D:\workspace\python\nlp-project\corpus\output'
# c = Tokenization(inp, out)
# c.run()
