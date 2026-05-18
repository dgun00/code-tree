import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

res_arr = []
arr = []
visit_col = []


def fill_grid(curr_cnt):
    global min_res

    if curr_cnt == n:
        res_arr.append(min(arr))
        return

    for i in range(n):
        if i in visit_col:
            continue

        visit_col.append(i)
        arr.append(grid[i][curr_cnt])
        fill_grid(curr_cnt+1)

        arr.pop()
        visit_col.pop()

fill_grid(0)
print(max(res_arr))


