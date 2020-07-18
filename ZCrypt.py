from banner import *
banner()
print("""
[1] - RSA
""")
check = int(input("==> "))
if check == 1:
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
    x = int(input("==> "))
    if x == 1:
        os.system(clear)
        import RSA.RSA1
    elif x == 2:
        os.system(clear)
        import RSA.RSA2
    elif x == 3:
        os.system(clear)
        import RSA.RSA3
    elif x == 4:
        os.system(clear)
        import RSA.RSA4
    elif x == 5:
        os.system(clear)
        import RSA.RSA5
    elif x == 6:
        os.system(clear)
        import RSA.RSA7
    else:
        exit()
else:
     exit()
