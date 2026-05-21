import sys

INT_MIN = -sys.maxsize
    
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
s = [
    0
    for _ in range(n + 1)
]
e = [
    0
    for _ in range(n + 1)
]
v = [
    0
    for _ in range(n + 1)
]

for i in range(0, n):
    s[i], e[i], v[i] = tuple(map(int, input().split()))




dp = [
    [INT_MIN for _ in range(n)]
    for _ in range(m + 1)
]

def can_wear(n,s,e):
    if s <= n and e >= n:
        return 1
    return 0


for i in range(n):
    if can_wear(1,s[i],e[i]):
        dp[1][i] = 0





# print(dp)
for i in range(2, m + 1):

    for j in range(n):
        for k in range(n):
           if can_wear(i,s[k],e[k]) and can_wear(i-1,s[j],e[j]):
            dp[i][k] = max(dp[i][k], dp[i-1][j] + abs(v[j]-v[k]))


maxs=[]  
    
for row in dp:
    maxs.append(max(row))

print(max(maxs))
# ans = max(dp[m][1:n + 1])

# print(ans)
