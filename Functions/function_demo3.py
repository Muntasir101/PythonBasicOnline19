c = 50


def summation():
    a = 20
    b = 50
    # print(a + b + c)
    return a + b + c
    print("Hello world")  # unreachable statement


def subtraction():
    a = 20
    b = 5
    # print(a - b - c)
    # return a - b - c
    return summation() - a - b


print(summation())
print(subtraction())

result = summation() + subtraction()
print(result)


def get_name_and_age():
    name = "smith"
    age = 20
    return name, age


# print(get_name_and_age())  # ('smith', 20)
name_age = get_name_and_age()  # ('smith', 20)
print(name_age[0])  # smith
