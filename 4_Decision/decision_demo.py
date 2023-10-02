"""
if condition:
    code
"""
"""
age = int(input("Enter Age: "))
if age <= 10:
    print("Child")
else:
    print("Adult")
"""
age = int(input("Enter Age: "))

if age >= 80:
    print("Old")
elif age >= 60:
    print("Senior Citizen")
elif age >= 30:
    print("Adult")
elif age >= 10:
    print("Teenager")
else:
    print("Child")
