mean = 87
sd = 8

l = 104.6
h = 108.2

# How do we determine the z-scores corresponding to these values using Python's standard statistics package?

from statistics import NormalDist
# Standard normal distribution (mu=0, sigma=1)
z_l = (l - mean) / sd

print(f"z-score for {l}: {z_l:.4f}")
# How do we determine the percentage of data below l using Python's standard statistics package?

# We can use the cumulative distribution function (CDF) of the normal distribution.
# The CDF gives us the probability that a random variable from the distribution is less than or equal to a certain value.

# Method 1: Use the cumulative distribution function (CDF)
cdf_l = NormalDist().cdf(z_l)
print(f"Percentage of data below {l}: {cdf_l * 100:.4f}%")


z_h = (h - mean) / sd
cdf_h = NormalDist().cdf(z_h)
print(f"z-score for {h}: {z_h:.4f}")
print(f"Percentage of data below {h}: {cdf_h * 100:.4f}%")

answer = cdf_h - cdf_l
print(f"Percentage of data between {l} and {h}: {answer * 100:.4f}%")
print(f"Proportion of data between {l} and {h}: {answer:.4f}")

output = """
z-score for 104.6: 2.2000
Percentage of data below 104.6: 98.6097%
z-score for 108.2: 2.6500
Percentage of data below 108.2: 99.5975%
Percentage of data between 104.6 and 108.2: 0.9879%
Proportion of data between 104.6 and 108.2: 0.0099
"""
print()
print("--- CORRECT OUTPUT ---")
print(output)