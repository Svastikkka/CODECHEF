t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    res=sorted(arr)
    largest_divisor=0
    for i in res:
        if k % i == 0:
            largest_divisor = i
    if largest_divisor  in arr:
        print(largest_divisor)
    else:
        print(-1)







