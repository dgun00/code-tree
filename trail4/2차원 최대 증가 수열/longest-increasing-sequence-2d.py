n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[-1]*m for _ in range(n)]

# for i in range(1,m):
#     dp[0][i] = -1

# for j in range(1,n):
#     dp[j][0] = -1

dp[0][0] = 1


for i in range(1,n):
    for j in range(1,m):

        for k in range(i):
            for l in range(j):
                if dp[k][l] == -1:
                    continue
                if grid[i][j] > grid[k][l]:
                    dp[i][j] = max(dp[i][j],dp[k][l]+1)


# print(dp)

max_in_row = [
    max(row)
    for row in dp
]

print(max(max_in_row))





