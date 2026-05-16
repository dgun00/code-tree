n, m, t = map(int, input().split())

r = []
c = []
d = []
w = []

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    w.append(int(wi))

# Please write your code here.
grid = [[0]*n for _ in range(n)]

def dir_reflect(dir):
    if dir == "U":
        return "D"
    elif dir == "D":
        return "U"
    elif dir == "L":
        return "R"
    elif dir == "R":
        return "L"

def dir_to_idx(dir):
    if dir == "U":
        return 0
    elif dir == "D":
        return 1
    elif dir == "L":
        return 2
    elif dir == "R":
        return 3

def is_in_range(x,y):
    if x >=0 and x < n and y >=0 and y < n:
        return 1
    else:
        return 0

def simulation():
    
    move()
    crash()


def crash():

    global r,c,d,w
    crashed_idx = []
    crashed_w = 0
    for i in range(n):
        for j in range(n):

            if grid[i][j] > 1:
                for idx in range(len(r)):
                    if r[idx]-1 == i and c[idx]-1==j:
                        crashed_idx.append(idx)
                    
                for k in range(len(crashed_idx)-1):
                    crashed_w += w[crashed_idx[k]]
                    r[crashed_idx[k]] = -1
                    c[crashed_idx[k]] = -1
                    d[crashed_idx[k]] = -1
                    w[crashed_idx[k]] = -1

                # print(crashed_idx)
                w[crashed_idx[-1]] += crashed_w
                grid[i][j] = 1
            crashed_idx = []
            crashed_w = 0
    
    r = [e for e in r if e != -1]
    c = [e for e in c if e != -1]
    d = [e for e in d if e != -1]
    w = [e for e in w if e != -1]
    
def move():
    temp_grid = [[0]*n for _ in range(n)]

    for i in range(len(r)):
        dir = dir_to_idx(d[i])
        # 진행
        if is_in_range(r[i]-1+dx[dir],c[i]-1+dy[dir]):
            temp_grid[r[i]-1+dx[dir]][c[i]-1+dy[dir]] +=1
            r[i] += dx[dir]
            c[i] += dy[dir]
        # 반사
        else:
            d[i] = dir_reflect(d[i])
            temp_grid[r[i]-1][c[i]-1] +=1

    grid[:] = temp_grid[:]

for _ in range(t):
    simulation()

max_w = max(w)
cnt = sum(row.count(1) for row in grid)
print(cnt,max_w)