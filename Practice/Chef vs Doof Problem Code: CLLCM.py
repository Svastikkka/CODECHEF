t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ec=0
    oc=0
    for j in range(len(l)):
        if l[j]%2==0:
            ec=ec+1
        else:
            oc=oc+1
    if ec>0:
        print("NO")
    else:print("YES")




