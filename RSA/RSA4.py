from banner import *
from utils import Convert
banner()

try:
    c = int(input("==> c = "))
    n = int(input("==> n = "))
    d = int(input("==> d = "))
    
    decrypt = pow(c,d,n)
    Convert(decrypt)
except ValueError:
    slowprint("\n[-] c,n,d Must be Integer Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
