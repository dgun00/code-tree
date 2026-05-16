T = int(input())

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dir_to_num(dir):
    if dir == "U":
        return 0
    elif dir == "D":
        return 1
    elif dir == "L":
        return 2
    else:
        return 3

def next_action(x,y,d,grid_size):
    temp_grid = [[0] * grid_size for _ in range(grid_size)]

    for idx in range(len(x)):

        dir_idx = dir_to_num(d[idx])
        # 진행 방향 앞이 격자 밖이 아닐때
        if x[idx]+dx[dir_idx]-1 >=0 and x[idx]+dx[dir_idx]-1 < grid_size and \
            y[idx]+dy[dir_idx]-1 >=0 and y[idx]+dy[dir_idx]-1 < grid_size:

            temp_grid[x[idx]+dx[dir_idx]-1][y[idx]+dy[dir_idx]-1] += 1
            x[idx] = x[idx]+dx[dir_idx]
            y[idx] = y[idx]+dy[dir_idx]
        else: # 진행방향 앞이 격자 밖일때
            if d[idx] == 'L':
                d[idx] = 'R'
            elif d[idx] == 'R':
                d[idx] = 'L'
            elif d[idx] == 'U':
                d[idx] = 'D'
            elif d[idx] == 'D':
                d[idx] = 'U'

            temp_grid[x[idx]-1][y[idx]-1] += 1

    
    return temp_grid

def collpse(x,y,d,grid):

   
    temp_x = []
    temp_y = []
    temp_d = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 1:
                for k in range(len(x)):
                    if x[k]-1 == i and y[k]-1 == j:
                        x[k] = -1
                        y[k] = -1
                        d[k] = -1
                grid[i][j] = 0
                
    

    for idx in range(len(x)):
        if x[idx] == -1:
            pass
        else:
            temp_x.append(x[idx])
            temp_y.append(y[idx])
            temp_d.append(d[idx])
    x[:] = temp_x[:]
    y[:] = temp_y[:]
    d[:] = temp_d[:]

def simulation(x,y,d,grid_size):
    for i in range(2*grid_size):
        res_grid = next_action(x,y,d,grid_size)
        collpse(x,y,d,res_grid)
        # print(x,y,d)
        # print(res_grid)

    return res_grid


for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    grid = [[0]*N for _ in range(N)]
    
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)

    # Please write your code here.
  
    grid = simulation(x,y,d,N)

    cnt = sum(row.count(1) for row in grid)
    print(cnt)




    


