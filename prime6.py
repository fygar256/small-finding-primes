def s(n):
 for p in m:
  if n%p==0:return 0 
 return 1
m=[]
for i in range(2,100):
 if s(i):m+=[i];print(i)
