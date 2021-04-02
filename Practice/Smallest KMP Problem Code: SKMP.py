t=int(input())
for i in range(t):
    s=list(input().strip())
    s2=input()
    for j in s2:
        s.remove(j)
    s1=sorted(s)
    c1=0
    for j in s1:
        c1=c1+1
        if j != s2[0]:
            break
    for j in s2:
        s1.insert(c1-1,j)
    for j in s1:
        print(j,end="")
    print()




