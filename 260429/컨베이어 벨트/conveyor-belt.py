n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

new_u = [0]*n
new_d = [0]*n
# Please write your code here.
for _ in range(t):
    for i in range(n-1):
        new_u[i+1] = u[i]
        new_d[i+1] = d[i]
    new_u[0] = d[n-1]
    new_d[0] = u[n-1]
    u = list(new_u)
    d = list(new_d)

for e in u:
    print(e,end=" ")
print()
for e in d:
    print(e,end=" ")