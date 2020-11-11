from math import sqrt
def QUADEQ():
    print("What is A?")
    a = float(input(">> "))
    print("What is B?")
    b = float(input(">> "))
    print("What is C?")
    c = float(input(">> "))
    if a == 0:
        print("A CANNOT BE 0 YOU FOOOL")
    elif a:        
        XintA = ((b * -1) + (sqrt(( b ** 2) - (4 * a * c)))) / (2 * a)
        XintB = ((b * -1) - (sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
        XVert = (XintA + XintB) / 2 
        YVert = 1#runEQ(round(a,1),round(b,1),round(c,1), round(XVert,1))
        
def YMXB():
    print("What is X of point A?")
    AX = int(input(">> "))
    print("What is Y of point A?")
    AY = int(input(">> "))
    print("What is X of point B?")
    BX = int(input(">> "))
    print("What is Y of point B?")
    BY = int(input(">> "))
    SLP = (AY - BY) / (AX - BX)
    print("The slope is {}".format(SLP))
    if AY - AY != 0:
        AY == AY * -1
    PARAM = (SLP * AX)
    if AY - PARAM == 0:
        B = 0
    elif AY -  PARAM != 0:
        B == PARAM - AY
        
def runEQ(a,b,c,x):
    s = a(x ** 2) + b(x) + c
    round(s,2)
    return s