from collections import defaultdict
from numpy import log
import crawler
import runners
import scrambler


def f(x, s, g):
    y = 0
    for i in range(0, len(s) - 1):
        v = g[x[s[i]]][x[s[i + 1]]]
        if v == 0:
            v = 1 / 50000000
        y += log(v)

    return y


def run(runner):
    print('\033c')
    g = crawler.cbpd_from_book('ProjectGutenberg/Hamlet.txt')
    o = crawler.sanitize(
        'ENTER HAMLET. HAMLET. To be, or not to be, that is the question: Whether ’tis nobler in the mind to suffer The slings and arrows of outrageous fortune')
    s = scrambler.scramble(o)
    x = dict(zip(crawler.alphabet, crawler.alphabet))

    iteration = 1
    # plotx = []
    # ploty = []
    max_iteration = 100000
    if runner == runners.hill_climbing:
        max_iteration = 70
    while iteration < max_iteration:  # and scrambler.unscramble_with_cipher(x, s) != o:
        # plotx.append(iteration)
        # ploty.append(-f(x, s, g))

        x = runner(f, x, s, g)

        print('\033c')
        print(runner)
        print('%d %s' % (iteration, scrambler.unscramble_with_cipher(x, s)))
        iteration += 1

    '''plt.title('Iterations vs Plausibility')
    plt.xlabel('Iterations')
    plt.ylabel('-log(Plausibility)')
    plt.plot(plotx, ploty, 'b', label='Plausibility')
    plt.legend(loc='best')
    plt.grid()
    plt.savefig('output.png')'''

    return scrambler.unscramble_with_cipher(x, s), iteration


def average(arr):
    avg = []
    for i in range(len(arr[0])):
        m = defaultdict(lambda: 0)
        for str in arr:
            m[str[i]] += 1
        k = max(m.items())
        avg.append(k[0])
    return ''.join(avg)


def metrics():
    measuring = [runners.metropolis, runners.metropolis_hastings, runners.simulated_annealing]
    '''[runners.hill_climbing, '''
    results = {}
    global T
    for r in measuring:
        results[r] = []

    for r in measuring:
        if r == runners.simulated_annealing:
            T = 100
        for i in range(3):
            unscrambled, iterations = run(r)
            results[r].append(unscrambled)

    for r in measuring:
        print(r, average(results[r]))


metrics()
