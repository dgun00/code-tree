N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.

max_cnt = -1
for i in range(N):
    costs = []

    for j in range(N):
        if i==j:
            costs.append(P[j]/2+S[j])
        else:
            costs.append(P[j]+S[j])

    costs.sort()
    total = 0
    cnt=0
    for e in costs:
        total += e
        cnt+=1
        if total > B:
            cnt-=1
            break
        

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)




