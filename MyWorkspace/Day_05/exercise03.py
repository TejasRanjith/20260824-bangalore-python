import re
def scrape_directory_phones(directory_text):
    phone_book=[]
    m1 = re.findall(r"([0-9-()\s]{3,})",directory_text)
    print(m1)
    for num in sorted(m1):
        phone_record,num = dict(),num.strip()
        print(num)
        if len(num) == 12:
            phone_record["area_code"] = num[:3]
            phone_record["prefix"] = num[4:7]
            phone_record["line_number"] = num[8:]
            phone_record["formatted"] = f"({phone_record['area_code']}) {phone_record['prefix']}-{phone_record['line_number']}"
            # phone_book.append(phone_record)
        elif len(num) == 10:
            phone_record["area_code"] = num[:3]
            phone_record["prefix"] = num[3:6]
            phone_record["line_number"] = num[6:]
            phone_record["formatted"] = f"({phone_record['area_code']}) {phone_record['prefix']}-{phone_record['line_number']}"
        elif len(num) ==14:
            phone_record["area_code"] = num[1:4]
            phone_record["prefix"] = num[6:9]
            phone_record["line_number"] = num[10:]
            phone_record["formatted"] = f"({phone_record['area_code']}) {phone_record['prefix']}-{phone_record['line_number']}"            
        phone_book.append(phone_record)
    for item in phone_book:
        print(item)

directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
scrape_directory_phones(directory)