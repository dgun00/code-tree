n = int(input())

# Please write your code here.

visited = [0]*(n+1)
arr = []

def find(curr_n):
    if curr_n == n :
        for e in arr:
            print(e, end=" ")
        print()
        return
    
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        
        visited[i] = 1
        arr.append(i)
        find(curr_n+1)
        
        arr.pop()
        visited[i] = 0


find(0)
