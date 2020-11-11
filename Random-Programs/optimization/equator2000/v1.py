import cmath,time,sys
a=float    
b=input
c=cmath.sqrt
d=print
e=str
def m():
 while True:
  d("L Q E")
  f=e(b(""))
  if f.lower()=="l":
   Y,X,Y2,X2=a(b("Y1 ")),a(b("X1 ")),a(b("Y2 ")),a(b("X2 "))
   L(X,Y,X2,Y2)
  elif f.lower()=="q":
   x=a(b("a "))
   y=a(b("b "))
   z=a(b("c "))
   rQ(x,y,z)
  elif f.lower()=="e":
   sys.exit(0)
def rQ(x,y,z):
 d("J=Cmp")
 xRA=-y+z((y**2)-4*(x*c))/2*x
 d("xRA="+xRA)
 xRB=-y-z((y**2)-4*(x*c))/2*x
 d("xRB="+xRB)
 xV=(xRA+xRB)/2
 yV=(a*xV)**2+b*xV+c
 d("VCoords%s,%s"%(yV,xV))
 b("")
def L(X,Y,X2,Y2):
 sL,dY,dX=0,Y-Y2,X-X2
 if dX!=0: sL=dY/dX
 elif dX: d("0Div!")
 b=Y-sL*X
 d("y="+e(sL)+"x+"+e(b))
m()