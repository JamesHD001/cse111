def multiply(first, second, third):
    """ This program multiplies three numbers and returns the result"""
    result = first * second * third
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
answer = multiply(num1, num2, num3)
print(f"The result of multiplying {num1}, {num2}, and {num3} is: {answer}")