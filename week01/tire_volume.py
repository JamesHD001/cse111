"""
    Author: Henry Daniel James
    Course: CSE 111 - Programming with Functions
    Week 01 Project: Tire Volume
    Description: This program asks the user for tire dimensions, computes the tire volume, displays it, and logs the details to a text file.

    Creativity/Features:
    - Added a feature that first asks the user if they would like to purchase a tire.
    - If the user selects "yes," the program collects their details, performs the tire volume calculation, and logs the information for future reference.
    - If the user selects "no," the program offers an expert tire analysis option, allowing the volume calculation to still be performed without collecting personal purchase details.
    - If the user declines both options, the program ends gracefully.
"""

from math import pi
from datetime import datetime

def tire_volume(width, aspect_ratio, wheel_diameter):
    """Compute and return the volume of a tire."""
    volume = (pi * width**2 * aspect_ratio *
              (width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000
    return volume

print("Welcome to the Tire Expert!")
print("This program calculates the volume of a tire.\n")

while True:
    purchase = input("Would you like to purchase a tire? (yes/no): ").strip().lower()

    if purchase == "yes":
        name = input("Please enter your name: ").strip()
        contact = input("Please enter your contact information: ").strip()
        volume = None

        width = int(input("Enter the width of the tire in mm: "))
        aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
        wheel_diameter = int(input("Enter the diameter of the wheel in inches: "))

        volume = tire_volume(width, aspect_ratio, wheel_diameter)
        print(f"\nThe approximate volume is {volume:.2f} liters\n")

    elif purchase == "no":
        expert = input("Would you like an expert tire volume analysis instead? (yes/no): ").strip().lower()

        if expert == "yes":
            name = ""
            contact = ""
            volume = None

            width = int(input("Enter the width of the tire in mm: "))
            aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
            wheel_diameter = int(input("Enter the diameter of the wheel in inches: "))

            volume = tire_volume(width, aspect_ratio, wheel_diameter)
            print(f"\nThe approximate volume is {volume:.2f} liters\n")
        else:
            print("\nNo problem! Have a great day.\n")
            break
    else:
        print("Invalid input. Please answer yes or no.")
        continue

    current_date = datetime.now().strftime("%Y-%m-%d")
    with open("volumes.txt", mode="at") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {wheel_diameter}, "
                   f"{volume:.2f}, {name}, {contact}\n")

print("Thank you for using the Tire Expert program. Goodbye!")
