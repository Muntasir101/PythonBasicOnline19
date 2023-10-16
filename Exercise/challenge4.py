def remove_duplicate(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_elements = input('Enter a list of numbers separated by spaces')
elements = input_elements.split()

unique_elements = remove_duplicate(elements)

print(f"List with unique elements {unique_elements}")