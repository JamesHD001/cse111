"""
Author: Henry Daniel James

Description:
Write a Python program named random_numbers.py that creates a list of numbers, appends more numbers onto the list, and prints the list. The program must have two functions named main and append_random_numbers as follows:

Requirements
Your program includes two functions named main and append_random_numbers. The append_random_numbers function has two parameters named numbers_list and quantity, and quantity has a default value of 1.
The main function calls append_random_numbers twice, first with one argument and second with two arguments.
The append_random_numbers function includes a loop that appends quantity random numbers at the end of numbers_list.
"""

import random

def main():
    """
    Main function to create and print a list of random numbers.
    """
    numbers = []
    random_words = []
    append_random_numbers(numbers, 2)
    print(numbers)
    append_random_words(random_words, 3)
    print(random_words)
    
def append_random_numbers(numbers_list, quantity=1):
    """Appends random numbers to a list."""
    for _ in range(quantity):
        random_number = random.uniform(1, 100)
        random_number = round(random_number, 2)
        numbers_list.append(random_number)
        
def append_random_words(wordlist, quantity=1):
    """Appends random words to a list."""
    random_words = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Temple', 'Nephi', 'Laman', 'Lemuel', 'Jared']
    for _ in range(quantity):
        random_words = random.choices(random_words)
        wordlist.append(random_words)
        
if __name__ == "__main__":
    main()