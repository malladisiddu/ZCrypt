from banner import *
from utils import *
from factorizations.factordb import *
banner()

try:

    def factordb(n):
    	f = FactorDB(n)
    	f.connect()
    	return f.get_factor_list()
    
    c = int(input("==> c = "))
    e = int(input("==> e = "))
    n = int(input("==> n = "))
    
    factordb = factordb(n)
    print(factordb)
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    Convert(decrypt)
    
except IndexError:
    slowprint("[-] Sorry can't factorize n ")
    slowprint("\n[!] Try to use Multi-Prime Attack ")
except ImportError:
    slowprint("\n[-] Module not setup")
except ValueError:
    slowprint("\n[-] c, e, n Must be integer number")
except AssertionError:
    slowprint("\n[-] Wrong data")
except KeyboardInterrupt:
    exit()
except requests.exceptions.ConnectionError:
    slowprint("\n[-] Check your internet")
except:
    slowprint("False Attack")
