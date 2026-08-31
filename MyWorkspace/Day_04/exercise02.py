InvalidPhoneNumberError = Exception()
InvalidPhoneNumberError.__str__ = "This is my custom error"


def register_contact(phonebook, name, phone_input):
    try:
        if len(name) == 0:
            raise ValueError
    except ValueError:
        print("Contact name must be a non-empty alphabetic string.")
    
    try:
        phone_input = int(phone_input)
    except ValueError:
        # print("Phone number must contain digits only.")
        raise InvalidPhoneNumberError

register_contact(dict(),"","")