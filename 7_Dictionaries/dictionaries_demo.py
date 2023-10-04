user_details = {
    "username": "admin",
    "password": 123456,
    "email": "admin@mail.com"
}

# Adding Entries
user_details["address"] = "Dhaka"
print(user_details)

# Updating Entries
user_details["address"] = "NY"
print(user_details)  # {'username': 'admin', 'password': 123456, 'email': 'admin@mail.com', 'address': 'NY'}

# Accessing Values
username_value = user_details["username"]  # provide key
print(f"Username: {username_value}")

# Checking if key exists in the dictionary
if 'email2' in user_details:
    print(f"Email:", user_details["email"])
else:
    print("Key not found!")

# Iterating over keys
for key in user_details.keys():
    print(f"Key:", key)

# Iterating over values
for value in user_details.values():
    print(f"Value:", value)

# Iterating over key-value pairs
for key, value in user_details.items():
    print(key, value)

print(len(user_details))  # 4

# Removing Entries
del user_details['address']
print(len(user_details))  # 3
print(user_details)  # {'username': 'admin', 'password': 123456, 'email': 'admin@mail.com'}
