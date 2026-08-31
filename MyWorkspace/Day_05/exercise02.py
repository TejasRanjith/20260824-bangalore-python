import re
def validate_password(password):
    if len(password) < 8:
        print("Password must contain at least 8 characters.")
    elif not re.search(r"[A-Z]",password):
        print("Password must contain at least one uppercase letter.")
    elif not re.search(r"[a-z]",password):
        print("Password must contain at least one lowercase letter.")
    elif not re.search(r"[0-9]",password):
        print("Password must contain at least one number.")
    elif not re.search(r"[@#$!%^&*]",password):
        print("Password must contain at least one special character.")
    else:
        print("Your Password is valid.")
        
        

validate_password("Tejas@035611")
# validate_password("Tejas1033")
# validate_password("tejas1033")
# validate_password("t")
    