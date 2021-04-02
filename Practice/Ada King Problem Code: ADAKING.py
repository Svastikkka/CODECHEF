def chessFun(n,chess):
    for i in range(n):
        if i==0:
            continue
        chess[i]="."
    return (chess)

t=int(input())
for i in range(t):
    n=int(input())
    chess = ["O","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]
    res=chessFun(n,chess)
    for j in range(64):
        if j%8==0:
            print()
        print(res[j],end="")


