N = int(input())
num = list(map(int, input().split()))

# Please write your code here.

min_res = 99999

flag = 0
 

def jump(idx,cnt):

    global flag
    global min_res

    if idx >=N-1 :
        min_res = min(min_res,cnt)
        flag = 1
        return
    
    for i in range(1,num[idx]+1):
        jump(idx+i,cnt+1)


jump(0,0)

if flag == 1:
    print(min_res)
else:
    print(-1)
