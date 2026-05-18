N, M = map(int, input().split())

# Please write your code here.
arr = []


def choose(num,cnt):
    if num == N+1:
        if cnt == M:
            for e in arr:
                print(e,end=" ")
            print()
        return

    # for i in range(num+1,N+1):
    #     if num < i:
    #         arr.append(i)
    #         choose(cnt+1,i)
    #         arr.pop()
    arr.append(num)
    choose(num+1,cnt+1)
    arr.pop()

    choose(num+1,cnt)

choose(1,0)