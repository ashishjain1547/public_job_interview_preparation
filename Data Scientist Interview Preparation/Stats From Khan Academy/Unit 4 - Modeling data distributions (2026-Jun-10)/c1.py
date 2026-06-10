mean = 170.4
sd = 10

l = 145
lz = (l - mean) / sd
print(lz)

import statistics
lz_area = statistics.NormalDist(mu=0, sigma=1).cdf(lz)
print(lz_area)

h = 171
hz = (h - mean) / sd
print(hz)

hz_area = statistics.NormalDist().cdf(hz)

area_req = round(hz_area - lz_area,4)
print(area_req)

