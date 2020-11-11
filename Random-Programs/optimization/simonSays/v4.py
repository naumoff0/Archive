import random,time
def u():
 l,c=3,1
 while l>0:
  s=w(c,"")
  print("%s %s"%(l,s))
  c+=1
  time.sleep(2)
  print("\n"*99)
  if input("")!=s:l,c=(l-1,c-1)
 print("%s"%c)
def w(d,n): 
 for _ in range(d):n+=str(random.randint(0,9))
 return n
u()