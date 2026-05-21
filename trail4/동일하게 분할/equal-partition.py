n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)

if total%2 ==1:
    print("No")
    exit()

dp_size = total//2

dp = [False]*(dp_size+1)
dp[0] = True

for i in range(n):
    for j in range(dp_size,arr[i]-1,-1):
        if dp[j-arr[i]]:
            dp[j] = True 

if dp[dp_size]==True:
    print("Yes")
else:
    print("No")
