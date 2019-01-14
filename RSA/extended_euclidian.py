def EEA(num_one, num_two):
    R0 = num_one
    R1 = num_two

    S0 = 1
    S1 = 0

    T0 = 0
    T1 = 1

    step = 0
    print("***** EEA Table *****\n")
    print("    R ----- Q ----- S ----- T")

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
        print("{}: {} ----- {} ----- {} ----- {}".format(step, R1, Q, S0, T0))

        step += 1

    print("The inverse of {} is {} mod {}".format(T0, T0, num_one))
    return T0 % num_one

num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

EEA(num_one, num_two)
