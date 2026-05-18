K, N = map(int, input().split())

# Please write your code here.

arr = []
cnt = 0
def find_arr(n):
    if N==n:
        for e in arr:
            print(e, end=" ")
        print()

        return

   
    
    for i in range(1,K+1):
        arr.append(i)
        if n >= 2:
            if arr[n] == arr[n-1] and arr[n-2]== arr[n-1] :
        
                arr.pop()
                continue
        find_arr(n+1)
        arr.pop()


find_arr(0)
