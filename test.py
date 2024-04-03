import pdfplumber

# Open the PDF file
with pdfplumber.open('input\POC_RH18347Y_CAI GUO_03122024.pdf') as file:

    third_page = file.pages[2]
    tables = third_page.extract_tables()
    print(len(tables))
    print(tables[0])
    # Open a new text file to write the extracted data
    # with open('extracted_data.txt', 'w') as output_file:
    #     # Iterate over the pages
    #     for page in file.pages:
    #         # Extract tables from the current page
    #         tables = page.extract_tables()
    #         # Iterate over the tables on the page
    #         for table in tables:
    #             # Iterate over the rows in the table
    #             for row in table:
    #                 # Check if any element in the row is None
    #                 if any(cell is None for cell in row):
    #                     # Skip this row if it contains any None values
    #                     continue
    #                 # Join the elements of the row into a single string with tab separation
    #                 row_text = '\t'.join(str(cell) for cell in row)
    #                 # Write the row to the output file
    #                 output_file.write(row_text + '\n')
    #             # Add an empty line between tables
    #             output_file.write('\n')
