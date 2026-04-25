n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_score = -1
def form_1(y,x):
    score = grid[y][x]+grid[y-1][x]+grid[y][x-1]
    return score

def form_2(y,x):
    score = grid[y][x]+grid[y-1][x]+ grid[y][x+1]
    return score
def form_3(y,x):
    score = grid[y][x]+grid[y+1][x] + grid[y][x-1]
    return score
def form_4(y,x):
    score = grid[y][x]+grid[y+1][x] + grid[y][x+1]
    return score

# 3x1
for i in range(n):
    if i+2 > n-1:
        break
    for j in range(m):
        current_score = grid[i][j]+grid[i+1][j]+grid[i+2][j]
        if max_score < current_score:
            max_score = current_score
# 1x3
for i in range(n):
    for j in range(m):
        if j+2 > m-1:
            break
        current_score = grid[i][j]+grid[i][j+1]+grid[i][j+2]
        if max_score < current_score:
            max_score = current_score

for i in range(n):
    for j in range(m):
        
        if i-1 < 0 and j > 0 and j < m-1:
            max_score = max(max_score,form_3(i,j))
            max_score = max(max_score,form_4(i,j))
        if i+1 > n-1 and j > 0 and j < m-1:
            max_score = max(max_score,form_1(i,j))
            max_score = max(max_score,form_2(i,j))
        if j-1 < 0 and i > 0 and i < n-1:
            max_score = max(max_score,form_2(i,j))
            max_score = max(max_score,form_4(i,j))
        if j+1 > m-1 and i > 0 and i<n-1:
            max_score = max(max_score,form_1(i,j))
            max_score = max(max_score,form_3(i,j))
        if i==0 and j==0:
            max_score = max(max_score,form_4(i,j))
        if i==0 and j==m-1:
            max_score = max(max_score,form_3(i,j))
        if i==n-1 and j==0:
            max_score = max(max_score,form_2(i,j))
        if i==n-1 and j==m-1:
            max_score = max(max_score,form_1(i,j))

        if i >=1 and j >=1 and i <=n-2 and j <=m-2:
            max_score = max(max_score,form_1(i,j))
            max_score = max(max_score,form_2(i,j))
            max_score = max(max_score,form_3(i,j))
            max_score = max(max_score,form_4(i,j))


            


print(max_score)


        

    
