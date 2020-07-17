from banner import *
from utils import egcd,modinv,Convert
banner()

try:
    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))
    p = int(input("==> p = "))
    q = n//p
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    Convert(decrypt)
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
