N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)
min = 1000000
for i in range(N):
    for j in range(i+1,N):
        if abs(total - (arr[i]+arr[j])) <= min:
            min = abs(total - (arr[i]+arr[j]))

print(min-S)