n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 상하좌우
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            visited[i][j] =-1

res_arr = []
cnt = 0

def is_in_range(x,y):
    if x >=0 and x<n and y>=0 and y<n:
        return 1
    else:
        return 0

def can_join(x,y):
    if is_in_range(x,y) == 1 and grid[x][y] == 1 and visited[x][y] == 0:
        return 1
    else:
        return 0
            

def dfs(x,y):
    global cnt
    cnt+=1

    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy

        if can_join(nx,ny):
           
            
            visited[nx][ny] = 1
            # print(visited)
            dfs(nx,ny)
            


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j]=1
            dfs(i,j)
            res_arr.append(cnt)
            cnt =0

# print(visited)

res_arr = [ e for e in res_arr if e != 0]

print(len(res_arr))

for e in sorted(res_arr):
    print(e)

