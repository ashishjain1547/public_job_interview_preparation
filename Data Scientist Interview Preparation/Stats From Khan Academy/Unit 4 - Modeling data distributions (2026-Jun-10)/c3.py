mean = 13.1
sd = 1.5

sd1 = (mean - sd, mean + sd)
print(sd1)

sd2 = (mean - 2 * sd, mean + 2 * sd)
print(sd2)

sd3 = (mean - 3 * sd, mean + 3 * sd)
print(sd3)

sd2_area = 0.95
sd3_area = 0.997

area_req = (sd3_area - sd2_area) / 2

print(area_req)

percentage_wise = round(area_req * 100, 4)
print(percentage_wise)

out = """
(11.6, 14.6)
(10.1, 16.1)
(8.6, 17.6)
0.02350000000000002
2.35
"""
