# find second largest elem in a list

import random
l = [random.randint(0, 10) for i in range(10)]
print(l)
# print(list(sorted(l))[-2])

def largest(l):
    # max(l)
    max_num = -99999999
    ix = -1
    for i in range(len(l)):
        if l[i] > max_num:
            max_num = l[i]
            break
    return max_num, i
    
def second_largest(l):
    largest_, ix = largest(l)
    #print("Lar)
    #l = l[:ix] + l[ix+1:]
    # pop, del, remove, list concat
    del l[ix]
    
    # print(l)
    slargest, sl_ix = largest(l)
    return slargest
    
print(second_largest(l))