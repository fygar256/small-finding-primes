def s(n):
 for p in m:
  if n%p==0:return 1 
 return 0
m=[]
print([i for i in range(2,1000) if s(i)==0])
