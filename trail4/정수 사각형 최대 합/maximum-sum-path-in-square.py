n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
res_grid =[[0]*n for _ in range(n)]

# 초기설정
res_grid[0][0] = grid[0][0]
for i in range(1,n):
        res_grid[0][i] =+ res_grid[0][i-1] + grid[0][i]
        res_grid[i][0] =+ res_grid[i-1][0] + grid[i][0]


for i in range(1,n):
    for j in range(1,n):
        
        res_grid[i][j] = max(res_grid[i-1][j]+grid[i][j], res_grid[i][j-1]+grid[i][j])
print(res_grid[n-1][n-1])