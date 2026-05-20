from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]
res_grid = [[n*n+1] * n for _ in range(n)]


dxs = [-1,1,0,0]
dys = [0,0,-1,1]

st_point =[
    (i,j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]

q = deque()

def is_in_range(x,y):
    if x >=0 and x<n and y>=0 and y<n:
        return 1
    return 0
 

def can_go(x,y):
    if is_in_range(x,y) == 1 and visited[x][y] == 0 and grid[x][y]!=0:
        return 1
    return 0

def push(x,y,s):
    q.append((x,y))
    visited[x][y] =1
    step[x][y] = s

def min_update():
    global res_grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                res_grid[i][j] = min(res_grid[i][j],step[i][j])

def bfs():

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy

            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

for x,y in st_point:
    push(x,y,0)

bfs()

# for x,y in st_point:
#     push(x,y,0)
#     bfs()
#     # print(step)
#     min_update()
#     # print(res_grid)
    
#     visited = [[0] * n for _ in range(n)]
#     step = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0 : # 안썩은귤
            step[i][j] = -1
        elif grid[i][j] == 2 :
            step[i][j] = 0
        elif grid[i][j] == 1 and step[i][j] == 0:
            step[i][j] = -2



for row in step:
    for e in row:
        print(e,end=" ")
    print()