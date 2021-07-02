t=int(input())
for i in range(t):
    d,x,y,z=list(map(int,input().split()))
    first= 7*x
    second= (d*y) + (z * (7-d))
    print(max(first,second))

