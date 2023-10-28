from banner import *
from utils import *
from factorizations.factordb import *
banner()
'''
==> c = 61755320155925494660551920761454463487401548279688672761033639271968447552538039977698223026933796912494116347243805242200612025326482838810791756260085509550131713662597497521153195111273693512858774027842245708759910171933236029123361890400870896212504017945900641684931685449796719984403627813045065427962
==> n = 75267542047891848594630737311377686328322054122372174893906679499848429933554461483262840858561421691196745054401234786962886383772042458390620571955008818482322126005048853034866519574149834251335018597072237820298484967761635887969772946574871350539523281304243297613418863668754341179466678536081767878689
==> e = 65537

'''

try:

    def factordb(n):
    	f = FactorDB(n)
    	f.connect()
    	return f.get_factor_list()
    
    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))
    
    factordb = factordb(n)
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decrypt = pow(c,d,n)
    convert(decrypt)
    
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
