from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

finish = 0
q = deque()

visited = [[0]*m for _ in range(n)]


def is_in_range(x,y):
    if x>=0 and x<n and y>=0 and y<m:
        return 1
    else:
        return 0



def can_go(x,y):
    if is_in_range(x,y) == 1 and a[x][y] == 1 and visited[x][y]==0:
        return 1
    else:
        return 0


def bfs():
    global finish
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            
            if can_go(nx,ny): 
                if nx == n-1 and ny == m-1:
                    finish = 1
                    break
                q.append((nx,ny))
                visited[nx][ny]=1

bfs()
print(finish)