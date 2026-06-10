mean = 66000
sd = 22000

# How do we determine the z-score with an area of 0.05 above it using Python?

from scipy.stats import norm

# Method 1: Use the percent point function (ppf)
# The ppf takes the cumulative probability to the LEFT.
# Since the area above is 0.05, the area below is 1 - 0.05 = 0.95.
z_score = norm.ppf(0.95)

# Method 2: Use the inverse survival function (isf)
# The isf directly takes the upper tail probability.
z_score_alt = norm.isf(0.05)

print(f"z-score (ppf): {z_score}")     # 1.6448536269514729
print(f"z-score (isf): {z_score_alt}") # 1.6448536269514729

print("--- Using standard \"statistics\" Package ---")

from statistics import NormalDist

# Standard normal distribution (mu=0, sigma=1)
z = NormalDist().inv_cdf(0.95)
print(z)  # 1.6448536269514722

x = mean + z * sd
print(f"Value corresponding to z-score: {x}")  # 101000.0


