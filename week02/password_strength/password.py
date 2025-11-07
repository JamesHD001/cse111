"""
Author: Henry Daniel James
Purpose: CSE111 W02 - Password Strength Project

Project Requirements:

- Function: word_in_file(word, filename, case_sensitive=False)
- Check if `word` is in the specified file.

- Function: word_has_character(word, character_list)
- Check if `word` contains any character from `character_list`.

- Function: word_complexity(word)
- Return complexity score based on character types present.

- Function: password_strength(password, min_length=10, strong_length=16)
- Determine password strength with specified rules.

- Main Program:
- Loop to get user input and display password strength until 'q' or 'Q' is entered.
    
Enhancements Made:
- I preloaded word lists into sets for faster lookup in `word_in_file`.
"""

LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

#Load the word files into sets
with open("wordlist.txt", "r", encoding="utf-8") as f:
    wordlist = {line.strip().lower() for line in f}

with open("toppasswords.txt", "r", encoding="utf-8") as f:
    toppasswords = {line.strip() for line in f}

#Iterate through the files and check if the password exists in either file
def word_in_file(word, filename, case_sensitive=False):
    if "wordlist" in filename.lower():
        return word.lower() in wordlist
    elif "toppassword" in filename.lower():
        return word in toppasswords
    return False

#Iterate through the characters in the word and check if any character exists in the character list
def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False

#Iterate through the character types and calculate complexity
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

#Iterate through the files, password  and calculate the password strength
def password_strength(password, min_length=10, strong_length=16):
    if password.lower() in wordlist:
        print("Password is a dictionary word and is not secure.")
        return 0

    if password in toppasswords:
        print("Password is a commonly used password and is not secure.")
        return 0

    #Check the length of the password
    length = len(password)
    if length < min_length:
        print("Password is too short and is not secure.")
        return 1

    if length >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    #Calculate the complexity score
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

#The man program function to get user input, iterate and display password strength
def main():
    while True:
        password = input("Enter a password to test (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password)
        print(f"Password strength (0–5): {strength}\n")

if __name__ == "__main__":
    main()
    