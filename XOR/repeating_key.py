from banner import *
from pwn import xor
import binascii
try:
    def repeating_key(c,key):
    	flag = xor(c,key)
    	return flag
    c = input("\n==> ciphertext(in hex) = ")
    key = input("\n==> key(in hex) = ")
    c = bytes.fromhex(c)
    key = bytes.fromhex(key)
    print("Output(in ascii): ",repeating_key(c,key))
    print("Output(in hex): ",binascii.hexlify(repeating_key(c,key)))
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
except:
    slowprint("Unknown Error")
