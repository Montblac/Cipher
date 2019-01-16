import cipher
import random

text1 = "Facts are stubborn, but statistics are more pliable."
text2 = "One should always play fairly when one has the winning cards."


if __name__ == '__main__':
    ciph = cipher.Cipher()
    keys = [0, 1, 5, 10, 20, 30, 60, 120]
    texts = [text1, text2]

    ciph.key = random.choice(keys)
    print("Key used:", ciph.key, "\n")

    for text in texts:
        ciph.text = text
        print("  Initial MSG: " + text)

        ciph.transform()
        print("Encrypted MSG: " + ciph.text)

        ciph.toggle_mode()
        ciph.transform()
        print("Decrypted MSG: " + ciph.text)
        print("\n")
