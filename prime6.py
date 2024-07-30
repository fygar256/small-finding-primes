#!/usr/bin/python3

import sys
import math

prime=[]
def sub1(n):
    for p in prime:
        if math.sqrt(n)<p:
            return True
        if n%p==0:
            return False
    return True

def main():
    global prime
    n=int(sys.argv[1])
    for i in range(2,n+1):
        if sub1(i):
            prime+=[i]
    print(f"{len(prime)} primes{prime}")

if __name__=="__main__":
    main()

