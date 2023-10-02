"""
check given number positive or negative and even or odd.
ex:
input: 10
output: positive and even

input : 9
output : positive and odd

input : -2
output : negative and even
"""
# Nester decision
number = int(input("Enter Number: "))

if number > 0:
    if number % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    if number % 2 == 0:
        print("Number is Negative and even")
    else:
        print("Number is Negative and odd")
