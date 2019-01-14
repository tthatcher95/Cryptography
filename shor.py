import numpy as np

P = int(input("Enter P: "))
Q = int(input("Enter Q: "))
a = int(input("Enter a: "))

f = 1
current = 0

while(current % (P*Q) != 1):
    current = a ** f
    print("Current f: {} Mod: {}".format(f, current % (P*Q)))
    f += 1
