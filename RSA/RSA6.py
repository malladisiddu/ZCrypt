from banner import *
from utils import egcd,modinv,Convert
from factorizations.factordb import *
banner()

try:
    def factordb(n):
    	f = FactorDB(n)
    	f.connect()
    	return f.get_factor_list()
    	
    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))
    
    primes = factordb(n)
    print(primes)
    phi = 1
    for i in primes:
    	phi *= i-1  
    print(phi)	
    d = modinv(e,phi)
    m = pow(c,d,n)
    Convert(m)
    
except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,n,e Must Be Integer Number")
except KeyboardInterrupt:
    exit()
except:
    slowprint("[-] False Attack !")
