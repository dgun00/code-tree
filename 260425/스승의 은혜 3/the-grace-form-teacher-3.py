N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
arr = []
total =0
sorted = sorted(gifts, key=lambda x: x[0]/2 + x[1])

for p,s in gifts:
    total += p + s

idx = N-1
while 1:
    if (total - (sorted[idx][0]/2 + sorted[idx][1])) > B:
        total = (total - (sorted[idx][0] + sorted[idx][1]))
        idx -= 1
    else: break
res = idx+1

print(res)
