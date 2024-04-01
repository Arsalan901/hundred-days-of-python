# Sure, here is a Python program that calculates the mean, median, and mode for ungrouped data:


from collections import Counter
from statistics import mean, median,mode

# Ungrouped data
data = [2, 3, 4, 5, 6, 5, 4, 3, 2, 2, 4, 5, 6]

# Mean calculation
mean_value = mean(data)

# Median calculation
median_value = median(data)

# Mode calculation
mode_value = mode(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
