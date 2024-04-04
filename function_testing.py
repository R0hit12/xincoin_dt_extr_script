list1 = ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Assist with Feeding (57)']
list2 = ['No', 'No', 'No', 'No', 'No', 'No', 'No','No', 'Yes',
         'Breakfast', 'Lunch', 'Assist with wa alking', 'Cane', 'Remind to take medications', 'Ask patient about pain']

# Extract unique elements from list2 that are also present in list1
filtered_elements = set([item for item in list2 if item in list1])

# Filter list1 based on the elements present in filtered_elements
list1_filtered = [item for item in list1 if item in filtered_elements]

print(list1_filtered)
