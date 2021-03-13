# monteCarlo.py
# A program that approximates Pi using a random float generator and the formula of a circle
# Date: 9/15/2020
# Name: Ben Goldstone

#imports Random Library
from random import *
hits = 0;
shots = int(input("How many trials would you like to run? "))
# loops for total number of shots
for i in range(shots):
    x = (2 * random()) - 1.0
    y = (2 * random()) - 1.0
    if((x ** 2) + (y ** 2) <= 1):
        hits += 1
print(f"Pi Approximation: {4*(hits/shots)}")

