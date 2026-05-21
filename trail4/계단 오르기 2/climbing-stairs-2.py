import sys

n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
MIN_SIZE = -sys.maxsize

dp = [[MIN_SIZE]*(n+1) for _ in range(4)]

for i in range(4):
    dp[i][0] = 0

# dp[0][1] = -1
dp[1][1] = coin[1]
# dp[2][1] = -1
# dp[3][1] = -1


# print(dp)
for i in range(2,n+1):
    for j in range(4):
        
        # if j == 0 and dp[0][i-2] != MIN_SIZE:
            
        #     dp[j][i] = dp[0][i-2] + coin[i]

        # elif j!=0:
        #     dp[j][i] = max(dp[j-1][i-1] + coin[i], dp[j][i-2]+coin[i])

        # i-2에서 i로 오는 경우
        if dp[j][i-2] != MIN_SIZE:
            dp[j][i] = max(dp[j][i], dp[j][i-2] + coin[i])

        # i-1에서 i로 오는 경우
        if j > 0 and dp[j-1][i-1] != MIN_SIZE:
            dp[j][i] = max(dp[j][i], dp[j-1][i-1] + coin[i])

# print(dp)
res = []


for e in dp:
    res.append(e[n])

print(max(res))
