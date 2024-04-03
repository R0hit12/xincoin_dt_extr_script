with open("output_texts\page_2.txt", 'r') as file:
    data = []
    for line in file:
        # Remove the newline character from each line
        line = line.strip()
        data.append(line)


headings = ["LIVES WITH","FUNCTIONAL LIMITATIONS",'DME / SUPPLIES','SPECIAL SAFETY PRECAUTIONS: 24 HOUR ON-CALL OR CALL 911 FOR EMERGENCIES','ALLERGIES','DIET']