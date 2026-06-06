import numpy as np

l = [4, 5, 7, 7, 7, 8, 10, 11, 11, 13, 13, 14]

q1 = np.percentile(l, 25)
print(q1) # 7.0

q3 = np.percentile(l, 75)
print(q3) # 11.5


import numpy as np

l = [4, 5, 7, 7, 7, 8, 10, 11, 11, 13, 13, 14]

# NumPy >= 1.22.0 (using the 'method' parameter)
q3_nearest = np.percentile(l, 75, method='nearest')  # Returns 11
q3_lower   = np.percentile(l, 75, method='lower')    # Returns 11
q3_higher  = np.percentile(l, 75, method='higher')   # Returns 13

print(q3_nearest)
print(q3_lower)
print(q3_higher)


# # NumPy < 1.22.0 (using the older 'interpolation' parameter)
# q3_nearest = np.percentile(l, 75, interpolation='nearest')  # Returns 11
