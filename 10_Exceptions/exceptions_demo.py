"""
# SyntaxError
print("Error)
"""

"""
# IndentationError
if True:
print("IndentationError")
"""

"""
# NameError
age = 20
print(Age)
"""

"""
# TypeError
result = 10 + '5'
print(result)
"""

"""
# valueError
user_input = input("Please Enter Number:")
number = int(user_input)
print(number)
"""

"""
# ZeroDivisionError
result = 20/0
print(result)
"""

"""
# indexError
my_list = [1, 2, 3]
print(my_list[4])
"""

"""
# keyError
user = {
    'name': 'smith',
    'age': 20,
    'password': 1234
}
print(user['email'])
"""

"""
# FileNotFoundError
file_obj = open('testfile2.txt', 'r')
fileText = file_obj.read()
print(fileText)
file_obj.close()
"""