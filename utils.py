import binascii
import gmpy2

def convert(decimal):
    hex_ = hex(decimal).replace("0x","").replace("L","")
    ascii = binascii.a2b_hex(hex_)
    print("\nPlainText in Decimal :",decimal)
    print("PlainText:",ascii.decode("utf-8"))

def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)
def modinv(a,m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('[-] Modular inverse does not exist')
    else:
        return x % m

