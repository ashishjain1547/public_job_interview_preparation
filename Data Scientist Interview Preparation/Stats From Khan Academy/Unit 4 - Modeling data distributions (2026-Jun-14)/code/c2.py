mean = 80
sd = 9

proportion = 0.4

import statistics
z = statistics.NormalDist().inv_cdf(proportion)

print(z)

x = z * sd + mean

print(x)