import cipher
import random

if __name__ == '__main__':
    ciph = cipher.Cipher(ctype='a')

    texts = [
        "Facts are stubborn, but statistics are more pliable.",
        "One should always play fairly when one has the winning cards."
    ]
    keys = [0, 1, 5, 10, 20, 30, 45, 51, 53, 60, 120]

    ciph.key = random.choice(keys)
    print("Key used:", ciph.key, "\n")

    for text in texts:
        ciph.text = text
        print("  Initial MSG: " + text)

        ciph.transform()
        print("Encrypted MSG: " + ciph.text)

        ciph.toggle_mode()
        ciph.transform()
        print("Decrypted MSG: " + ciph.text + "\n")
