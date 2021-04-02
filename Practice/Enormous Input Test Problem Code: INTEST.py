m,n=list(map(int,input().split()))
count=0
for i in range(m):
    t=int(input())
    if t%n==0:
        count+=1
print(count)