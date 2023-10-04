txt = 'Hello world'
print(txt[1])
print(txt[2:5])

# strip()
message = " Hello "
print(message.strip())
print(message.upper())
print(message.lower())
txt = txt.replace("h", "j")
print(txt)

age = 50
tax = 10.5

# template then format
txt = "My name is John, and I am {}"
print(txt.format(age))

# Template and format
print(f"My name is John, and I am {age} and My tax is {tax}")
