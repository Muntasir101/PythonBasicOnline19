
# keyword arguments
# function with 2 parameters; a and b
def summation(a, b):
    return a + b


print(summation(20, 40))  # passing arguments


# default argument
def subtraction(a=100, b=20):
    return a - b


print(subtraction())  # 80
print(subtraction(40, 10))  # 30


# arbitrary argument
def print_animals(*animals):
    for animal in animals:
        print(animal)


# print_animals("Lion", "Tiger", "Mammal", "wolf")
