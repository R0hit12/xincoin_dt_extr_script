import tabula
import pdfplumber

 
s_list = []
with open("output_texts/page_3.txt","r")as file:
    for i in file:
        s_list.append(i)
# print(s_list)

split_data = [item.split('\n') for item in s_list]

# Flatten the list
flattened_data = [item.strip() for sublist in split_data for item in sublist]
# flattened_data = [item.replace(", ", ",") for sublist in split_data for item in sublist]
cleaned_list = [item for item in flattened_data if item.strip()]
# print(cleaned_list)



manual_dict = {'BATH: TUB (15)': ['Yes', 'No'], 'BATH: SHOWER (16)': ['Yes', 'No'], 'BATH: BED (18)': ['Yes', 'No'],
                'GROOMING: SHAVE (23)': ['Yes', 'No'], 'GROOMING: NAIL CARE (FILE NAILS ONLY) (24)': ['Yes', 'No'],
                  'DRESSING(27)': ['Yes', 'No'], 'SKIN CARE (23)': ['Yes', 'No'], 'FOOT CARE (20)': ['Yes', 'No'],
                    'PREPARE MEALS(58)': ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Assist with Feeding (57)'],
                      'ORAL CARE (19)': ['Mouth Care (19)', 'Denture Care (19)'], 'HAIR CARE (21)': ['Comb (21)', 'Shampoo (21)'],
                        'TRANSFERS(43) AND AMBULATION(42)': ['Contact Guard', 'Assist with walking', 'Cane', 'Crutches', 'Walker', 'Wheelchair', 'Rollator', 'Bedbound', 'ROM Turn Q2 Hours', 'Hoyer Lift 2 person assist', 'Hoyer Lift 1 person assist'],
                        'MEDICATIONS(60)': ['Remind to take medications', 'Ask patient about pain', 'FREQUENCY 3xweek'],
                          'ESCORT TO APPOINTMENT (83)': ['Yes', 'No', 'As', 'patient', 'needed']}


headings = ["BATH: TUB (15)","BATH: SHOWER (16)","BATH: BED (18)","GROOMING: SHAVE (23)","GROOMING: NAIL CARE (FILE NAILS ONLY) (24)","DRESSING(27)",
            "SKIN CARE (23)","FOOT CARE (20)","PREPARE MEALS(58)","ORAL CARE (19)","HAIR CARE (21)","TRANSFERS(43) AND AMBULATION(42)",
            "MEDICATIONS(60)","ESCORT TO APPOINTMENT (83)"]

c_box_list = ['No', 'No', 'No', 'No', 'No', 'No', 'No','No', 'Yes', 'Breakfast', 'Lunch', 'Assist with wa alking', 'Cane', 'Remind to take medications', 'Ask patient about pain']

# print(list1)

# data_dict = {}
#----------- Code to get the dictionary with Keys and values ,
#  values are added in a list to map so all  are separated so have to manually correct some values

# Iterate through the list to find data between consecutive headings
# current_heading = None
# current_values = []
# for item in cleaned_list:
#     if item in headings:
#         if current_heading is not None:
#             data_dict[current_heading] = current_values
#             current_values = []  # Reset values for new heading
#         current_heading = item
#     elif current_heading is not None:
#         current_values.extend(item.split())  # Split values and add to the current values list

# # Add the last set of values to the dictionary
# if current_heading is not None:
#     data_dict[current_heading] = current_values

# print(data_dict)

#---------------------------------------------------------------------------------------

c_box_list = ['No', 'No', 'No', 'No', 'No', 'No', 'No','No', 'Yes',
               'Breakfast', 'Lunch', 'Assist with wa alking', 'Cane', 'Remind to take medications', 'Ask patient about pain']

# with open("c_box/checkbox_content_page_3.txt","r") as file:
#     for i in file:
#         c_box_list.append(i.rstrip())
# print(c_box_list)


print(manual_dict[headings[8]])



for i in range(0,14):
    if i<8:
        a = headings[i]
        b = c_box_list[i]
        manual_dict[a] = [b]
    # print(manual_dict)

    elif i<13:
        a = headings[i]
        b = c_box_list
        c = manual_dict[a]
        
        # Extract unique elements from list2 that are also present in list1
        filtered_elements = set([item for item in b if item in c])

        # Filter list1 based on the elements present in filtered_elements
        list1_filtered = [item for item in c if item in filtered_elements]
        if list1_filtered == []:
            list1_filtered = ["No"]

        manual_dict[a] = list1_filtered
    else:
        a = headings[i]
        b = c_box_list[8]
        manual_dict[a] = [b]
print(manual_dict)


        