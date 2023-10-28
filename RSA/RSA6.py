from banner import *
from utils import convert
import gmpy2
import binascii
banner()
'''
==> c = 2029613660163843396903464782115528008655183225445848001281643028687992002927755695965369902157711827410470381085949600499524270486328046449551598001242088232771076726041029619343560895809087267563848414489258883125846714056071432180906074031501935662926108057389184049920101
Probably 'e' will be small
==> e = 3

'''

try:
    c = int(input("==> c = "))
    print("Probably 'e' will be small")
    e = int(input("==> e = "))
    m = gmpy2.iroot(c,e)[0]
    assert pow(m,e) == c
    convert(m)
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c Must Be Integer Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
    
