import unittest
from Scrambler import Scrambler


class ScrambleTester(unittest.TestCase):
    def test(self):
        word = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
        s = Scrambler()
        scrambled, cipher = s.scramble(word)
        assert scrambled != word
        unscrambled = s.unscramble_with_cipher(scrambled, cipher)
        assert unscrambled == word