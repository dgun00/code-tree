n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dx = [0,-1,-1,0,1,1,1, 0,-1]
dy = [0, 0, 1,1,1,0,-1,-1,-1]

def is_in_range(x,y):
    if x >=0 and x < n and y>=0 and y<n:
        return 1
    else:
        return 0


cnt = 0
max_cnt = 0

def find_path(r,c):
    global max_cnt
    global cnt
    dir = move_dir[r-1][c-1]

    for i in range(1,n):
        if is_in_range(r-1+dx[dir]*i,c-1+dy[dir]*i): 
            if num[r-1][c-1] <= num[r-1+dx[dir]*i][c-1+dy[dir]*i]:
                cnt+=1
                # print(num[r-1+dx[dir]*i][c-1+dy[dir]*i])
                # print("cnt:",cnt)
                find_path(r+dx[dir]*i,c+dy[dir]*i)
                cnt-=1
            else:
                # print(cnt,"!")
                # print(num[r-1+dx[dir]*i][c-1+dy[dir]*i])
                # print()
                max_cnt = max(cnt,max_cnt)
        else:
            # print("out of range")
            # print()
            # print(cnt,"!")
            # print()
            max_cnt = max(cnt,max_cnt)
            return 

find_path(r,c)
print(max_cnt)