
def count(arr):
    sum=0
    for i in range(len(arr)-1):
        sum=sum+((max(arr[i],arr[i+1])-min(arr[i],arr[i+1]))-1)
    return sum

t=int(input())
for i in range(t):
    l=int(input())
    e=list(map(int,input().split()))
    print(count(e))
