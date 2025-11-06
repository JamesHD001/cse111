"""
Author: Henry Daniel James.
Program Name: heart_rate.py

Description:
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

def calculate_heart_rate_range(age):
    max_heart_rate = 220 - age
    lower_bound = max_heart_rate * 0.65
    upper_bound = max_heart_rate * 0.85
    return lower_bound, upper_bound
def main():
    age = int(input("Enter your age: "))
    lower, upper = calculate_heart_rate_range(age)
    print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower:.1f} and {upper:.1f} beats per minute.")
if __name__ == "__main__":
    main()
