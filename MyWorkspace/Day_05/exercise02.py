import re
def validate_academic_email(email):
    m = re.search(r"^([a-z0-9._]+)@([a-z.-]).([a-z.])$",email)
    if m:
        print(m.groups())
    else:
        print("No M")

print(validate_academic_email("arham.khan@cdac.res.in"))