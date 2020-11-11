""" square root finder """
import time
import random
p=print
r=r
t=time.sleep
def m():
 """ main module """
 n = 0
 x = int(input("Number: "))
 n = 1
 z = random.randint(2, 20)
 while True:
  if r((z * z), 2) == r(x, 2):
   z = r(z, 4)
   q = z * z
   z = str(z)
   p(q)
   p(z.rstrip(z[:-4]))
   return
  elif r((z * z), 2) <= r(x, 2):
   z += r(((z * z)/10000), 4)
   p(z, end="\r")
   n += 1
   if n >= 1000:
    z += r(((z * z)/n), 2)
    if n >= 10000:
     p = z * z
     z = str(z)
     p(p)
     p(z.rstrip(z[:-4]))
     return
   time.sleep(.001)
  elif r((z * z), 2) >= r(x, 2):
   z -= r(((z * z)/10000), 4)
   n += 1
   if n >= 1000:
    z -= r(((z * z)/n), 2)
    if n >= 10000:
     p = z * z
     z = str(z)
     p(p)
     p(z.rstrip(z[:-4]))
     p(z, end="\r")
     return
   time.sleep(.001)
m()