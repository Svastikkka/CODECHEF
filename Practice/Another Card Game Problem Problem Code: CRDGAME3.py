import math

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    chef=round(math.ceil(x/9))
    raick=round(math.ceil(y/9))
    if raick<chef:
        print(1,"",raick)
    elif raick==chef:
        print(1," ",raick)
    else:print(0," ",chef)
