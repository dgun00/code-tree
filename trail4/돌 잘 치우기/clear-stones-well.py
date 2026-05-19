from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.

q = deque()

visited = [[0]*n for _ in range(n)]
block_pos = []
deleted_block = []

res = 0
max_res = -1

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def is_in_range(x,y):
    if x >=0 and x<n and y>=0 and y<n:
        return 1
    else:
        return 0

def can_go(x,y):
    if is_in_range(x,y) == 1 and grid[x][y] == 0 and visited[x][y]==0:
        return 1
    else:
        return 0

def bfs(st_x,st_y):
    cnt = 0
    if visited[st_x][st_y] == 0:
        q.append((st_x,st_y))
        visited[st_x][st_y] = 1
        cnt += 1

    while q:
        x,y = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            
            if can_go(nx,ny):
                # print(nx,ny)
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx,ny))

    return cnt


def delete_block(cnt,st_idx):
    global visited
    global res
    global max_res

    if cnt == m:
        # print(grid)
        for x,y in zip(r,c):
            res += bfs(x,y)
            max_res = max(res,max_res)
        visited = [[0]*n for _ in range(n)]
        res = 0

        return

    for i in range(st_idx, len(block_pos)):
        x, y = block_pos[i]
        
        grid[x][y] = 0
        delete_block(cnt+1,i+1)
        grid[x][y] = 1




for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            block_pos.append((i,j))

delete_block(0,0)
print(max_res)


