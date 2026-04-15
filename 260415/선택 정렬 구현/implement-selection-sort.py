n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


for i in range(n):
    min = 101
    for j in range(i,n):
        if arr[j] < min:
            min_index = j
            min = arr[j]
    tmp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = tmp
    print(arr[i],end=" ")

    
    
