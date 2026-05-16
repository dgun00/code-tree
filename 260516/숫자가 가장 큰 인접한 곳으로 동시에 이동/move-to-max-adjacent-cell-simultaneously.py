n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = [[0]*n for _ in range(n)]
next_count = [[0]*n for _ in range(n)]

def move(x,y):
    global count
    global next_count
    max_num = 0
    tmp_x,tmp_y =x,y
    for i in range(4):
        if x+dx[i] >=0 and x+dx[i]<n and y+dy[i] >=0 and y+dy[i]<n:
            if a[x+dx[i]][y+dy[i]] > max_num:
                max_num = a[x+dx[i]][y+dy[i]]
                tmp_x, tmp_y = x+dx[i], y+dy[i]
            
    next_count[tmp_x][tmp_y] += 1
    count = [row[:] for row in next_count]
    # print(count)
    return 1

def set_marble_pos():
    global marbles
    global r
    global c

    temp_marbles = []

    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                temp_marbles.append((i+1,j+1))
            
            elif count[i][j] > 1:
                count[i][j] = 0

    marbles = temp_marbles
    r = [pos[0] for pos in marbles]
    c = [pos[1] for pos in marbles]

    return 1



def is_marble(x,y):
    for k in range(len(marbles)):
        if r[k] -1 ==x and c[k]-1 ==j:
            return 1
    return 0



for _ in range(t):
    for i in range(n):
        for j in range(n):
            if is_marble(i,j):
                move(i,j) # k는 구슬 위치 인덱스

    set_marble_pos()
    next_count = [[0]*n for _ in range(n)]



res= sum(row.count(1) for row in count)


print(res)
        
