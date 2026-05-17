expression = input()

# Please write your code here.

expression = list(expression)

my_alpha =  [ e for e in expression if e.isalpha() ]
# my_expression = [e for e in expression if e.isalpha() != 1]

# print(my_alpha,my_expression)

no_dup_alpha = list(set(my_alpha))
N = len(no_dup_alpha)

alpha_num_couple = [[al,-1] for al in no_dup_alpha]

# print(no_dup_alpha)
# print(alpha_num_couple)

max_res = -1

def alpha_to_num_expression():
    temp_expression = expression[:]
    for al,num in alpha_num_couple:
        for i in range(len(temp_expression)):
            if al == temp_expression[i]:
                temp_expression[i] = num
    
    return temp_expression

def calculate(expression):
    res = expression[0]
    for i in range(1, len(expression),2):
        if expression[i] == "-":
            res = res - expression[i+1]
        elif expression[i] == "+":
            res = res + expression[i+1]
        elif expression[i] == "*":
            res = res * expression[i+1]
    return res

def find_max(n):
    global max_res
    if N == n:
        # print(alpha_to_num_expression())
        # print(calculate(alpha_to_num_expression()))
        current_res = calculate(alpha_to_num_expression())
        max_res = max(max_res,current_res)
        return

    alpha_num_couple[n][1] = 1
    find_max(n+1)
    alpha_num_couple[n][1] = 2
    find_max(n+1)
    alpha_num_couple[n][1] = 3
    find_max(n+1)
    alpha_num_couple[n][1] = 4
    find_max(n+1)
    

find_max(0)
print(max_res)