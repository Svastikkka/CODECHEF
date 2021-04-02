T = list(map(int,input().split()))
for j in range(0,T[0]):
    N,Q=list(map(int,input().split()))
    n=list(map(int,input().split()))
    q=list(map(int,input().split()))

    for i in range(0,len(q)):
        print(max(n[:q[i]]))

