n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

def dir_selection(x,y):

    priority_x, priority_y = 0, 0

    while 1:
        flag = 0 
        print(a[x][y],end=" ")
        
        for i in range(4):
            if x+dx[i] >=0 and x+dx[i] <= n and y+dy[i] >=0 and y+dy[i] <=n:
                if a[x+dx[i]][y+dy[i]] > a[x][y]:
                    priority_x = x+dx[i]
                    priority_y = y+dy[i]
                    flag = 1
                    break

        
        if flag == 0:
            break
        else:
            x = priority_x
            y = priority_y

    return 1
        

dir_selection(r,c)

