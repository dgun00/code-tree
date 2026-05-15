N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.
# 오른쪽, 아래쪽, 왼쪽, 위쪽 순

visited = [[[0] * 4 for _ in range(N + 1)] for _ in range(N + 1)]

front_check_dx = [0,1,0,-1]
front_check_dy = [1,0,-1,0]

right_check_dx = [1,0, -1,0] 
right_check_dy = [0,-1,0,1]

current_dir_num = 0
current_x = x
current_y = y


T = 0

def is_right_block(x,y):
    global current_dir_num

    # 오른쪽이 격자밖이 아닐때
    if x+right_check_dx[current_dir_num] >=1 and x+right_check_dx[current_dir_num] <= N and\
        y+right_check_dy[current_dir_num] >=1 and y+right_check_dy[current_dir_num] <= N:

        # 오른쪽이 벽이면
        if grid[x+right_check_dx[current_dir_num]][y+right_check_dy[current_dir_num]] == '#':
            return 1
        else:
            return 0
    else:
        return 0


def is_front_block(x,y):
    global current_dir_num
    # for i in range(4):
    #     circular_num = (current_dir_num + i) % 4
        # 진행 방향 앞이 격자 밖이 아닐때
    if x+front_check_dx[current_dir_num] >= 1 and x+front_check_dx[current_dir_num] <= N and \
        y+front_check_dy[current_dir_num] >= 1 and y+front_check_dy[current_dir_num] <= N:

        # 앞이 벽이면
        # if grid[x+front_check_dx[circular_num]][y+front_check_dy[circular_num]] == '#':
        #     circular_num = (circular_num - 1) % 4 # 반시계 회전

        # 앞이 벽이면
        if grid[x+front_check_dx[current_dir_num]][y+front_check_dy[current_dir_num]] == '#':
            return 1

        else: # 앞이 벽이아니면
            return 0
    else:
        return 0     
        



while 1:
    if visited[current_x][current_y][current_dir_num] == 1:
        print(-1)
        break

    visited[current_x][current_y][current_dir_num] = 1

    if is_front_block(current_x,current_y) == 1 and is_right_block(current_x,current_y) == 1:
        #print("반시계 회전")
        current_dir_num = (current_dir_num - 1) % 4 # 반시계 회전
    elif is_front_block(current_x,current_y) != 1 and is_right_block(current_x,current_y) ==1:
        # 앞이 격자 밖일때 종료
        if current_x+front_check_dx[current_dir_num] < 1 or current_x+front_check_dx[current_dir_num] > N or \
            current_y+front_check_dy[current_dir_num] < 1 or current_y+front_check_dy[current_dir_num] > N:
            T+=1
            print(T)
            break
        else: # 앞이 격자 안이면 전진
            current_x = current_x + front_check_dx[current_dir_num]
            current_y = current_y + front_check_dy[current_dir_num]
            T+=1
            # if visited[current_x][current_y] == 1:
            #     print(-1)
            #     break

    elif is_right_block(current_x,current_y) != 1:# 오른쪽이 없을떄
        current_dir_num = (current_dir_num + 1) % 4 # 시계 회전
        #print("시계 회전")
        current_x = current_x + front_check_dx[current_dir_num]
        current_y = current_y + front_check_dy[current_dir_num]
        T+=1
        # if visited[current_x][current_y] == 1:
        #     print(-1)
        #     break
        



