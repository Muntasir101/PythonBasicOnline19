def find_largest_smallest(numbers):
    largest = smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest


# get user input for a list of numbers
input_numbers = input('Enter a list of numbers separated by spaces')
numbers = [int(num) for num in input_numbers.split()]

largest, smallest = find_largest_smallest(numbers)

print(f"The Largest number is: {largest}")
print(f"The Smallest number is: {smallest}")
