n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

for _ in range(t):
    temp1, temp2, temp3 = l[n-1], r[n-1], d[n-1]

    for i in range(n-1,0,-1):
        l[i] = l[i-1] 
        r[i] = r[i-1]
        d[i] = d[i-1]
    l[0] = temp3
    r[0] = temp1
    d[0] = temp2

for e in l:
    print(e, end=" ")
print()

for e in r:
    print(e, end=" ")
print()

for e in d:
    print(e, end=" ")
