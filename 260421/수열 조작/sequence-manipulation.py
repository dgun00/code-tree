n = int(input())

# Please write your code here.
from collections import deque

dq = deque()

for i in range(1,n+1):
    dq.append(i)

while 1:
    if len(dq) == 1:
        print(dq[0])
        break;
    dq.popleft() 
    dq.append(dq.popleft())

