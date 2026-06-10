mean = 1497
sd = 322

proportion = 0.85

import statistics
z = statistics.NormalDist().inv_cdf(proportion)

x = z * sd + mean

print(round(x, 4))