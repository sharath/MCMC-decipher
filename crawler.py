import re
import string
import numpy as np

alphabet = string.ascii_uppercase + ' '


def cbpd_from_book(book):
    text = sanitize(open(book, 'r').read())
    g = {}
    for c1 in alphabet:
        g[c1] = {}
        for c2 in alphabet:
            g[c1][c2] = 0

    for i in range(0, len(text) - 1):
        g[text[i]][text[i + 1]] += 1

    for c1 in g.keys():
        total = sum(g[c1].values())
        for c2 in g[c1].keys():
            g[c1][c2] = g[c1][c2] / total

    return g

def cbfd_from_book(book):
    text = sanitize(open(book, 'r').read())
    h = np.zeros((len(alphabet), len(alphabet)))
    for c1 in alphabet:
        for c2 in alphabet:
            h[alphabet.index(c1)][alphabet.index(c2)] = 0

    for i in range(0, len(text) - 1):
        h[alphabet.index(text[i])][alphabet.index(text[i + 1])] += 1
        
    return h


def sanitize(text):
    return ' '.join(re.findall("[a-zA-Z]+", text)).upper()
