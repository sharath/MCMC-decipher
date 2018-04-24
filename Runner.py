import random


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

    # runs iterations of the metropolis algorithm
    def run(self):
        xp = self.xs(self.x)
        if self.f(xp, self.s, self.g) > self.f(self.x, self.s, self.g):
            self.x = xp
        elif random.uniform(0, 1) <= self.f(xp, self.s, self.g) / self.f(self.x, self.s, self.g):
            self.x = xp
