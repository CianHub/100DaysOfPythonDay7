# Lists
numList = [1, 2, 3, 4, 5]

# List methods

# Reverse list
numList.reverse()

# Sort list in this case undo reverse
numList.sort()

# Iterate through list
for num in numList:
    str(num)

# Convert string to list
str_example = 'test'
str_to_list = list(str_example)

# Access List values by index
first_item = str_to_list[0]

# Remove last item
str_to_list.pop()

# Add it back
str_to_list.insert(3, 't')

# Replace value
str_to_list[0] = 'b'

# Delete value
del str_to_list[0]

# Add it back
str_to_list.insert(0, 't')

# Remove specific value at an index
str_to_list.pop(0)

# Add a new value to the end
str_to_list.append('a')
