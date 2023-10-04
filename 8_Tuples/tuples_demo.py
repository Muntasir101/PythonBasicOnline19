my_tuple = (1, 2, 3, 4)

# Accessing Element
print(my_tuple[0])  # 1 using positive index
print(my_tuple[-1])  # 4 using negative index

# Slicing
print(my_tuple[0:2]) # (1, 2)

# Length
print(len(my_tuple)) # 4

# count: returns the number of occurrences of element
count = my_tuple.count(1)
print('Count', count)

# Iterating over the tuple
for item in my_tuple:
    print(item)
