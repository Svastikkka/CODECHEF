def count(n):
    chief=0
    morty=0
    for i in range(n):
        e=list(map(int,input().split()))
        res1 = sum(list(map(int, str(e[0]).strip())))
        res2 = sum(list(map(int, str(e[1]).strip())))
        if res1>res2:
            chief=chief+1
        elif res2>res1:
            morty=morty+1
        elif res2==res1:
            morty=morty+1
            chief=chief+1

    if chief >morty:
        return 0 , chief
    elif morty > chief:
        return 1 , morty
    elif morty == chief:
        return 2 , morty




t=int(input())
for i in range(t):
    n=int(input())
    res=list(count(n))
    print(res[0],res[1])

