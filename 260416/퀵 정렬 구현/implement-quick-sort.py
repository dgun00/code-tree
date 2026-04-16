n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    j = low

    while j <= high:
        if arr[j] < pivot:
            tmp = arr[i+1]
            arr[i+1] = arr[j]
            arr[j] = tmp
            i+=1
        j+=1
        
    tmp = arr[i+1]
    arr[i+1] = pivot
    arr[high] = tmp 

    return i+1

def quick_sort(arr,low,high):
    if low < high:
        pos = partition(arr,low,high)
    
        quick_sort(arr,low,pos-1)
        quick_sort(arr,pos+1,high)



quick_sort(arr,0,n-1)

for e in arr:
    print(e, end=" ")
            
