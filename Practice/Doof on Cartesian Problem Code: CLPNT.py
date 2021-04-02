from bisect import bisect_left
def solve(n,aa):
    num=int(input())
    for j in range(num):
        x, y = map(int, input().split())
        position=bisect_left(aa,x+y)
        if position<n and aa[position]==x+y:
            print(-1)
        else:
            print(position)


t=int(input())
for i in range(t):
    n=int(input())
    aa=list(map(int,input().split()))
    aa.sort()
    solve(n,aa)



