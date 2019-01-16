import cipher
import random

if __name__ == '__main__':
    '''
    ciph = cipher.Cipher(ctype='a')

    texts = [
        "Facts are stubborn, but statistics are more pliable.",
        "One should always play fairly when one has the winning cards."
    ]
    keys = ['0', '1', '5', '10',
            '20', '30', '45', '51',
            '53', '60', '120', '250']

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
    '''
    ciphers = ['a', 'c']
    ciph = cipher.Cipher()
    running = True

    print("Greetings, user! Welcome to a simple encipher and decipher program.\n")

    ciph.text = input("What is your message?\nMSG: ")
    print()

    while running:
        command = input("What would you like to do?\n"
                        " [1] Encipher\n"
                        " [2] Decipher\n"
                        " [3] Show message\n"
                        " [4] Change message\n"
                        " [5] Exit\n\n")

        if command in ['1', '2']:
            ciph.mode = 1 if command == '2' else 0

            cipher = input("What cipher would you like to use?\n"
                           " [a] Atbash\n"
                           " [c] Caesar\n\n")

            while cipher not in ciphers:
                cipher = input(" ERROR: Cipher does not exist!\n ")

            ciph.ctype = cipher

            if cipher in ['c']:
                ciph.key = input("Please provide an integer value to be used as a key:\n")
                while not ciph.key.isdigit():
                    key = input(" ERROR: Invalid key; please try again.\n ")

            ciph.transform()

        elif command == '3':
            print("MSG: " + ciph.text + "\n")

        elif command == '4':
            ciph.text = input("What is your new message?\nMSG: ")

        elif command == '5':
            running = not running
            print("Exiting program...")

        else:
            print("Invalid command; please try again.")

