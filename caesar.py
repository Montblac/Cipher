"""
Cipher abbreviations

c = Caesar
"""

class Cipher:
    def __init__(self, key=0, text=None, mode=0):
        self.key = key
        self.text = text
        self.mode = mode

    @property
    def key(self):
        return self.key

    @key.setter
    def key(self, key):
        self.key = key
        print("$ The cipher key has been set to " + self.key)

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
        self.text = text
        print("$ The text has been set.")

    def transform(self):
        if self.enc == 'c':
            caesar(self.key, self.text, self.mode)
        else:
            pass


def caesar(key, text, mode):
    result = ''
    for char in text:
        if mode == 0:
            result += chr((ord(char) + key) % 26)
        else:
            result += chr((ord(char) - key) % 26)
    return result
