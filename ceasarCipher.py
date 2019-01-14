from PIL import Image
import numpy as np
import operator
from collections import OrderedDict

# Encrypt the messages
def encrypt(plain_text, key, xor=False):

    # Encrypting the message
    cipher = ""
    for letter in plain_text:
        ascii = ord(letter.upper())
        if ascii == 32:
            cipher += chr(ascii)
        elif letter.isdigit() and ascii != 32:
            if xor == True:
                new_letter = (ord(letter.upper()) ^ (int(key) % 10))
            else:
                new_letter = (ord(letter.upper()) + (int(key) % 10))
            if new_letter > 57:
                new_letter -= 9
            cipher += chr(new_letter )
        else:
            if xor == True:
                new_letter = (ord(letter.upper()) ^ (int(key) % 26))
            else:
                new_letter = (ord(letter.upper()) + (int(key) % 26))
            # new_letter = (ord(letter.upper()) ^ int(key)) + (int(key) % 26)
            if new_letter > 90:
                new_letter -= 26
            cipher += chr(new_letter)

    print("Encrypted: '{}' to '{}'".format(plain_text, cipher))
    return cipher

# Frequency anaylysis to break the ceasar cipher
def break_cipher(cipher, plain_text):
    eng_aplph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    most_frq_eng_alph = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    print('\n*** Breaking the cipher ***')
    counters = list(np.zeros(len(cipher)))
    counter_dict = dict(zip(cipher, counters))

    for letter in cipher:
        if letter == ' ':
            continue
        else:
            counter_dict[letter] += 1

    ordered = {k: v for k, v in sorted(counter_dict.items(), key=lambda x: x[1])}
    max_val = max(ordered.items(), key=operator.itemgetter(1))[0]

    for letter in most_frq_eng_alph:
        plain_inverse = ""
        new_key = ord(max_val.upper()) - ord(letter.upper())
        for val in cipher:
            if ord(val.upper()) == 32:
                plain_inverse += ' '
            else:
                new_letter = ord(val.upper()) - int(new_key) % 26

                if new_letter < 65 and new_letter != 32:
                    new_letter += 26
                plain_inverse += chr(new_letter)

        print("Using letter '{}' we got PT: {}".format(letter, plain_inverse))

        if(plain_inverse == plain_text.upper()):
            print('\n------ FOUND IT ------')
            print('The key is: {}'.format(abs(new_key)))
            print('The PT is: {}\n'.format(plain_inverse))
            return 0

# Decrypting the message
def decrypt(cipher, plain_text, bruteForce = False, xor = False):
    if bruteForce == True:
        max_key = 26
        print('\n*** Running Brute Fource Method ***')
        for val in range(1, int(max_key + 1)):
            plain_inverse = ""
            for letter in cipher:
                if ord(letter.upper()) == 32:
                    plain_inverse += chr(ord(letter.upper()))
                elif letter.isdigit() and ord(letter.upper()) != 32:
                    if xor == True:
                        new_letter = (ord(letter.upper()) ^ val % 10)
                    else:
                        new_letter = (ord(letter.upper()) - val % 10)

                    if new_letter < 48:
                        new_letter += 9
                    plain_inverse += chr(new_letter)

                else:
                    if xor == True:
                        new_letter = (ord(letter.upper()) ^ val % 26)
                    else:
                        new_letter = (ord(letter.upper()) - val % 26)
                    if new_letter < 65 and new_letter != 32:
                        new_letter += 26
                    plain_inverse += chr(new_letter)

            print("Key: '{}' produces: '{}'".format(val, plain_inverse))

            if(plain_inverse == plain_text.upper()):
                print('\n------ FOUND IT ------')
                print('The key is: {}'.format(val))
                print('The PT is: {}\n'.format(plain_inverse))
                return 0
    else:
        plain_inverse = ""
        key = int(input("Enter the decrypt key: "))
        for letter in cipher:
            if ord(letter.upper()) == 32:
                plain_inverse += chr(ord(letter.upper()))
            elif letter.isdigit() and ord(letter.upper()) != 32:
                if xor == True:
                    new_letter = (ord(letter.upper()) ^ int(key) % 10)
                else:
                    new_letter = (ord(letter.upper()) - int(key) % 10)
                if new_letter < 48:
                    new_letter += 9
                plain_inverse += chr(new_letter)

            else:
                if xor == True:
                    new_letter = (ord(letter.upper()) ^ int(key) % 26)
                else:
                    new_letter = (ord(letter.upper()) - int(key) % 26)
                if new_letter < 65 and new_letter != 32:
                    new_letter += 26
                plain_inverse += chr(new_letter)
        print("Decrypted: ", plain_inverse)

def vigenere_cipher(message, xor=False):
     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     keyword = input("Enter Keyword: ")
     keys = []
     cipher = ""
     length = 0

     for letter in keyword:
         keyNum = letters.find(letter.upper())
         keys.append(keyNum)

     for symbol in message:
         if symbol == ' ':
             cipher += ' '
         length = length % len(keyword)
         if xor == True and symbol != ' ':
             cipher += letters[(letters.find(symbol.upper()) ^ keys[length]) % 26]
             length += 1
         elif symbol != ' ':
             cipher += letters[(letters.find(symbol.upper()) + keys[length]) % 26]
             length += 1
     print("Encrypted: '{}' to '{}'".format(message, cipher))
     return cipher

def decrypt_vigenere(cipher, xor=False):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword = input("Enter Keyword: ")
    keys = []
    message = ""
    length = 0

    for letter in keyword:
        keyNum = letters.find(letter.upper())
        keys.append(keyNum)

    for symbol in cipher:
        if symbol == ' ':
            message += ' '
        length = length % len(keyword)
        if xor == True and symbol != ' ':
            message += letters[(letters.find(symbol.upper()) ^ keys[length]) % 26]
            length += 1
        elif symbol != ' ':
            message += letters[(letters.find(symbol.upper()) - keys[length]) % 26]
            length += 1

    return message



if __name__ == '__main__':
    plain_text = input("What is your plaintext? ")
    encrypt_type = input("XOR of Sub? (x or s) ")

    if(encrypt_type == 's'):

        v_or_c = input("Vigenere or Ceasar? (v or c) ")
        print('\n*** Encrypting ***')

        if v_or_c == 'v':
            cipher = vigenere_cipher(plain_text)
            print(cipher)
            print('\n')

        elif v_or_c == 'c':
            key = input("What is the key? ")
            cipher = encrypt(plain_text, key)
            print('\n')

        user_selection = input("Do you wanna try to break the cipher or just decrypt? (b or d) ")

        if user_selection == 'b':
            type_of_break = input("Brute Force or Frequecy Analysis? (b or f) ")
            if type_of_break == 'b':
                decrypt(cipher, plain_text, bruteForce = True)

            elif type_of_break == 'f':
                break_cipher(cipher, plain_text)

        elif user_selection == 'd' and v_or_c == 'v':
            print("Decrypted Cipher is: {}".format(decrypt_vigenere(cipher).lower()))
        elif user_selection == 'd' and v_or_c == 'c':
            decrypt(cipher, plain_text)

    elif(encrypt_type == 'x'):
        v_or_c = input("vigenere or Ceasar? (v or c) ")
        if v_or_c == 'v':
            cipher = vigenere_cipher(plain_text, xor=True)
            print(cipher)
        elif v_or_c == 'c':
            key = input("What is the key? ")
            cipher = encrypt(plain_text, key, xor=True)

        user_selection = input("Do you wanna try to break the cipher or just decrypt? (b or d) ")
        if user_selection == 'b':
            type_of_break = input("Brute Force or Frequecy Analysis? (b or f) ")
            if type_of_break == 'b':
                decrypt(cipher, plain_text, bruteForce = True, xor=True)

            elif type_of_break == 'f':
                print(cipher)
                break_cipher(cipher, plain_text)

        elif user_selection == 'd' and v_or_c == 'v':
            decrypt_vigenere(cipher, xor=True)
        elif user_selection == 'd' and v_or_c == 'c':
            decrypt(cipher, plain_text, xor=True)
