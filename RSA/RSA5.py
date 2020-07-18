from banner import *
from utils import Convert
import functools
import gmpy

banner()

def crt(n, a):
   sum = 0
   prod = functools.reduce(lambda a, b: a*b, n)
   for i,j in zip(n,a):
   	p = prod // i
   	sum += j * gmpy.invert(p,i) * p
   return sum % prod

try:
    c1 = int(input("==> c1 = "))
    c2 = int(input("==> c2 = "))
    c3 = int(input("==> c3 = "))
    n1 = int(input("==> n1 = "))
    n2 = int(input("==> n2 = "))
    n3 = int(input("==> n3 = "))
    
    N = [n1, n2, n3]
    C = [c1, c2, c3]
    e = len(N)
    a = crt(N,C)
    for n,c in zip(N, C):
    	assert a % n == c
    m = gmpy.root(a,e)[0]
    Convert(m)
except ValueError:
    slowprint("\n[-] c1,c2,c3,n1,n2,n3 Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
