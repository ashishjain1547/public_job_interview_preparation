xmean = 24.1
ymean = 12.9
sx = 12
sy = 16.2
r = 0.9

m = r * (sy/sx)
c = ymean - m*xmean

print("m, c:", round(m, 3), round(c, 3))

# KA's Answers: 1.22, -16.38