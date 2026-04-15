n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please write your code here.
class Node:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0
    
    def push_front(self,new_data):
        new_node = Node(new_data)
        
        if self.num == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.num += 1

    def insert(self,it_node,new_data):
        new_node = Node(new_data)

        new_node.next = it_node.next
        it_node.next.prev = new_node
        it_node.next = new_node
        new_node.prev = it_node



    def erase(self, node):
        if node == None:
            return print("None node")
            
        elif node == self.head:
            self.head.next.prev = None
            self.head = self.head.next

        elif node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.num -=1



dlist = dll()


for i in s[::-1]:
    dlist.push_front(i)


dlist.push_front(-1) # dummy node

it = dlist.tail

for cmd in commands:
    
    if cmd[0] == "L" and it != dlist.head:
        it = it.prev

    elif cmd[0] == "R" and it != dlist.tail:
        it = it.next

    elif cmd[0] == "D":
        dlist.erase(it.next)
    
    elif cmd[0] == "P":
        dlist.insert(it, cmd[1])
        it = it.next
    




node = dlist.head.next
while node != None:
    print(node.data,end="")
    node = node.next



        

            

