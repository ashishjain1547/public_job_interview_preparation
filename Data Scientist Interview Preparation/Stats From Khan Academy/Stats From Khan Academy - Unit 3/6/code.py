import numpy as np

l = [1, 2, 3, 3, 4, 4, 4, 6]

q1 = np.percentile(l, 25)
q3 = np.percentile(l, 75)

print(q1, q3)

iqr = q3 - q1
print(iqr)


print("--- CALCULATION AS PER KHAN ACADEMY ---")

m = np.median(l)

lower = [x for x in l if x <= m]
upper = [x for x in l if x >= m]

print(lower, upper)
q1 = np.median(lower)
q3 = np.median(upper)
print(q1, q3)

iqr = q3 - q1
print(iqr)

