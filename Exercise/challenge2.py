input_string = input("Enter your word: ")

# remove spaces and convert to lowercase
s = input_string.replace(" ", "").lower()

# check if the string is equal to its reverse
if s == s[::-1]:
    print(f"{input_string} is a Palindrome")
else:
    print(f"{input_string} is not a Palindrome")
