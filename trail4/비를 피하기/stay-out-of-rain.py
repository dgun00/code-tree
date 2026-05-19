from collections import deque
import sys
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]
temp_step = [[n*n+1]*n for _ in range(n)]
res_grid = [[0]*n for _ in range(n)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

human_pos = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]
save_pos = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 3
]
q = deque()

def is_in_range(x,y):
    if x >=0 and x<n and y>=0 and y<n:
        return 1
    return 0

def can_go(x,y):
    if is_in_range(x,y) == 1 and grid[x][y] != 1 and visited[x][y] == 0:
        return 1
    return 0

def push(x,y,s):
    # global visited
    # global step
    visited[x][y] = 1
    q.append((x,y))
    step[x][y] = s

def bfs():

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy

            if can_go(nx,ny):
                # print(nx,ny)
                push(nx,ny,step[x][y]+1)

def min_path_update():
    global temp_step
    global step

    for x,y in human_pos:
        if visited[x][y] == 1:
            if temp_step[x][y] > step[x][y]:
                temp_step[x][y] = step[x][y]

    

for x,y in save_pos:

    q.append((x,y))
    visited[x][y] = 1
    bfs()

    
    min_path_update()

    # print(temp_step)

    visited = [[0]*n for _ in range(n)]
    step = [[0]*n for _ in range(n)]
    
for i in range(n):
    for j in range(n):
        
        if grid[i][j] == 2:
            if temp_step[i][j] == n*n+1:
                print(-1, end=" ")
            else:
                print(temp_step[i][j], end=" ")
        else:
            print(0, end=" ")
    print()











