from banner import *
banner()
print("""
[1] - RSA
[2] - XOR
[0] - Exit
""")
check = int(input("==> "))
if check == 2:
    banner()
    print("""
[1] - Single Byte XOR
[2] - Repeating Key XOR
[0] - Exit
     """)
    y = int(input("==> "))
    if y == 1:
    	os.system('tput reset')
    	import XOR.bruteforce
    elif y == 2:
    	os.system('tput reset')
    	import XOR.repeating_key
    else:
    	exit()
elif check == 1:
    banner()
    print("""
[1] - (c,n,e)
[2] - (c,p,q,e)
[3] - (c,n,e,{p or q})
[4] - (c,n,d)
[5] - (c1,c2,c3,n1,n2,n3)   [Hasted Broadcast Attack]
[6] - (c,e)                 [Small Exponent("e") Attack]
[7] - (c,p,q,dp,dq)         [Chinese Remainder Theorem]
[8] - (c,n,e)               [Fermat Factorization]
[9] - (c1,c2,n1,n2,e)       [Common Factor Attack]
[10] - (c1,c2,e1,e2,n)      [Common Modulus Attack]
[0] - Exit
	""")
    z = int(input("==> "))
    if int(z) >= 1 and int(z) <= 10:
        os.system('tput reset')
        exec('import RSA.RSA'+str(z))
    else:
        exit()
else:
     exit()

