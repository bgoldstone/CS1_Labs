# sphere.py
# 
# Name: Ben Goldstone
# Date: 9/1/2020
#
# Asks user for the radius of a sphere, and computes its
# diameter, surface area, and volume.
# A useful value:
PI = 3.14159265359

# Initialize the radius:
radius = float(input("Please enter a radius: "))
print()
# Calculate the properties of the sphere:
diameter = 2 * radius
area = 4 * PI * radius ** 2
volume = (4/3) * PI * radius ** 3
 # Print the results:
print("sphere radius = ", radius)
print()
print("diameter =", diameter)
print("area\t =", area)
print("volume\t =", volume)
