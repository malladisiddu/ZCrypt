from banner import *
from utils import *
banner()
try:
    
    def fermat_factors(n):
        assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    return a + gmpy2.isqrt(b2), a - gmpy2.isqrt(b2)

    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))
    
    p, q = fermat_factors(n)
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    convert(decrypt)
except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c, e, n Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except requests.exceptions.ConnectionError:
    slowprint("\n[-] Check Your Internet")
except:
    slowprint("False Attack")