n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def get_res():
    max_val = -1
    for i in range(n):
        for j in range(m):
            val = get_rect_size(i,j)
            if val > max_val:
                max_val = val
    return max_val

def get_rect_size(st_i,st_j):
    max_j = m-1
    max_rect_size = -1
    for i in range(st_i,n):
        for j in range(st_j,m):
            if grid[i][j] <= 0:
                temp_j = j-1
                if max_j > temp_j:
                    max_j = temp_j
                continue
            elif j <= max_j:
                rect_size = (i - st_i +1) * (j - st_j +1)
                if max_rect_size < rect_size:
                    max_rect_size = rect_size
    return max_rect_size

print(get_res())