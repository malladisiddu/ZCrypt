from banner import *
from utils import *
banner()

try:
    import gmpy2
    from Crypto.Util.number import GCD

    c1 = int(input("==> c1 = "))
    c2 = int(input("==> c2 = "))
    e1 = int(input("==> e1 = "))
    e2 = int(input("==> e2 = "))
    n = int(input("==> n = "))
    """
    def common_modulus(c1, c2, e1, e2, n):
        if GCD(e1, e2) != 1:
            raise ValueError("Exponents e1 and e2 must be coprime")
        t1 = int(modinv(e1,e2))
        t2 = int((GCD(e1,e2) - e1 * t1) / e2)
        t3 = int(modinv(c2, n))
        m1 = pow(c1,t1,n)
        m2 = pow(t3,-t2,n)
        return (m1 * m2) % n
    """
    def common_modulus(c1,c2,e1,e2,N):
        g, s, t = gmpy2.gcdext(e1, e2)
        assert e1 * s + e2 * t == 1
        if s < 0 and t > 0:
            c1i = gmpy2.invert(c1, N)
            m = (pow(c1i, -s, N) * pow(c2, t, N)) % N
        elif s > 0 and t < 0:
            c2i = gmpy2.invert(c2, N)
            m = (pow(c1, s, N) * pow(c2i, -t, N)) % N
        return m
    Convert(common_modulus(c1, c2, e1, e2, n))

except ValueError:
    slowprint("\n[-] c1, c2, e1, e2, n Must Be Integar Number")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()