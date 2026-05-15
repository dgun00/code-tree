n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

GRID_SIZE = n

def boom(x,y,boom_range,grid):

    original_grid = [row[:] for row in grid]

    for i in range(boom_range):
        if x-i >= 0:
            original_grid[x-i][y] = 0
        if y-i >= 0:
            original_grid[x][y-i] = 0
        if x+i < GRID_SIZE:
            original_grid[x+i][y] = 0
        if y+i < GRID_SIZE:
            original_grid[x][y+i] = 0

    boomed_grid = gravity_work(original_grid)

    return boomed_grid

def gravity_work(grid):
    temp_grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

    temp_grid_idx = 0

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,-1,-1):
            if grid[j][i] != 0:
                temp_grid[i][temp_grid_idx] = grid[j][i]
                temp_grid_idx +=1
        temp_grid_idx = 0


    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j] = temp_grid[j][GRID_SIZE-1-i]

    return grid

def find_couple_cnt(grid):
    cnt =0

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0 and j+1 < GRID_SIZE:
                if grid[i][j] == grid[i][j+1]: 
                    cnt +=1
            
            if grid[i][j] !=0 and i+1 <GRID_SIZE:
                if grid[i][j] == grid[i+1][j]:
                    cnt +=1

    return cnt

max_cnt = -1
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        boomed_grid = boom(i,j,grid[i][j],grid)
        cnt = find_couple_cnt(boomed_grid)
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)

