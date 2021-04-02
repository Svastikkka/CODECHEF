a,b,c=list(map(int,input().split()))
if (a==b):
    print("YES")
elif (b==c):
    print("YES")
elif (c==a):
    print("YES")
else:
    print("NO")