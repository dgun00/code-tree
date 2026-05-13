n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.


def delete_blocks(a,b):

    global blocks

    temp_blocks = []

    idx_a, idx_b = a-1 , b-1
    for i in range(len(blocks)-1,-1,-1):
        if idx_a > i or idx_b < i:

            temp_blocks.append(blocks[i])

    blocks = temp_blocks[::-1]

    return 1

delete_blocks(s1,e1)
delete_blocks(s2,e2)

print(len(blocks))
for e in blocks:
    print(e)