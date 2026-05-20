N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

dp = [10001]* (M+1)

dp[0] = 0

coin.sort(reverse=True)



for i in range(1,M+1):
    # if dp[i] != -1:
    #     continue
    
    for v in coin:
        if v > i:
            continue
        # elif v==i:
        #     dp[i] = 1
        #     continue

        dp[i] = min(dp[i],dp[i-v] + 1)

# print(dp)
if dp[M]== 10001:
    dp[M] = -1
print(dp[M])