from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

q = deque()

res = -1
visited = [[0]*m for _ in range(n)]

step = [[0]*m for _ in range(n)]

def is_in_range(x,y):
    if x >=0 and x<n and y>=0 and y<m:
        return 1
    return 0

def can_go(x,y):
    if is_in_range(x,y) == 1 and a[x][y] == 1 and visited[x][y] == 0:
        return 1
    return 0

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = 1
    q.append((x,y))

def bfs():
    global res
    push(0,0,0)

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            res = step[x][y]

        for dx, dy in zip(dxs,dys):
            nx , ny = x+dx, y+dy
            # print(q)
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)


bfs()
print(res)
# print(step)
# print()


        








