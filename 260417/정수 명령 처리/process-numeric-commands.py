N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class stack:
    def __init__(self):
        self.stk = []

    def push(self, e):
        self.stk.append(e)
    
    def pop(self):
        poped =self.stk.pop()
        return poped

    def size(self):
        return len(self.stk)

    def empty(self):
        if self.size() == 0:
            return 1
        else: return 0

    def top(self):
        return self.stk[self.size()-1]

stk = stack()

for i in range(N):
    if command[i] == "push":
        stk.push(value[i])
    elif command[i] == "pop":
        print(stk.pop())
    elif command[i] == "size":
        print(stk.size())
    elif command[i] == "empty":
        print(stk.empty())
    elif command[i] == "top":
        print(stk.top())