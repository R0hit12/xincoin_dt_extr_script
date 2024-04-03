manual_data_dict = {'LIVES WITH': "'Alone', 'Spouse', 'Family', 'Other'",
                      'FUNCTIONAL LIMITATIONS': "'Hearing', 'Vision', 'Speech', 'Nonverbal', 'Mobility', 'IADLS', 'ADL'S', 'Other'",
                        'DME / SUPPLIES': "'Cane', 'Walker', 'Wheelchair', 'Crutches', 'Rollator', 'Sliding board', 'Hoyer Lift', 'Incontinent supplies', 'Commode', 'Bedpan/urinal', 'Raised toilet seat', 'Shower chair', 'Grab bars', 'Hospital bed', 'Oxygen', 'Nebulizer', 'Diabetic supplies', 'Blood pressure machine', 'Prosthesis', 'Hearing aid', 'Glasses', 'Life alert', 'Other', 'GT', 'NG tube', 'IV supplies', 'Injection supplies', 'Ostomy supplies', 'Wound care supplies', 'Gloves', 'Bed rails', 'Catheter', 'Chux', 'Enema', 'Trach', 'Vent', 'Suction'",
                          'SPECIAL SAFETY PRECAUTIONS: 24 HOUR ON-CALL OR CALL 911 FOR EMERGENCIES': "'Safety Considerations / Precautions', 'Injuries / Bruising / Skin Breakdown', 'Fall / Safety Precautions', 'Pain', 'Burning on Urination, Cloudy Foul-Smelled Urine', 'Bleeding Precautions', 'Aspiration / Choking Precautions', 'Seizure Precautions', 'Oxygen Precautions', 'Dizziness', 'Feeding Tube Precautions', 'Hypo / Hyperglycemia Symptoms', 'Sharps Precautions', 'Elopement Risk'",
                            'ALLERGIES': "'No', 'known', 'allergies'",
                              'DIET': "'Regular', 'Low Fat', 'Low Sugar', 'Low Sodium', 'Fluid Restrictions', 'Supplements','Others'"}


for key, value in manual_data_dict.items():
    # Remove leading and trailing single quotes, split the value by comma and strip the whitespace
    values_list = [v.strip()[1:-1] for v in value.split(',')]
    # Update the dictionary with the values list
    manual_data_dict[key] = values_list

# print(manual_data_dict)

with open(r"C:\Users\Lenovo\Downloads\checkbox_content_page_2.txt", "r") as file:
    my_list = []
    for i in file:
        my_list.append(i.rstrip())  # Removes trailing newline character
print(my_list)




# Iterate over dictionary keys and values
for key, value_list in manual_data_dict.items():
    # Check each value in the list
    for value in value_list[:]:
        if key!= "ALLERGIES":
        # Get the first four alphabets of the first word
          first_word_first_four_letters = value.split()[0][:4]
          # Check if the first four alphabets of the first word are in my_list
          if first_word_first_four_letters not in [x[:4] for x in my_list]:
              value_list.remove(value)

print(manual_data_dict)