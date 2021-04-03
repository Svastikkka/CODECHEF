n=int(input())
for i in range(n):
    m,k=list(map(int,input().split()))
    s=list(map(str,input().strip()))
    count=0
    maxx=0
    for j in range(len(s)):
        if s[j]=="*":
            count+=1
            if count>=maxx:
                maxx=count
        else:
            count=0
    if maxx>=k:
        print("YES")
    else:
        print("NO")





