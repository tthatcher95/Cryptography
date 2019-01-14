import numpy as np
from sympy import *

def EEA(num_one, num_two):
    R0 = num_one
    R1 = num_two

    S0 = 1
    S1 = 0

    T0 = 0
    T1 = 1

    step = 0
    # print("***** EEA Table *****\n")
    # print("    R ----- Q ----- S ----- T")

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
        # print("{}: {} ----- {} ----- {} ----- {}".format(step, R1, Q, S0, T0))

        step += 1

    # print("The inverse of {} is {} mod {}".format(T0, T0, num_one))
    return T0 % num_one

def poly(m):
    poly = input("Enter a polynomial: ")
    x_val = int(input("Enter an X Value: "))
    x, y, z = symbols("x y z")
    poly = sympify(poly)
    y_val = poly.subs(x, x_val)
    print("Starting (x,y): {}".format((x_val, y_val % m)))
    return (x_val, y_val % m)

def point_doubling(x1, y1, m, a):
    y1_inv = EEA(m, 2*y1)
    s = ((3*(x1**2) + a) * y1_inv) % m
    x3 = ((s**2)-x1-x1) % m
    y3 = (s*(x1-x3) - y1) % m
    return (x3, y3)

def point_addition(x1, x2, y1, y2, m):
    x_inv = EEA(m, (x2 - x1) % m)
    s = ((y2 - y1) * x_inv) % m
    x3 = ((s**2)-x1-x2) % m
    y3 = (s*(x1-x3) - y1) % m
    return (x3, y3)

def get_cyclic_group(x, y, m, a):
    y_inv = EEA(m, y)
    cyclic_group = []
    d_or_a = 0
    p = 1
    orig_x = x
    new_x = x
    new_y = y
    print("P{}: {} {}".format(p, new_x, new_y))
    cyclic_group.append((new_x, new_y))
    p += 1
    new_x, new_y = point_doubling(new_x, new_y, m, a)
    cyclic_group.append((new_x, new_y))
    print("P{}: {} {}".format(p, new_x, new_y))
    p += 1
    a_x = new_x
    a_y = new_y
    while(a_x != orig_x):
        a_x, a_y = point_addition(x, a_x, y, a_y, m)
        cyclic_group.append((a_x, a_y))
        d_or_a = 0
        print("P{}: {} {}".format(p, a_x, a_y))
        p += 1

    return cyclic_group, p

def key_exchange():
    a = int(input("Enter the a value: "))
    m = int(input("Enter m: "))
    (x, y) = poly(m)
    cyclic_group, p = get_cyclic_group(x, y, m, a)
    a = int(input("Choose an a (0 - {}): ".format(m)))
    b = int(input("Choose a  b (0 - {}): ".format(m)))
    A = a
    B = b
    a_key = cyclic_group[((a * B) % p) - 1]
    b_key = cyclic_group[((b * A) % p) - 1]
    print("({} x {})P = {}P mod {} = {}P = {}".format(a, b, (a*b), p, ((a * B) % p), a_key))
    print("A Key: {}".format(a_key))
    print("B Key: {}".format(b_key))

key_exchange()
# print("(9,16) + (9, 16) = {} ".format(point_addition(9, 9, 16, 16, 17)))
# print("(9,16) + (9, 16) = {} ".format(point_doubling(9, 16, 17, 2)))
# print("(9,16) + (5, 16) = {} ".format(point_addition(9, 5, 16, 16, 17)))
#
# print(EEA(17, 0))
