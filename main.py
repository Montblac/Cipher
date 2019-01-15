import caesar


text1 = "Facts are stubborn, but statistics are more pliable."
text2 = "One should always play fairly when one has the winning cards."


if __name__ == '__main__':
    caesar = caesar.CaesarCipher()
    print(caesar.getKey())
    print(caesar.getText())
    caesar.setText(text1)
    print(caesar.getText())

