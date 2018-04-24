import random
import numpy as np


class HillClimbingRunner:
    """
    g: proposal density
    s: scrambled text
    x: initial candidate
    xs: function for picking next candidate
    f: evaluation function for candidate
    """

    def __init__(self, g, s, x, xs, f):
        self.g = g
        self.s = s
        self.x = x
        self.xs = xs
        self.f = f

    # runs iterations of the hill-climbing algorithm
    def run(self):
        xp = self.xs(self.x)
        a = self.f(self.x, self.s, self.g) / self.f(xp, self.s, self.g)
        if a > 1:
            self.x = xp


class MetropolisRunner:
    """
    g: proposal density
    s: scrambled text
    x: initial candidate
    xs: function for picking next candidate
    f: evaluation function for candidate
    """

    def __init__(self, g, s, x, xs, f):
        self.g = g
        self.s = s
        self.x = x
        self.xs = xs
        self.f = f

    # runs iterations of the metropolis algorithm
    def run(self):
        xp = self.xs(self.x)
        a = self.f(self.x, self.s, self.g) / self.f(xp, self.s, self.g)
        u = random.uniform(0, 1)
        if u <= a:
            self.x = xp


class MetropolisHastingsRunner:
    """
    g: proposal density
    s: scrambled text
    x: initial candidate
    xs: function for picking next candidate
    f: evaluation function for candidate
    """

    def __init__(self, g, s, x, xs, f):
        self.g = g
        self.s = s
        self.x = x
        self.xs = xs
        self.f = f

    # runs iterations of the metropolis-hastings algorithm
    def run(self):
        xp = self.xs(self.x)
        if self.f(xp, self.s, self.g) > self.f(self.x, self.s, self.g):
            self.x = xp
        elif random.uniform(0, 1) <= self.f(xp, self.s, self.g) / self.f(self.x, self.s, self.g):
            self.x = xp


class SimulatedAnnealingRunner:
    """
    g: proposal density
    s: scrambled text
    x: initial candidate
    xs: function for picking next candidate
    f: evaluation function for candidate
    t: starting temperature
    rate: rate of annealing
        """

    def __init__(self, g, s, x, xs, f, t=100, rate=0.3):
        self.g = g
        self.s = s
        self.x = x
        self.xs = xs
        self.f = f
        self.t = t
        self.rate = rate

    # runs iterations of the simulated-annealing algorithm
    def run(self):
        self.t = max(0.00000001, self.t * self.rate)
        xp = self.xs(self.x)
        delta = self.f(xp, self.s, self.g) - self.f(self.x, self.s, self.g)
        if delta > 0:
            self.x = xp
        elif np.exp(delta / self.t) > random.uniform(0, 1):
            self.x = xp
