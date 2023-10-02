#print("Hello world!")

# template
"""
for item in sequence:
    code
"""
"""
for _ in range(10):
    print("Hello Dhaka!")
"""

"""
for item in range(1, 10, 3):
    print(item, "Good Day")
"""

lower_value = int(input("Enter lower value: "))
upper_value = int(input("Enter upper value: "))
increment_value = int(input("Enter increment value: "))

for item in range(lower_value, upper_value, increment_value):
    print(item, "Great")
