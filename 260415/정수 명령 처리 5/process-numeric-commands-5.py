N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.

ary = []

for i in range(N):
    if command[i] == "push_back":
        ary.append(num[i])
    elif command[i] == "get" and num[i]-1 <= len(ary):
        print(ary[num[i]-1])
    elif command[i] == "size":
        print(len(ary))
    elif command[i] == "pop_back":
        ary.pop()
