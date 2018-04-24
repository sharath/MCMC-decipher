import nltk, re


class TextCrawler():
    def __init__(self, filename):
        self.filename = filename
        self.dist = None
        raw = open(self.filename, 'r').read()
        self.text = ' '.join(re.findall('[a-zA-Z]+', raw)).upper()

    # returns the normalized conditional bigram frequency distribution
    def cond_prob(self):
        bigrams = nltk.bigrams(self.text)
        self.dist = nltk.ConditionalFreqDist(bigrams)
        for a in self.dist.keys():
            total = sum(self.dist[a].values())
            for b in self.dist[a].keys():
                self.dist[a][b] /= total
        return self.dist
