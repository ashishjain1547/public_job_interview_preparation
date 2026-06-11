# fibonacci
# upto a number - coming as an input
# use recursion

# l = [0, 1, 1, 2, 3]


def fib(in_num):
    fib_in_num = 0
    if in_num > 1:
        fib_in_num = fib(in_num - 1) + fib(in_num - 2)
    elif in_num == 0:
        fib_in_num = 0
    elif in_num == 1:
        fib_in_num = 1
        
    return fib_in_num
    
in_num = 0
out = [fib(i) for i in range(in_num)]

print(out)
    
# TEST (1): 5
# TEST (2): 0 (Edge)