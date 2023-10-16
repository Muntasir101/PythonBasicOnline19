# get user input for upper limit
user_defined_limit = int(input("Enter upper limit:"))

# initialized a variable to store the sum
sum_of_evens = 0

# loop through numbers from 1 to user defined limit
for number in range(1, user_defined_limit + 1):
    if number % 2 == 0:
        sum_of_evens += number

print(f"Ths sum of evens from 1 to {user_defined_limit} is: {sum_of_evens}")

