l1 = list(range(0,9))
k = 9

# pick any two random from l1. if a+b == k, return a,b. return all such pairs -- reverse of the pair should not be returned

from itertools import combination

def func(l1, k):
    pairs = combination(l1, size=2)
    
    selected_pairs = [i for i in pairs if sum(i) == k]
    
    
    sel_pairs = []
    for i in pairs:
        s = sum(i)
        if s == k:
            sel_pairs.append(i)
    
    
    
    return selected_pairs
