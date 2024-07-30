m=[2]
def s(n):
    for p in m:
        if n**0.5<p:
            return 1
        if not n%p:
            return 0
for i in range(3,int(input("N:"))+1):
    if s(i):
        m+=[i]
print(len(m),m)
