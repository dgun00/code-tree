N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)
min = 10000000
for i in range(N-1):
    for j in range(i+1,N):
        if abs( S - (total - (arr[i]+arr[j]))) <= min:
            min = abs( S - (total - (arr[i]+arr[j])))

print(min)