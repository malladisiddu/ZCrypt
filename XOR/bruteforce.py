from banner import *
from pwn import xor
banner()
try:
    def bruteforce(ct):
    	flag = []
    	for i in range(255):
    		flag.append(xor(ct,i))
    	return flag
    c = input("\n==> ciphertext(in hex) = ")
    c = bytes.fromhex(c)
    print("Output: ",bruteforce(c))
except IndexError:
    slowprint("[-] Check the input")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] Check the input")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
