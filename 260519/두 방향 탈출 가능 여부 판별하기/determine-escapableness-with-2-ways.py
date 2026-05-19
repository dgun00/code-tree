n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 아래, 오른쪽
dxs = [1,0]
dys = [0,1]

visited = [[0]*m for _ in range(n)]


res =0

def is_in_range(x,y):
    if x >=0 and x < n and y >= 0 and y < m:
        return 1
    else:
        return 0

# def is_block(x,y):
#     if grid[x][y] == 0:
#         return 1
#     else:
#         return 0

def can_go(x,y):
    if is_in_range(x,y) == 1 and grid[x][y]==1 and visited[x][y]==0:
        return 1
    else:
        return 0


def dfs(x,y):
    global res
    
    if x == n-1 and y == m-1:
        res = 1
        return 

    for dx ,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy

        if can_go(nx,ny) == 1:
            visited[nx][ny] = 1
            # print(nx,ny)
            # print(visited)
            dfs(nx,ny)



visited[0][0] = 1
dfs(0,0)
print(res)