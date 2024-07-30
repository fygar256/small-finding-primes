#!/usr/bin/python3
import sys
prime=[2]
def sub1(n):
    for p in prime:
        if n**0.5<p:
            return True
        if n%p==0:
            return False

def main():
    global prime
    n=int(sys.argv[1])
    for i in range(3,n+1):
        if sub1(i):
            prime+=[i]
    print(f"{len(prime)} primes{prime}")

if __name__=="__main__":
    main()
