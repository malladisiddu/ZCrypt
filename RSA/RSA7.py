from banner import *
from utils import modinv,convert
banner()
try:
    c = int(input("==> c = "))
    p = int(input("==> p = "))
    q = int(input("==> q = "))
    dp = int(input("==> dp = "))
    dq = int(input("==> dq = "))

    slowprint("\n[+] Please Wait ...\n")
    def chinese_remainder_theorem(p,q,dp,dq,cipher_text):
        q_inv = modinv(p , q)
        m1 = pow(cipher_text,dp,p)
        m2 = pow(cipher_text,dq,q)
        h = (q_inv*(m1-m2)) % p
        return m2 + h * q
    convert(chinese_remainder_theorem(p,q,dp,dq,c))
except ValueError:
    slowprint("\n[-] c,p,q,dp,dq Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
