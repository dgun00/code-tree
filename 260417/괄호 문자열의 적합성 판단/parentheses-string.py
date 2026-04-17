str = input()

# Please write your code here.

class stack:
    def __init__(self):
        self.stk = []
    
    def push(self,e):
        self.stk.append(e)

    def pop(self):
        poped = self.stk.pop()
        return poped

    def empty(self):
        if len(self.stk) == 0:
            return 1
        else: return 0
    
    def top(self):
        return self.stk(len(self.stk)-1)

stk = stack()

def f(stk, str):
    
    for e in str:
        if e == '(':
            stk.push(e)
        
        if e == ')':
            if stk.empty():
                return "No";
            
            else: stk.pop()

    if stk.empty():
        return "Yes"
    else:
        return "No"


print(f(stk,str))