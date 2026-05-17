n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
line_setting = [0]*n
max_line_cnt = -1

def is_gyeopchim(x1,x2,x3,x4):

    if x1 <= x3 and x2 >= x3:
        return 1
    elif x1 <= x4 and x2 >= x4:
        return 1
    else: 
        return 0

def current_gyeopchim():
    for i in range(n):
        if line_setting[i] == 1:
            for j in range(n):
                if i!=j and line_setting[j] == 1:
                    
                    if is_gyeopchim(x1[i],x2[i],x1[j],x2[j]):
                        # print(i,j)
                        return 1

    return 0


def set_line(idx):
    global max_line_cnt
    if idx == n:
        if  current_gyeopchim() == 0:
            cnt = sum(line_setting)
            if max_line_cnt < cnt:
                max_line_cnt = cnt 
        return
    
    line_setting[idx] = 1
    set_line(idx+1)
    line_setting[idx] = 0
    set_line(idx+1)


set_line(0)
print(max_line_cnt)