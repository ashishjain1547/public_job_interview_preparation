# building a module
# function that returns a rolling mean

l = []
# cn: curr_number
def roll_mean(cn, k):
    
    if not(cn.isinstance(int) or cn.isinstance(float)):
        
    
    global l
    if len(l) == k:
        l = l[-(k-1):] + [cn]
    elif len(l) < k:
        l.append(cn)
    
    if len(l) == k:
        out = sum(l) / len(l)
        return out
    elif len(l) < k:
        return None
    
    

k = 5
stream_data = [1,2,3,4,5,6,7,8,9,10]
 
for current_num in stream_data:
    print(roll_mean(current_num, k))
        