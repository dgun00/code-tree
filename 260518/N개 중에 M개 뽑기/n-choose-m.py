N, M = map(int, input().split())

# Please write your code here.
arr = []


def choose(cnt,num):
    if cnt == M:
        for e in arr:
            print(e,end=" ")
        print()
        return

    for i in range(num+1,N+1):
        if num < i:
            arr.append(i)
            choose(cnt+1,i)
            arr.pop()
choose(0,0)