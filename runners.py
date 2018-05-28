import random
import numpy as np
import mpmath as mp

mp.dps = 50


def swap(x):
    xs = dict(x)
    k1, k2 = random.sample(xs.keys(), 2)
    xs[k1], xs[k2] = xs[k2], xs[k1]
    return xs


def metropolis_hastings(f, x, s, g):
    xc = swap(x)
    plx = f(x, s, g)
    plxc = f(xc, s, g)

    A = min(1, mp.exp(plxc) / mp.exp(plx))
    u = random.uniform(0, 1)
    if u <= A:
        x = xc
    return x


def metropolis(f, x, s, g):
    xc = swap(x)
    plx = f(x, s, g)
    plxc = f(xc, s, g)

    alpha = mp.exp(plxc) / mp.exp(plx)
    u = random.uniform(0, 1)
    if u <= alpha:
        x = xc

    return x


def neighbors(x):
    # optimize when awake
    n = []
    for k1 in x.keys():
        for k2 in x.keys():
            if k2 is not k1:
                c = dict(x)
                c[k1], c[k2] = c[k2], c[k1]
                if c not in n:
                    n.append(c)
    return n


def hill_climbing(f, x, s, g):
    n = neighbors(x)
    plx = f(x, s, g)
    for xc in n:
        plxc = f(xc, s, g)
        if plxc >= plx:
            plx = plxc
            x = xc
    return x


T = 100


def reset_temp():
    global T
    T = 100

    
def simulated_annealing(f, x, s, g, r=0.99):
    global T
    T = max(T * r, 2)
    xc = swap(x)
    delta = f(x, s, g) - f(xc, s, g)
    if delta < 0:
        x = xc
    elif np.exp(-(delta / T)) > random.uniform(0, 1):
        x = xc
    return x
