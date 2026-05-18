n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = []
visited_i = []


max_res = -1
def can_choose(x):
    if x in visited_i:
        return 0

    return 1

def choose_point(curr_n):
    global max_res

    if curr_n == n:
        res = sum(arr)
        # print(arr)
        max_res = max(max_res,res)
        return

    for i in range(n):
            
        if can_choose(i) == 0:
            continue

        visited_i.append(i)

        arr.append(grid[i][curr_n])
        choose_point(curr_n+1)

        visited_i.pop()

        arr.pop()

choose_point(0)
print(max_res)