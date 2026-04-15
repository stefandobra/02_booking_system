import datetime
from client import Client

def add_client():
    print("\n--- Please enter new client details ---")
    first_name = input("First Name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone numner: ")
    email_address = input("Email address: ")
    
    while True:
        option1 = input("Do you want to add client date of birth (Y/N): ").strip().upper()
        if option1 in ["Y", "N"]:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    if option1 == "Y":
        while True:
            dob_str = input("Date of birth (DD/MM/YYYY): ")
            try:
                dob = datetime.datetime.strptime(dob_str, '%d/%m/%Y').date()
                break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")          
    else:
        dob = None
        print("No date of birth entered!")
    
    while True:
        option2 = input("Do you want to add client gender (Y/N): ").strip().upper()
        if option2 in ["Y", "N"]:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    if option2 == "Y":
        while True:
            gender_input = input("Gender (F/M): ").strip().upper()
            if gender_input in ["F", "M"]:
                gender = gender_input
                break
            else:
                print("Invalid input. Please enter 'F' or 'M'.")
    else:
        gender = None
        print("No gender entered!")


    while True:
        option3 = input("Do you want to add client source (Y/N): ").strip().upper()
        if option3 in ["Y", "N"]:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    if option3 == "Y":
        source = input("Source: ")
    else:
        source = None
        print("No source entered!")

    while True:
        option4 = input("Do you want to add client ntoes (Y/N): ").strip().upper()
        if option4 in ["Y", "N"]:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    if option4 == "Y":
        notes = input("Notes: ")
    else:
        notes = None
        print("No notes entered!")

    return Client(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email_address=email_address,
        notes=notes,
        intake_forms=None,
        upcoming_appts=None,
        past_appts=None,
        gender=gender,
        dob=dob,
        source=source
    )

