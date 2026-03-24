x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

COLS = 2000
ROWS = 2000
OFFSET = 1000

def add_offset(x1,y1,x2,y2):
    for i in range(2):
        x1[i] += OFFSET
        y1[i] += OFFSET
        x2[i] += OFFSET
        y2[i] += OFFSET

def fill_matrix(x1,y1,x2,y2):
    for idx in range(2):
        for j in range(y1[idx],y2[idx]):
            for i in range(x1[idx],x2[idx]):
                if idx == 0:
                    matrix[j][i] = 1
                else:
                    matrix[j][i] = 2
    
def res_func():
    min_x, max_x, min_y, max_y = ROWS, 0 , COLS, 0
    exist = False
    for x in range(ROWS):
        for y in range(COLS):
            if matrix[y][x] == 1:
                exist = True
                min_x = min(min_x,x)
                max_x = max(max_x,x)
                min_y = min(min_y,y)
                max_y = max(max_y,y)

    if not exist:
        res = 0
    else: 
        res = (max_x - min_x+1) * (max_y - min_y +1)

    return res

matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

add_offset(x1,y1,x2,y2)
fill_matrix(x1,y1,x2,y2)
print(res_func())
