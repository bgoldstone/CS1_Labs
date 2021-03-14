# 4_speedTrap.py
# a program that takes the speed limit on a street and the speed of a car in as input,
# and outputs if you are going the legal speed limit, if you are speeding, or if you are excessively speeding
# Date: 9/15/2020
# Name: Ben Goldstone
# gets speed limit from user
speedLimit = int(input("What is the speed limit of the street? "))
# gets speed of car from user
speedOfCar = int(input("What speed are you going? "))
# If Driving a Legal Speed
if(speedOfCar <= speedLimit):
    print(f"You are going a legal speed of {speedOfCar} mph at {speedLimit - speedOfCar} mph under the speed limit.")
# If Common Speeding
elif(speedOfCar < (speedLimit + 31)):
        print(f"You are going {(speedOfCar-speedLimit)} mph over the speed limit.")
# If Excessive Speeding
else:
    print(f"You are going {(speedOfCar - speedLimit)} mph over the speed limit.")
    print("You are subject to an immediate 15-day driver's license suspension")
