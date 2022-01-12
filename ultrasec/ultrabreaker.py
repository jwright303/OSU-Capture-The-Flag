from pwn import *
import sys

def random():
    sh = remote('chal.ctf-league.osusec.org', 4545)
    out  = sh.recvline().decode("utf-8")
    print(out)
    nonce = out.split(" ")[-1]
    nonceV = nonce[:-1]
    print(nonceV)
    sh.sendline(str(nonceV).encode())
    ret = sh.recvline()
    print(ret)

    needed1 = 3735925567
    needed2 = -559041729
        #print(needed)
        #print('-0x21524cc1')
    barr = 0xdeadb33f
    #barr = b'\x3f\xb3\xad\xde'
        #print(barr)

    sh.sendline(str(barr).encode())
    #sh.sendline(barr)
    ret = sh.recvline().decode("utf-8")
    print(ret)

    sh.close()
        #print(needed)

    return

def testW(word):
    sh = process('./ultrasecure')
    out  = sh.recvline(timeout=0.001).decode("utf-8")
    nonce = out.split(" ")[-1]
    nonceV = nonce[:-1]

    sh.sendline(str.encode(nonceV))
    ret = sh.recvline(timeout=0.01)
    print(ret)

    sh.sendline(str.encode(word))
    #sh.sendline(barr)
    ret = sh.recvline(timeout=0.01).decode("utf-8")
    if "wrong" not in ret.split(" "):
        print(ret)
        return 1
    sh.close()

    return 0

def main():
    random()
    
    return 0

main()
