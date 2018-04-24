from Runner import *
from TextCrawler import TextCrawler
from Scrambler import Scrambler
import random


def f(x, s, dist):
    p = 1
    for i in range(len(s) - 1):
        if dist[x[s[i]]][x[s[i + 1]]] == 0:
            p *= 0.00001
            continue
        p *= dist[x[s[i]]][x[s[i + 1]]]
    return p


def xs(x=None):
    if x is None:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
        x = dict()
        for c in alphabet:
            x[c] = c
        return dict(zip(random.sample(x.keys(), len(x.keys())), x.values()))
    k1, k2 = random.sample(x.keys(), 2)
    xp = dict(x)
    xp[k1], xp[k2] = xp[k2], xp[k1]
    return xp


def main():
    g = TextCrawler('ProjectGutenberg/Hamlet.txt').cond_prob()
    s, answer = Scrambler().scramble('ENTER HAMLET HAMLET TO BE OR NOT TO BE THAT IS')
    runners = [SimulatedAnnealingRunner, MetropolisHastingsRunner, MetropolisRunner, HillClimbingRunner]
    r = 0
    print(runners[r])
    runner = runners[r](g, s, xs(), xs, f)
    i = 0
    while Scrambler().unscramble_with_cipher(s, runner.x) != 'ENTER HAMLET HAMLET TO BE OR NOT TO BE THAT IS':
        if i % 2000 == 0:
            print(Scrambler().unscramble_with_cipher(s, runner.x))
        runner.run()
        i += 1


if __name__ == '__main__':
    main()
