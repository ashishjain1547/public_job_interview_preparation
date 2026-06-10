import numpy as np

l = [4, 5, 7, 7, 7, 8, 10, 11, 11, 13, 13, 14]

q1 = np.percentile(l, 25)
q3 = np.percentile(l, 75)

print("q1, q3:", q1, q3) # 7.0, 11.5

import numpy as np

l = [4, 5, 7, 7, 7, 8, 10, 11, 11, 13, 13, 14]

# NumPy >= 1.22.0 (using the 'method' parameter)
q3_nearest = np.percentile(l, 75, method='nearest')  # Returns 11
q3_lower   = np.percentile(l, 75, method='lower')    # Returns 11
q3_higher  = np.percentile(l, 75, method='higher')   # Returns 13

print("q3_nearest, q3_lower, q3_higher:")
print(q3_nearest, q3_lower, q3_higher)


# # NumPy < 1.22.0 (using the older 'interpolation' parameter)
# q3_nearest = np.percentile(l, 75, interpolation='nearest')  # Returns 11

print("---  CALCULATION AS PER KHAN ACADEMY ---")

median = np.median(l)
print("Median:", median) # 8.0

lower_half = [x for x in l if x <= median]
upper_half = [x for x in l if x >= median]

q1 = np.median(lower_half)
q3 = np.median(upper_half)
print("Q1:", q1) # 7.0
print("Q3:", q3) # 11.0