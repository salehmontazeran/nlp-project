from nltk.corpus import wordnet as wn


class Wordnet():

    def s(self, word):
        syn = []
        ant = []
        for s in wn.synsets(word):
            for l in s.lemmas():
                syn.append(l.name())
                if l.antonyms():
                    ant.append(l.antonyms()[0].name())
        # res = wn.synsets(word)
        return syn, ant
