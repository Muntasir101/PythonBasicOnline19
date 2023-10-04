my_list = [1, 2, 3, 4, 5, 6]

# append(): Adds an element to the end of the list
my_list.append(7)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7]

# extend(): Appends the element of an iterable to the end of the list
my_list.extend([8, 9])
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert(i, e): insert element(e) at position(i)
my_list.insert(0, 0)
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove(): remove the first occurrence of element
number_list = [1, 2, 3, 4, 2, 1, 3, 4, 3]
number_list.remove(2)
print(number_list)  # [1, 3, 4, 2, 1, 3, 4]

# pop(i): remove and return the element at index i
popped_element = my_list.pop(1)
print("popped: ", popped_element)
print(my_list) # [0, 2, 3, 4, 5, 6, 7, 8, 9]

# count: returns the number of occurrences of element
count = number_list.count(3)
print("count: ", count)

# sort(): Sorts the list in ascending order
number_list.sort()
print("sort: ", number_list)

# reverse(): Reverse the order
number_list.reverse()
print("reverse: ", number_list)

print(len(number_list))  # 7

# get the first element of the list by index
print(number_list[0])

# get the last element of the list by index
print(number_list[len(number_list)-1])

# clear(): Removes all elements, make it empty
my_list.clear()
print(my_list)



