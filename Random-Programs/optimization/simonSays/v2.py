import random, time, os
def m(): 
    l, t, d = 3, 2, 1
    while l > 0: 
        os.system("clear")
        S = ran(d)
        print("life:" + str(l) + "\nSimon Says:" + S)
        time.sleep(t)
        d, t = ((d + 1), (t - 0.01))
        os.system("clear")
        if input("Rpt: \n>> ") != S: print("fail"), l -= 1, d == 1
    print("PTS:" + str(d))
def ran(d): 
    n = ""
    for _ in range(d) : n += str(random.randint(0, 9))
    return n
m() 