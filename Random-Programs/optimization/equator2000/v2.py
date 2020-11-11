import math
i=input
p=print    
f=float
def c():
 p("l\nq")
 if i("e:")=="l":m(x("x1"),x("x2"),x("y1"),x("y2"))
 else:q(x("a"),x("b"),x("c"))
def q(a,b,c):
 t=math.sqrt((b**2)-4*(a*c))
 z=b+t
 v=b-t
 p("x%s\nb%s"%(z,v))
 m=(z+v)/2
 p("v %s %s"%(m,(a*m)**2+b*m+c))
def m(q,w,e,r):  
 s=(q-w)/(e-r)
 p("y=%sx+%s"%(s,w-s*q))
def x(n):return f(i(n+":"))
c()