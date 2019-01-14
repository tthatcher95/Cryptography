import numpy as np
import random
import math

def isPrime(p):
    if(p==2):
        return True
    if(not(p&1)):
        return False
    return pow(2,p-1,p)==1

def EA(num_one, num_two):
    step = 0

    num_three = num_one % num_two

    while(num_one % num_two != 0):
        # print('Step:', step)
        # print('R{}: {}'.format(step, num_one))
        num_three = num_one % num_two
        num_one = num_two
        # print('R{}: {}'.format(step + 1, num_two))
        # print('R{}: {}'.format(step + 2, num_three))
        # print('\n')

        num_two = num_three

        step += 1

    return num_two

def EEA(num_one, num_two):
    R0 = num_one
    R1 = num_two

    S0 = 1
    S1 = 0

    T0 = 0
    T1 = 1

    step = 0
    print("***** EEA Table *****\n")
    print("    R ----- S ----- T")

    while R1 != 0:
        Q = int(R0 / R1)
        old_r = R1
        R1 = R0 - Q * R1
        R0 = old_r
        # print("R{}: {}".format(step, R1))

        old_s = S1
        S1 = S0 - Q * S1
        S0 = old_s

        old_t = T1
        T1 = T0 - Q * T1
        T0 = old_t
        # print("T{}: {}".format(step, T0))
        print("{}: {} ----- {} ----- {}".format(step, R1, S0, T0))

        step += 1

    print("The inverse of {} is {} mod {}".format(T0, T0, num_one))
    return T0 % num_one




def keyGen():
    ''' Generate  Keypair '''

    # # initialising primes
    correctEntry = False
    choice = input("Do you wanna enter a P, Q, and e? (y or n) ")

    while(correctEntry == False):
        if choice == 'y':
            p = int(input("Enter a prime P: "))
            while(not isPrime(p)):
                p = int(input("Enter a prime P: "))
            q = int(input("Enter a prime Q: "))
            while(not isPrime(q)):
                q = int(input("Enter a prime Q: "))
            minPrime = 0
            maxPrime = 1000
            cached_primes = [i for i in range(minPrime,maxPrime) if isPrime(i)]
            print("List of co-primes: ", cached_primes)
            e = int(input("Choose a co-prime of {}: ".format(p*q)))
            correctEntry = True

        elif choice == 'n':
            minPrime = 0
            maxPrime = 1000
            cached_primes = [i for i in range(minPrime,maxPrime) if isPrime(i)]
            correctEntry = True

            # #elsewhere in the code
            p = random.choice([i for i in cached_primes if minPrime<i<maxPrime])
            q = random.choice([i for i in cached_primes if minPrime<i<maxPrime])

        else:
            print("Invalid Choice, please try again.")

    #computing n=p*q as a part of the RSA Algorithm
    n=p*q

    # Compute phi(n)
    pn = (p-1)*(q-1)

    #checking the Following : whether e and lamda(n) are co-prime
    if(choice == 'n'):
        e = 0
        while EA(e,pn)!=1:
            e=random.randint(1,pn)

    #Determine the modular Multiplicative Inverse
    d = EEA(pn, e)

    print("\n*********  Using P, Q, P(n): {}, {}, {} *********".format(p, q, pn))
    print("*********  Using e, d:       {}, {}     *********".format(e, d))
    #return the Key Pairs
    return ((e,n), (d,n))

def encrypt(pk, message, pt_str=True):
    """ Perform RSA Encryption Algorithm"""
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    if(pt_str == False):
        cipher = (message) ** key % n
    else:
        cipher = [(ord(char) ** key) % n for char in message]
    #Return the array of bytes
    return cipher

def decrypt(pk, cipher, pt_str=True):
    '''Perform RSA Decryption Algorithm '''
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    if(pt_str == False):
        real_message = (int(cipher) ** key) % n
    else:
        message = [chr((int(char) ** key) % n) for char in cipher]
        real_message = ''.join(str(e) for e in message)


    #Return the array of bytes as a string
    return real_message

if '__main__':
    e, d = keyGen()
    plaintext = input("Number (n) or String (s) message? ")

    correctEntry = False
    while(correctEntry == False):
        if plaintext == 'n':
            pt = int(input("Enter a number: "))
            cipher = encrypt(e, pt, pt_str=False)
            print("Encrypted: ", cipher)
            message = decrypt(d, cipher, pt_str=False)
            print("Decrypted: ", message)
            correctEntry = True

        elif plaintext == 's':
            pt = input("Enter a string: ")
            cipher = encrypt(e, str(pt))
            print("Encrypted: ", cipher)
            message = decrypt(d, cipher)
            print("Decrypted: ", message)
            correctEntry = True

        else:
            print("Invalid Entry, run again")
