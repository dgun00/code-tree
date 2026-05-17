K, N = map(int, input().split())

# Please write your code here.

arr = []

def choose_num(n):
    if n == N:
        for i in range(N):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1,K+1):
        arr.append(i)
        choose_num(n+1)
        arr.pop()

choose_num(0)