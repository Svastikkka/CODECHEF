# cook your dish here
try:    
    for _ in range(int(input())):
        f,t = map(int,input().split(' '))
        initial = 0
        total = 0
        for i in range(t):
            a,b = map(int,input().split(' '))
            cur_state = a - initial
            new_state = b - a
            if cur_state < 0 :
                cur_state = cur_state * -1
            if new_state < 0 :
                new_state = new_state * -1
            total = total + new_state + cur_state
            initial = b
        print(total)
except:
    pass