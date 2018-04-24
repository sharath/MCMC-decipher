import random


class Scrambler:
    def scramble(self, word):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
        cipher = dict()
        t = random.sample(alphabet, len(alphabet))
        for i in range(len(alphabet)):
            cipher[alphabet[i]] = t[i]
        scrambled = self.scramble_with_cipher(word, cipher)
        return scrambled, cipher

    def scramble_with_cipher(self, word, cipher):
        t = ''
        for c in word:
            t += cipher[c]
        return t

    def unscramble_with_cipher(self, scrambled, cipher):
        t = ''
        inv = dict(zip(cipher.values(), cipher.keys()))
        for c in scrambled:
            t += inv[c]
        return t
