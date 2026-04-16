n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.


def heapify(arr,n,i):
    root = arr[i]
    left_idx = 2*i
    right_idx = 2*i+1

    if right_idx <= n:
        large_idx = left_idx if arr[left_idx] > arr[right_idx] else right_idx
        if root < arr[large_idx]:
            arr[i], arr[large_idx] = arr[large_idx], arr[i]
            heapify(arr,n,large_idx)
    elif left_idx <= n:
        if root < arr[left_idx]:
            arr[i], arr[left_idx] = arr[left_idx], arr[i]
            heapify(arr,n,left_idx)
    

        

def heap_sort(arr,n):
    last_idx = n;
    
    for i in range(last_idx//2,0,-1):
        heapify(arr,last_idx,i)
    
    for _ in range(n+!):
        arr[1], arr[last_idx] = arr[last_idx], arr[1]
        last_idx -=1
        heapify(arr,last_idx,1)

heap_sort(arr,n)

for i in range(1,n+1):
    print(arr[i],end=" ")

