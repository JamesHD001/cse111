"""
Author: Henry Daniel James

Purpose/Description:
This module provides a function to evaluate the strength of a given password.
This function checks for length, presence of uppercase and lowercase letters,
digits, and special characters to determine if the password is strong.
"""
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(password, min_length=10, strong_length=16):
    pass

def main():
    password = input("Enter a password to test it's strength (or type 'q' to quit the program): ")
    while password.lower() != 'q':
        password = input("Enter a password to test its strength (or 'q' to quit the program): ")
        
    else:
        print("Exiting the program. Goodbye!")
        exit()

if __name__ == "__main__":

    main()
