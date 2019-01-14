def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t


    # Make x positive
    if (x < 0) :
        x = x + m0

    return x

def GenerateKeys(int bits):
    n = p * q
    p_1 = p - 1
    q_1 = q - 1

    tot_numerator = p_1 * q_1
    tot_denominator = math.gcd(p_1, q_1)
    tot = tot_numerator / tot_denominator

    if(e == 1 && e < tot && math.gcd(e, tot) == 0):
        return 0

    d = modInverse(tot)


def encrypt
