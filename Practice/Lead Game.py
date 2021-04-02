lead=0;sum_a=0;sum_b=0;a=[];b=[];n=int(input())
for i  in range(0,n):
    a.append(int(input()));b.append(int(input()))
    sum_a=sum_a+a[i];sum_b=sum_b+b[i]
    if (sum_a-sum_b)> lead:
        leader=1;lead=sum_a-sum_b
    elif (sum_b-sum_a)>lead:
        leader=2;lead=sum_b-sum_a

print(leader,lead)
