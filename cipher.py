"""
Cipher abbreviations

a = Atbash
c = Caesar

mode 0 = encrypt
mode 1 = decrypt
"""


class Cipher:
    def __init__(self, key='0', text='', ctype='c', mode=0):
        self._key = key
        self._text = text
        self._ctype = ctype
        self.mode = mode

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        # print("$ The cipher key has been set to " + str(self._key))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        # print("$ The text has been set.")

    @property
    def ctype(self):
        return self._ctype

    @ctype.setter
    def ctype(self, ctype):
        self._ctype = ctype

    def mode(self):
        if self.mode == 0:
            return 'Encrypting'
        else:
            return 'Decrypting'

    def toggle_mode(self):
        self.mode ^= 1

    def transform(self):
        if self._ctype == 'c' and self._key.isdigit():
            self._text = caesar(int(self._key), self._text, self.mode)
        elif self._ctype == 'a':
            self._text = atbash(self._text, self.mode)
        else:
            pass


def atbash(text, mode):
    """
    Encipher text using the Atbash Cipher.
    """
    intab = 'abcdefghijklmnopqrstuvwxyz'
    outtab = intab[::-1]
    trantab = str.maketrans(outtab, intab) if mode == 1 else str.maketrans(intab, outtab)
    return text.lower().translate(trantab)


def caesar(key, text, mode):
    """
    Encipher text using the Caesar Cipher.
    """
    # case-insensitive
    key = key % 26
    intab = 'abcdefghijklmnopqrstuvwxyz'
    outtab = intab[-key:] + intab[:-key]
    trantab = str.maketrans(outtab, intab) if mode == 1 else str.maketrans(intab, outtab)
    return text.lower().translate(trantab)

    # case-sensitive
    # WIP

