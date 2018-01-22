from fractions import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def totient_function(p, q):
    return (p - 1) * (q - 1)

#choose the lower value that satisfies the conditions
#1 - a value greater than one
#2 - a value without common divisors with totient n (except one)
def choose_e(tn):
    for i in range(2, tn):
        if gcd(i, tn) == 1:
            return i