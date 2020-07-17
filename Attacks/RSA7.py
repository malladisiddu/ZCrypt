from banner import *
from utils import Convert
import gmpy2
import binascii
banner()

try:
    c = int(input("==> c = "))
    print("Probably 'e' will be small")
    e = int(input("==> e = "))
    m = gmpy2.iroot(c,e)[0]
    assert pow(m,e) == c
    Convert(m)
except ImportError:
    slowprint("\n[-] Module not setup")
except ValueError:
    slowprint("\n[-] c Must be integer number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
    
