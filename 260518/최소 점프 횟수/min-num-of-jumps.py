N = int(input())
num = list(map(int, input().split()))

# Please write your code here.

min_res = 99999
res = 0
flag = 0
def is_in_range(n):
    return n < N 

def jump(n):
    global res
    global flag
    global min_res
    if N == n+1:
        min_res = min(min_res,res)
        flag = 1
        return
    
    for i in range(1,num[n]+1):
        if is_in_range(n+i):
            res +=1
            
            jump(n+i)
            res -=1

jump(0)
if flag == 1:
    print(min_res)
else:
    print(-1)
