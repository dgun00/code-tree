from collections import deque

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        poped = self.queue.popleft()
        print(poped)
    def size(self):
        print(len(self.queue))

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.empty() != 1:
            print(self.queue[0])

my_queue = Queue()


for i in range(N):
    if command[i] == "push":
        my_queue.push(A[i])

    elif command[i] == "front":
        my_queue.front()
    
    elif command[i] == "size":
        my_queue.size()

    elif command[i] == "empty":
        print(my_queue.empty())
    
    elif command[i] == "pop":
        my_queue.pop()
