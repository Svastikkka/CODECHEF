t=int(input())
for i in range(t):
    k1,k2,k3,T=list(map(float,input().split()))
    res=100/(((T*k1)*k2)*k3)
    if(round(res,2)<9.58):
        print("YES")
    else:
        print("NO")