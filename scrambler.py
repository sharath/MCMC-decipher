import random
import string


def scramble(o):
    c1 = string.ascii_uppercase + ' '
    x = dict()
    c2 = random.sample(c1, len(c1))
    for i in range(len(c1)):
        x[c1[i]] = c2[i]
    scrambled = scramble_with_cipher(x, o)
    return scrambled


def scramble_with_cipher(x, o):
    s = ''
    for i in range(0, len(o)):
        s += x[o[i]]
    return s


def unscramble_with_cipher(x, s):
    u = ''
    for i in range(0, len(s)):
        u += x[s[i]]
    return u
