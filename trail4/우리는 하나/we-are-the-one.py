from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

cnt = 0


max_res = -1

q = deque()


visited = [[0]*n for _ in range(n)]
selected_city = []

def is_in_range(x,y):
    if x >= 0 and x <n and y >=0 and y<n:
        return 1
    else:
        return 0
    

def can_go(x,y,prev_heigh):
    if is_in_range(x,y) == 1 and abs(prev_heigh - grid[x][y]) >= u and abs(prev_heigh - grid[x][y]) <= d \
        and visited[x][y] == 0:
        return 1
    else:
        return 0

def bfs(st_x,st_y):
    cnt = 0
    if visited[st_x][st_y] == 0:
        
        q.append((st_x,st_y))
        visited[st_x][st_y] = 1
        cnt+=1

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy

            if can_go(nx,ny,grid[x][y]):
                q.append((nx,ny))
                cnt+=1
                visited[nx][ny] = 1

    return cnt
# bfs(0,1)
# print(cnt)


def select_city(cnt,st_idx):
    global max_res
    if cnt == k:
        # print(selected_city)
        max_res = max(max_res,calc())
        return
    
    for i in range(st_idx,n*n):
        x = i // n
        y = i % n
        selected_city.append((x,y))
        select_city(cnt+1,i+1)
        selected_city.pop()

def calc():
    global visited 
    res = 0
    for x,y in selected_city:
        
        res += bfs(x,y)
       
    visited = [[0]*n for _ in range(n)]

    return res

select_city(0,0)


print(max_res)