import tabula
import pdfplumber


with pdfplumber.open('input\POC_RH18347Y_CAI GUO_03122024.pdf') as file:

    list1 = []
    # print(len(file.pages))
    first_page = file.pages[2]  # Accessing the first page
    tables = first_page.extract_tables()
    # print(tables)
    print(len(tables))
    # print(tables[0][7][0])#-------------- got data
    # print(tables[0][7])
    for table in tables:
        list1.extend(table)
        # print(table)
flattened_data = [item for sublist in list1 if sublist is not None for item in sublist if item is not None]

split_data = [item.split('\n') for item in flattened_data]

# Flatten the list
flattened_data = [item.strip() for sublist in split_data for item in sublist]
flattened_data = [item.replace(", ", ",") for sublist in split_data for item in sublist]

# headings = ['NAME OF PATIENT (Last,first,middle)',"MEDICAID ID",'DOB (m/d/Y,age)',"SEX",
#                        "HOME STREET ADDRESS (Street or RFD; City or Town; State; and ZIP Code)","PHONE 1",
#                        "PHONE 2","VISIT DATE","ASSESSMENT TYPE",'PATIENT REPRESENTATIVE/EMERGENCY CONTACT']

data = flattened_data

print(flattened_data)




# for i in range(len(headings) - 1):
#     start_heading = headings[i]
#     end_heading = headings[i + 1]
    
#     start_index = data.index(start_heading)
#     end_index = data.index(end_heading)
    
#     extracted_data = data[start_index + 1:end_index]
    
#     # Join the extracted data into a single string
#     extracted_data_string = ' '.join(extracted_data)
    
#     # Extract and print the data
#     print(f"{start_heading}: {extracted_data_string}")


# print(list1)