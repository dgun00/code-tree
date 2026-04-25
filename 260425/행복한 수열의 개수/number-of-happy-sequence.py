n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

cnt = 0


def is_happy_arr(arr,m):
    stnd_el = arr[0]
    same_cnt = 0
    for e in arr:
        if stnd_el == e:
            same_cnt +=1
        else:
            stnd_el = e
            same_cnt = 1
          
        if same_cnt == m:
            return 1
    return 0



for j in range(n):
    row_temp_arr = []
    col_temp_arr = []
    for i in range(n):
        col_temp_arr.append(grid[i][j])
        row_temp_arr.append(grid[j][i])
    if is_happy_arr(row_temp_arr,m):
        cnt += 1
    if is_happy_arr(col_temp_arr,m):
        cnt += 1

print(cnt)