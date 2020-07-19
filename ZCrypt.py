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
    	os.system(clear)
    	import XOR.bruteforce
    elif y == 2:
    	os.system(clear)
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
[5] - (c1,c2,c3,n1,n2,n3,e) [Hasted Broadvast Attack]
[6] - (c,e)                 [Small Modulus Attack]
[0] - Exit
	""")
    z = int(input("==> "))
    if z == 1:
        os.system(clear)
        import RSA.RSA1
    elif z == 2:
        os.system(clear)
        import RSA.RSA2
    elif z == 3:
        os.system(clear)
        import RSA.RSA3
    elif z == 4:
        os.system(clear)
        import RSA.RSA4
    elif z == 5:
        os.system(clear)
        import RSA.RSA5
    elif z == 6:
        os.system(clear)
        import RSA.RSA7
    else:
        exit()
else:
     exit()
