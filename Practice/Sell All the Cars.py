T = list(map(int,input().split()))
for i in  range(0,T[0]):
    profit = 0
    N = list(map(int,input().split()))
    car = list(map(int, input().split()))
    for j in range(0,N[0]):
        if car[j] != 0 and car[j] != 1:
            profit=profit+car[j]-j

        else:
            profit=profit+car[j]
    print(profit % 1000000007)
    car.clear()

