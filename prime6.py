m=[]
for i in range(2,10**6):
 if all(i%x for x in m):m+=[i];print(i)
