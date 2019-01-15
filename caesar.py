class CaesarCipher:
    def __init__(self, key=0, text=None):
        self.key = key
        self.text = text

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

    def encrypt(self):
        return


