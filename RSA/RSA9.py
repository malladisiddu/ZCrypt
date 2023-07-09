from banner import *
from utils import *
banner()

try:
    c1 = int(input("==> c1 = "))
    c2 = int(input("==> c2 = "))
    n1 = int(input("==> n1 = "))
    n2 = int(input("==> n2 = "))
    e = int(input("==> e = "))
    p = egcd(n1,n2)[0]
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p - 1) * (q1 - 1)
    phi2 = (p - 1) * (q2 - 1)
    d1 = modinv(e,phi1)
    d2 = modinv(e,phi2)
    m1 = pow(c1,d1,n1)
    Convert(m1)
    m2 = pow(c2,d2,n2)
    Convert(m2)
except TypeError:
	slowprint("\n[-] No common factor for n1, n2")
	exit()
except ImportError:
	slowprint("\n[-] Module Not Setup")
except ValueError:
	slowprint("\n[-] c1, c2, e, n1, n2 Must Be Integar Number")
except AssertionError:
	slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
	exit()
