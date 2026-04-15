n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


while(1):

    sorted = True

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            sorted = False
    
    if sorted == True:
        break;

for e in arr:
    print(e,end=" ")
