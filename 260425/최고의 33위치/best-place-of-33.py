n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = -1


for j in range(n):
    if j-1 < 0 or j+1 > n-1:
        continue
    for i in range(n):
        cnt = 0
        if i-1 <0 or i+1 > n-1:
            continue
    
        if grid[i-1][j-1]:
            cnt+=1
        if grid[i][j-1]:
            cnt+=1
        if grid[i+1][j-1]:
            cnt+=1
        if grid[i-1][j]:
            cnt+=1
        if grid[i][j]:
            cnt+=1
        if grid[i+1][j]:
            cnt+=1
        if grid[i-1][j+1]:
            cnt+=1
        if grid[i][j+1]:
            cnt+=1
        if grid[i+1][j+1]:
            cnt+=1 

        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt) 
            

