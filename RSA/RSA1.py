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
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    Convert(decrypt)
    
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
