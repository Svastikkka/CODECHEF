from collections import Counter
for i in range(int(input())):
    n=int(input())
    s=str(input())
    li=Counter(s)
    f="YES"
    for i in li.values():
        if i%2!=0:
            f="NO"
            break
    print(f)