from banner import *
from utils import modinv, Convert
banner()

try:
    
    c = int(input("==> c = "))
    p = int(input("==> p = "))
    q = int(input("==> q = "))
    e = int(input("==> e = "))
    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    Convert(decrypt)
    
except ImportError:
    slowprint("\n[-] Module not setup ")
except ValueError:
    slowprint("\n[-] p,q,e,c Must be Integer Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
