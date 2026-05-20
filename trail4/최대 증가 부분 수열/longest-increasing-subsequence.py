import sys
n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

dp = [1]*n

# dp[0] = 1

max_val = 1

for i in range(1,n):
        for j in range(i-1,-1,-1):
                if m[j] < m[i]:
                        dp[i] = max(dp[i], dp[j]+1)
        
        # dp[i] = max_val
        # max_val = 1

print(max(dp))


