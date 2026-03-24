x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
def fill_rect(x1,y1,x2,y2):
    for i in range(x1,x2):
        for j in range(y1,y2):
            matrix[j][i] = matrix[j][i] + 1
         

COLS = 1000
ROWS = 1000
width = 0
gyeopchim = 0
matrix = [[0 for _ in range(COLS)]for _ in range(ROWS)]


for i in range(2):
    fill_rect(x1[i],y1[i],x2[i],y2[i])

for j in range(COLS):
    for i in range(ROWS):
        if  matrix[j][i] == 1:
            width = width + 1
# ---- A,B 넓이 -----

fill_rect(x1[2],y1[2],x2[2],y2[2])

for j in range(COLS):
    for i in range(ROWS):
        if  matrix[j][i] == 2:
            gyeopchim = gyeopchim + 1
        
print(width-gyeopchim)    

