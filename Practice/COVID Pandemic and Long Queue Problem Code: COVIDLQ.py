t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=l.count(1)  # this will count how many times 1 is appear in l list
    r=[]
    q=0
    for i in range(n):
        if l[i]==1:
            r.append(i)
    x=len(r)
    for j in range(x-1):
        if (r[j+1]-r[j])>=6:
            q=q+1
    if (c-1)==q:
        print('YES')
    else:
        print('NO')