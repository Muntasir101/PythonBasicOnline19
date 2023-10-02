"""
default_username = "admin"
default_password = "123456"

# Ask the user for input
user_input_username = input("Username: ")
user_input_password = input("Password: ")

if user_input_username == default_username and user_input_password == default_password:
    print("Login successful")
else:
    print("Login failed")
"""

user_credentials = {
    "admin": "admin123",
    'super admin': "superadmin123",
    'user': 'user123'
}

# Ask the user for input
user_input_username = input("Username: ")
user_input_password = input("Password: ")

if user_input_username in user_credentials:
    if user_input_password == user_credentials[user_input_username]:
        print("Login successful")
    else:
        print("Login failed.Incorrect password")
else:
    print("Login failed. User does not exist")