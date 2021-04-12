def result(n):
    if (n==1):
        return 20
    elif (n==2):
        return 36
    elif (n==3):
        return 51
    elif (n==4):
        return 60
    else:
        rem=n%4
        res=((n-rem)//4)*44
        if (rem==0):
            res+=16
        elif (rem==1):
            res+=16*2
        elif (rem==2):
            res+=44
        elif (rem==3):
            res+=55
        return res

t=int(input())
for i in range(t):
    n=int(input())
    print(result(n))
