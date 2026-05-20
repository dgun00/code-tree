n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.

jobs.sort()

dp = [0] * 1001

jobs_s_e = [[0,0] for _ in range(1001)]

idx = 1

for s,e,p in jobs:
    if e == jobs_s_e[idx-1][1]:
        idx-=1

    # print(p)

    dp[idx] = max(p,dp[idx]) 

    for i in range(idx):
        if jobs_s_e[i][1] < s:  
            dp[idx] = max(dp[idx], p+dp[i])

    # print(dp[idx])
    jobs_s_e[idx] = [s,e]

    idx+=1


print(max(dp))