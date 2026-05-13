# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.

GRID_SIZE = 4

def left_union():
    global grid

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j+1] = 0
                grid[i][j] = grid[i][j]*2
                left_move_one_col(i)

        
    return 1
def left_move_one_col(col):
    global grid
    temp_arr = [0]*GRID_SIZE

    cnt = 0
    for i in range(GRID_SIZE):
        if grid[col][i] != 0:
            temp_arr[cnt] = grid[col][i]
            cnt+=1
    
    grid[col] = temp_arr

    return 1
def left_swipe():

    global grid

    temp_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    cnt = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                temp_grid[i][cnt] = grid[i][j]
                cnt+=1
        cnt=0
   
    grid = temp_grid
    left_union()
    return 1



def right_move_one_col(col):
    global grid
    temp_arr = [0]*GRID_SIZE

    cnt = 0
    for i in range(GRID_SIZE-1,-1,-1):
        if grid[col][i] != 0:
            temp_arr[cnt] = grid[col][i]
            cnt+=1
    
    grid[col] = temp_arr[::-1]
    return 1
def right_union():
    global grid

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,0,-1):
            if grid[i][j] == grid[i][j-1]:
                grid[i][j-1] = 0
                grid[i][j] = grid[i][j]*2
                right_move_one_col(i)

        
    return 1
def right_swipe():

    global grid

    temp_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    cnt = 3
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,-1,-1):
            if grid[i][j] != 0:
                temp_grid[i][cnt] = grid[i][j]
                cnt-=1
        cnt=3
   
    grid = temp_grid
    right_union()
    return 1

def up_union():
    global grid

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1):
            if grid[j][i] == grid[j+1][i]:
                grid[j+1][i] = 0
                grid[j][i] = grid[j][i]*2
                up_move_one_row(i)

        
    return 1
def up_move_one_row(row):
    global grid
    temp_arr = [0]*GRID_SIZE

    cnt = 0
    for i in range(GRID_SIZE):
        if grid[i][row] != 0:
            temp_arr[cnt] = grid[i][row]
            cnt+=1
    
    for i in range(GRID_SIZE):
        grid[i][row] = temp_arr[i]

    return 1
def up_swipe():

    global grid

    temp_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    cnt = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[j][i] != 0:
                temp_grid[i][cnt] = grid[j][i]
                cnt+=1
        cnt=0
   
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[j][i]= temp_grid[i][j]

    up_union()
    return 1



def down_union():
    global grid

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,0,-1):
            if grid[j][i] == grid[j-1][i]:
                grid[j-1][i] = 0
                grid[j][i] = grid[j][i]*2
                down_move_one_row(i)

        
    return 1

def down_move_one_row(row):
    global grid
    temp_arr = [0]*GRID_SIZE

    cnt = 0
    for i in range(GRID_SIZE-1,-1,-1):
        if grid[i][row] != 0:
            temp_arr[cnt] = grid[i][row]
            cnt+= 1
    
    k =0 
    for i in range(GRID_SIZE-1,-1,-1):
        grid[i][row] = temp_arr[k]
        k+=1

    return 1

def down_swipe():

    global grid

    temp_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    cnt = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,-1,-1):
            if grid[j][i] != 0:
                temp_grid[i][cnt] = grid[j][i]
                cnt+=1
        cnt=0
   
    k = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1,-1,-1):
            grid[j][i] = temp_grid[i][k]
            k+=1
        k=0

    down_union()
    return 1

if dir=='U':
    up_swipe()
elif dir=='D':
    down_swipe()
elif dir=='R':
    right_swipe()
else:
    left_swipe()

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        print(grid[i][j], end=' ')
    print()