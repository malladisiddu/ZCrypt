from banner import *
from utils import Convert
banner()

try:
    n = int(input("==> n = "))
    d = int(input("==> d = "))
    c = int(input("==> c = "))
    
    decrypt = pow(c,d,n)
    Convert(decrypt)
except ValueError:
    slowprint("\n[-] c,n,d Must be integer number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
