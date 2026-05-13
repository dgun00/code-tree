A = input()

# Please write your code here.



def run_length_encoding(arr):

    char_arr = []
    cnt_arr = []
    prev_e = arr[0]
    idx_cnt = 0

    for i in range(len(arr)):
        if len(char_arr) == 0:
            char_arr.append(arr[i]) 
            cnt_arr.append(1)

        if prev_e != arr[i]:
            idx_cnt +=1
            char_arr.append(arr[i])
            cnt_arr.append(1)
            prev_e = arr[i]
        else:
            cnt_arr[idx_cnt]+=1
        
    res = len(char_arr)*2
    for e in cnt_arr:
        if e >= 10:
            res +=1
    return res

def shift(arr):
    new_arr = list(arr)
    
    poped = new_arr.pop()
    new_arr.insert(0,poped)

    new_arr = ''.join(new_arr)
   
    return new_arr

def find_min_res(arr):

    min_cnt = 30
    next_arr = arr

    for _ in range(len(arr)):
        cur_cnt = run_length_encoding(next_arr)
        if cur_cnt < min_cnt:
            min_cnt = cur_cnt
        
        next_arr = shift(next_arr)
    
    return min_cnt

print(find_min_res(A))

        



        
        
