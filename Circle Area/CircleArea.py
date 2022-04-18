from cmath import pi
import math

# Get r
r = float(input("Enter r from circle : "))

# Calculate area and convert to string
area = str((r*r) * pi)

# Print result
print("Area is : " + area)
