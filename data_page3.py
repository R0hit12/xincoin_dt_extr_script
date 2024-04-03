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
# print(list1)

list1 = list1[1]

print(list1)

headings = ["BATH: TUB(15)","BATH: SHOWER","BATH: BED","GROOMING: SHAVE","GROOMING: NAIL CARE (FILE NAILS ONLY) (24)","DRESSING(27)",
            "SKIN CARE (23)","FOOT CARE (20)","PREPARE MEALS(58)","ORAL CARE (19)","HAIR CARE (21)","TRANSFERS(43) AND AMBULATION(42)",
            "MEDICATIONS(60)"]