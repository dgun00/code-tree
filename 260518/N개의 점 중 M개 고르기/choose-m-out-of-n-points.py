import sys
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.



visited = [0]*n

dists = []

def find_min_dist():

    max_dist = -sys.maxsize

    selected_point = [points[i] for i in range(n) if visited[i] == 1 ]
    # print(selected_point)

    for i in range(m):
        for j in range(i+1,m):
            dist = (selected_point[i][0] - selected_point[j][0])*(selected_point[i][0] - selected_point[j][0])\
                + (selected_point[i][1] - selected_point[j][1])*(selected_point[i][1] - selected_point[j][1])
            max_dist = max(dist,max_dist)
    dists.append(max_dist)


def select_point(curr_num, cnt):
    if cnt == m:
        # print(visited)
        find_min_dist()
        return
    
    if curr_num == n:
        return

    visited[curr_num] = 1
    select_point(curr_num+1,cnt+1)
    visited[curr_num] = 0
    select_point(curr_num+1,cnt)

select_point(0,0)

print(min(dists))