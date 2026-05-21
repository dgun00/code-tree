n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

dp = [-1001]*(n)

dp[0] = arr[0]

st_idx = 0
for i in range(1,n):
    # if dp[i-1]+arr[i] > arr[i]*2:
    #     dp[i] = dp[i-1]+arr[i]

        
    # else:
    #     dp[i] = 2*arr[i]
    #     st_idx = i

    dp[i] = max(dp[i-1]+arr[i],arr[i])

print(max(dp))

