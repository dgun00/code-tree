n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque

dq = deque()

for i in range(n):
    if cmd[i] == "push_front":
        dq.appendleft(num[i])
    elif cmd[i] == "push_back":
        dq.append(num[i])
    elif cmd[i] == "pop_front":
        if dq:
            print(dq.popleft())
            
    elif cmd[i] == "pop_back":
        if dq:
            print(dq.pop())
    elif cmd[i] == "size":
        print(len(dq))
    elif cmd[i] == "empty":
        if dq :
            print(0)
        else: print(1)
    elif cmd[i] == "front":
        print(dq[0])

    elif cmd[i] == "back":
        print(dq[-1])

