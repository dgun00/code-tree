N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Node:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class doblelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            if self.tail == None:
                self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.num = self.num + 1
    
    def push_back(self, new_data):
        new_node = Node(new_data)

        if self.tail == None:
            self.tail = new_node
            if self.head == None:
                self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.num = self.num + 1

    def pop_front(self):
        if self.head == None:
            print("pop err")
        elif self.head.next == None:
            poped = self.head.data
            self.head = None
            self.tail = None
            self.num = self.num - 1
            print(poped)

        else:
            poped = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.num = self.num - 1
        
            print(poped)
    
    def pop_back(self):
        if self.tail == None:
            print("pop err")
        elif self.tail.prev == None:
            poped = self.tail.data
            self.head = None
            self.tail = None
            self.num = self.num - 1
           
            print(poped)
        else:
            poped = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.num = self.num - 1

            print(poped)

    def size(self):
        print(self.num)

    def empty(self):
        if self.num == 0:
            print(1)
        else :
            print(0)

    def front(self):
        if self.head != None:
            print(self.head.data)
    
    def back(self):
        if self.tail != None:
            print(self.tail.data)


dli = doblelinkedlist()

for i in range(N):
    if command[i] == "push_front":
        dli.push_front(A[i])
    elif command[i] == "push_back":
        dli.push_back(A[i])
    elif command[i] == "pop_front":
        dli.pop_front()
    elif command[i] == "pop_back":
        dli.pop_back()
    elif command[i] == "size":
        dli.size()
    elif command[i] == "empty":
        dli.empty()
    elif command[i] == "front":
        dli.front()
    elif command[i] == "back":
        dli.back()