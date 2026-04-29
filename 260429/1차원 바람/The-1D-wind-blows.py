n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.

def can_diffusion(arr1,arr2):
    for i in range(m):
        if arr1[i]==arr2[i]:
            return 1
    return 0
    
def shift_by_wind(row, dir):
    if dir == "L":
        temp = a[row].pop()
        a[row].insert(0,temp)
    else:
        temp = a[row].pop(0)
        a[row].append(temp)
    # print(row,dir)

def diffusion(row,dir):
    new_dir = dir
    for i in range(row, 0, -1):
        if i-1 < 0:
            break

        if can_diffusion(a[i],a[i-1]):
            if new_dir == "L":
                new_dir = "R"
            else: 
                new_dir="L"
            shift_by_wind(i-1,new_dir)
                
        else:
            break
            
    new_dir = dir
    for i in range(row, n):
        if i+1 > n-1:
            break
        if can_diffusion(a[i],a[i+1]):
            if new_dir == "L":
                new_dir = "R"
            else: 
                new_dir="L"

            shift_by_wind(i+1,new_dir)
                
        else: break
            
                
for row,dir in winds:
    shift_by_wind(row-1,dir)
    diffusion(row-1,dir)

for e in a:
    for i in range(m):
        print(e[i],end= " ")
    print()
