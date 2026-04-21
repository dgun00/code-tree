from collections import deque

n, k = map(int, input().split())

# Please write your code here.

dq = deque()
res = ""
for i in range(1,n+1):
    dq.append(i)

while len(dq) > 0:
    for _ in range(k-1):
        dq.append(dq.popleft())
    poped = dq.popleft()
    res = res + str(poped) +" "

print(res)