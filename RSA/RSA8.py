from banner import *
import requests
from utils import *
banner()

'''
==> c = 34556241321778409829234252125398866442939962978969873136382201333200206297769416951162831936418949110944528236841238586744303476629927641535254876274091175076941922589651878305163739775003504738994366530124198403734813628243872035689617702431533182356107612904165873395653564321632211827028395012552136557561
==> n = 58249221268117887085192679008666481391991742878175658044606254797052676155819469643550544167108699240617881767689293494057479101008755114805240541465257199228386194347185579064158612401962673691504221389762800553538973887572052975111188998739455329190241182045290899911336417224594604893583476744708037361423
==> e = 65537
'''
try:
    def fermat_factors(n):
        assert n % 2 != 0
        a = gmpy2.isqrt(n)
        b2 = gmpy2.square(a) - n
        while not gmpy2.is_square(b2):
            a += 1
            b2 = gmpy2.square(a) - n
        return a + gmpy2.isqrt(b2), a - gmpy2.isqrt(b2)

    c = int(input("==> c = "))
    n = int(input("==> n = "))
    e = int(input("==> e = "))
    
    p, q = fermat_factors(n)
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
