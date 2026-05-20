import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]
dp = [[0]*n for _ in range(n)]
cnt = 0

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def is_in_range(x,y):
        if x >= 0 and x<n and y>=0 and y<n:
                return 1
        return 0

def can_go(x,y,prev_v):
        if is_in_range(x,y) == 1 and prev_v < grid[x][y]:
                return 1
        return 0

def dfs(x,y):
        
        if dp[x][y] != 0:
                return dp[x][y]
        
        dp[x][y] =1


        for dx,dy in zip(dxs,dys):
                nx,ny = dx+x, dy+y

                if can_go(nx,ny,grid[x][y]):
                        dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
        return dp[x][y]        

for i in range(n):
        for j in range(n):
                dfs(i,j)

maxs = [
        max(e)
        for e in dp
]

print(max(maxs))