N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

# print(w,v)
MIN_SIZE = -1

dp = [0]*(M+1)

dp[0] = 0

for i in range(N):

    for j in range(M,-1,-1):
        if j - w[i] >= 0:
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])


print(max(dp))
