n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def shift_by_wind(row, dir):
    if dir == "L":
        temp = a[row-1].pop()
        a[3].insert(0,temp)
    else:
        temp = a[row-1].pop(0)
        a[3].append(temp)

shift_by_wind(3,"L")

print(a)