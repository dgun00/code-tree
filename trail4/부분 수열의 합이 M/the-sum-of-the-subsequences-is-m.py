n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
MAX_SIZE = 10001

dp = [MAX_SIZE]*(m+1)


dp[0] = 0

for i in range(n):
    for j in range(m,-1,-1):
        if j >= A[i]:
            dp[j] = min(dp[j],dp[j-A[i]]+1)




if dp[m] == MAX_SIZE:
    dp[m] = -1

print(dp[m])