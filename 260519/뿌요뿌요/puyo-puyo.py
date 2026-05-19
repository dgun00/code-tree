n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

cnt = 0
max_cnt = -1
boom_block_cnt = 0

def is_in_range(x,y):
    if x >= 0 and x<n and y>=0 and y<n:
        return 1
    else:
        return 0


def can_go(x,y,prev_n):
    if is_in_range(x,y) == 1 and prev_n == grid[x][y] and visited[x][y] ==0:
        return 1
    else:
        return 0

def dfs(x,y):
    global cnt
    
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx , y+dy

        if can_go(nx,ny,grid[x][y]):
            # print(nx,ny)
            cnt +=1
            visited[nx][ny] = 1
            dfs(nx,ny)



for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(i,j)
            if cnt >=4:
                boom_block_cnt +=1
            max_cnt = max(cnt,max_cnt)


print(boom_block_cnt, max_cnt)