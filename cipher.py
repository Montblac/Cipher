"""
Cipher abbreviations

c = Caesar

mode 0 = encrypt
mode 1 = decrypt
"""


class Cipher:
    def __init__(self, key=0, text=None, ctype='c', mode=0):
        self._key = key
        self._text = text
        self.ctype = ctype
        self.mode = mode

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
        print("$ The cipher key has been set to " + str(self._key))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        print("$ The text has been set.")

    def mode(self):
        if self.mode == 0:
            return 'Encrypting'
        else:
            return 'Decrypting'

    def toggle_mode(self):
        self.mode ^= 1

    def transform(self):
        if self.ctype == 'c':
            self._text = caesar(self.key, self.text, self.mode)
        else:
            pass


def caesar(key, text, mode):
    #case-insensitive
    key = key % 26
    intab = 'abcdefghijklmnopqrstuvwxyz'
    outtab = intab[-key:] + intab[:-key]
    trantab = str.maketrans(outtab, intab) if mode == 1 else str.maketrans(intab, outtab)
    return text.lower().translate(trantab)

    #case-sensitive
    """
    for char in text:
        if char.isalpha():

    result = ''
    for char in text:
        if mode == 0:

            (ord(char) + key - 64 ) % 64 + 64
            if val > 122:
                val = val % 122 + 97

            result += chr((ord(char) + key) % 26)
            print(ord(char) + key)
        else:
            result += chr((ord(char) - key) % 26)
    return result
    """