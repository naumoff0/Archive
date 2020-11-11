import random, time, os
def m(): 
    l, t, d = 3,0.5,1
    o=input("Opp\n0)Yes\n1)No\n:")
    while l>0: 
        S=r(d,"")
        print("Lives:"+str(l)+"\nSimon Says:"+str(S))
        time.sleep(t*d)
        os.system("clear")
        if int(input("RPT\n>> "))!=S: l=(l - 1)
        else: d+=1
    print("PTS:"+str((d-3)))
def r(d,n): 
    for _ in range(d) : n = n + str(random.randint(0, 9))
    return int(n)
m() 