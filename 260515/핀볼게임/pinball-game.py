n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 공 방향기준 맞았을때 바뀌는 이동방향

reflect_dir_1 = [3,2,1,0]
reflect_dir_2 = [2,3,0,1]

# 공 진행방향, 위로 :0, 밑으로:1, 좌로:2, 우로:3
current_dir = 1
fall_dx = [-1,1,0,0]
fall_dy = [0,0,-1,1]


def fall(x,y,dir):
    T=1
    nx, ny = x,y
    while 1: 
        if grid[nx][ny] == 1:
            dir = reflect_dir_1[dir]
            # print(1)
        elif grid[nx][ny] == 2:
            dir = reflect_dir_2[dir]
            # print(2)
        
        if nx+fall_dx[dir] < 0 or nx+fall_dx[dir] > n-1 or\
            ny+fall_dy[dir] < 0 or ny+fall_dy[dir] > n-1:

            T+=1
            break

        nx += fall_dx[dir]
        ny += fall_dy[dir]
        T+=1
    
    return T


max_cnt= [0,0,0,0]

for i in range(n):
    if (res := fall(n-1,i,0)) > max_cnt[0]:
        max_cnt[0] = res
    
    if (res := fall(0,i,1)) > max_cnt[1]:
        max_cnt[1] = res
    
    if (res := fall(i,n-1,2)) > max_cnt[2]:
        max_cnt[2] = res

    if (res := fall(i,0,3)) > max_cnt[3]:
        max_cnt[3] = res

print(max(max_cnt))
