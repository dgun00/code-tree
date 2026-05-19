n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


# print(edges)

lists = [[] for _ in range(n+1)] 

visited = [0]*(n+1)

cnt = 0 
def make_lists():
    for s,e in edges:
        lists[s].append(e)
        lists[e].append(s)



def dfs(vertex):
    global cnt
    visited[vertex] = 1
    for curr_v in lists[vertex]:
        if not visited[curr_v]:
            cnt+=1
            visited[curr_v] = 1
            dfs(curr_v)


make_lists()
dfs(1)
# print(lists)
print(cnt)