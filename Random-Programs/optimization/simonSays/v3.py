import random,time
t=input
O=range
j=str
P=time.sleep
W=random.randint
def u():
 l,c=3,1
 while l>0:
  s=w(c,"")
  print("%s %s"%(l,s))
  c+=1
  P(2)
  print("\n"*99)
  if t("")!=s:l,c=(l-1,c-1)
 print("%s"%c)
def w(d,n): 
 for _ in O(d):n+=j(W(0,9))
 return n
u()