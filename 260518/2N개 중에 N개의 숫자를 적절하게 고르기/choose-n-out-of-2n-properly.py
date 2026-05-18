import sys
n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

arr = []
min_res = sys.maxsize

visited = [0]*(2*n)



def calculate(visited):

    
    arr1 = [num[i] for i in range(2*n) if visited[i] == 1]
    arr2 = [num[i] for i in range(2*n) if visited[i] != 1]
    return abs(sum(arr1)-sum(arr2))


def find_min(current_num,cnt):
    global min_res
    if cnt == n:
        
        res = calculate(visited)
        min_res = min(min_res,res)
        return
    
    if current_num == 2*n:
        return

   
    visited[current_num] = 1
    find_min(current_num+1,cnt+1)
    visited[current_num] = 0
    find_min(current_num+1,cnt)

find_min(0,0)
print(min_res)




