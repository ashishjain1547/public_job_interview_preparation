q1 = 2
q3 = 5
iqr = q3 - q1
print(iqr)

l = [1] + [2] * 7 + [3] * 5 + [5] * 3 + [6] * 2 + [7, 9]

print(l)

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(lower_bound, upper_bound)

outliers = [x for x in l if x < lower_bound or x > upper_bound]
print(outliers)
print(len(outliers))