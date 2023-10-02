# looping through a list
"""

# print all item
fruits = ['apple', 'orange', 'banana', 'cherry']
for fruit in fruits:
        print(fruit)

# print apple 3 times than all item
fruits = ['apple', 'orange', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    if index == 0:
        for _ in range(2):
            print(fruits[0])
    print(fruit)
"""

"""
# print every item 3 times
fruits = ['apple', 'orange', 'banana', 'cherry']
for fruit in enumerate(fruits):
    for _ in range(3):
        print(fruit)
"""

"""
message = "Hello world"
for letter in message:
    print(letter)
    
print(len(message))
"""

"""
# Nested loop : 2D Grid
for i in range(3):
    for j in range(3):
        print(i, j)
"""
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i, j, k)