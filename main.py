import cipher

text1 = "Facts are stubborn, but statistics are more pliable."
text2 = "One should always play fairly when one has the winning cards."


if __name__ == '__main__':
    ciph = cipher.Cipher()
    ciph.key = 4
    ciph.text = text1

    print("\n=== INITIAL MESSAGE ===")
    print(text1)

    print("\n=== ENCRYPTED MESSAGE ===")
    ciph.transform()
    print(ciph.text)

    print("\n=== DECRYPTED MESSAGE ===")
    ciph.toggle_mode()
    ciph.transform()
    print(ciph.text)