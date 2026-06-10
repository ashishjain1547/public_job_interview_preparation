def area_of_trapezium(b1, b2, h):
    return 0.5 * (b1 + b2) * h

b1 = 0.5
b2 = 0.75
h = 1

a = area_of_trapezium(b1, b2, h)
print(a)

print(round(a*100, 4))


b1 = 0.25
b2 = 0.5
h = 1

a = area_of_trapezium(b1, b2, h)
print(a)

print(round(a*100, 4))
