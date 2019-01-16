import cipher

text1 = "Facts are stubborn, but statistics are more pliable."
text2 = "One should always play fairly when one has the winning cards."


if __name__ == '__main__':
    ciph = cipher.Cipher()
    ciph.key = 4
    texts = [text1, text2]

    for text in texts:
        ciph.text = text
        print("\n=== INITIAL MESSAGE ===")
        print(text)

        print("\n=== ENCRYPTED MESSAGE ===")
        ciph.transform()
        print(ciph.text)

        print("\n=== DECRYPTED MESSAGE ===")
        ciph.toggle_mode()
        ciph.transform()
        print(ciph.text)

        print("\n=== END MESSAGE ===\n")