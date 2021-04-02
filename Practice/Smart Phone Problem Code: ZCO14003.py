num=int(input())
arr=[]
for i in range(0,num):
    arr.append(int(input()))
m=0
arr.sort()
for i in arr:
    if m<i*num:
        m=i*num
    num=num-1
print(m)
