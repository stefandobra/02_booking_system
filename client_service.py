import datetime
from client import Client
import json

def save_clients(clients):
    clients_dict=[]
    for client in clients:
        clients_dict.append(client.__dict__)
              
    data_to_save = {
        "clients": clients_dict
    }
    
    with open ("data.json", "w") as file:
        json.dump(data_to_save, file)

def load_clients():
    try:
        clients_from_file = []
        with open("data.json", "r") as file:
            data_to_load = json.load(file)
        
        for client in data_to_load["clients"]:
            clients_from_file.append(Client(**client))
        return clients_from_file

    except FileNotFoundError:
        print("No saved data found, starting fresh")
        return []
    
    except json.JSONDecodeError as error:
        print("Invalid JSON syntax:", error)
        return []

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

def view_clients(clients: list):
    if clients:
        i = 1
        print(f"\n--- Client list ---")
        for client in clients:
            print(f"{i}. {client.first_name} {client.last_name} p: {client.phone_number} e: {client.email_address}")
            i += 1
    else:
        print("No clients saved!")

def search_client(clients: list):
    print("\n--- Search Client ---")
    print("1. Search by email")
    print("2. Search by phone")

    while True: 
        option = input("Please select an option: ").strip()
        if option in ["1", "2"]:
            break  
        else:
            print("Invalid selection Please enter '1' or '2'")

    if option == "1":
        search_for = input("Please enter email address: ")
    else:
        search_for = input("Please enter phonu number: ")
    
    if clients:
        for client in clients:
            if option == "1":
                if client.email_address == search_for:
                    print(f"{client.first_name} {client.last_name} p: {client.phone_number} e: {client.email_address}")
                    return client
            else:
                if client.phone_number == search_for:
                    print(f"{client.first_name} {client.last_name} p: {client.phone_number} e: {client.email_address}")
                    return client
        print(f"No client found for {search_for}")
    else:
        print("No clients saved")

def update_client(clients: list):
    client_to_update = search_client(clients)

    if client_to_update:
        print(f"--- Update Client {client_to_update.first_name} {client_to_update.last_name} ---")
        print("What do you want to update for this client?")
        print(f"1. First name\n2. Last name\n3. Phone number\n4. Email address\n5. Notes\n6. Gender\n7. Date of birth\n8. Source\n9. Cancel")

        while True:
            option = input("Select option: ").strip()
            if option in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
            else:
                print("Invalid selection. Plese enter 1-9")
            
        if option == "1":
            new_first_name = input("Enter new first name: ")
            client_to_update.first_name = new_first_name
        elif option == "2":
            new_last_name = input("Enter new last name: ")
            client_to_update.last_name = new_last_name
        elif option == "3":
            new_phone_number = input("Enter new phone number: ")
            client_to_update.phone_number = new_phone_number
        elif option == "4":
            new_email_address = input("Enter new email address: ")
            client_to_update.email_address = new_email_address
        elif option == "5":
            return
        elif option == "6":
            new_gender = input("Enter new gender: ")
            client_to_update.gender = new_gender
        elif option == "7":
            new_dob = input("Enter new date of birth: ")
            client_to_update.dob = new_dob
        elif option == "8":
            new_source = input("Enter new source: ")
            client_to_update.source = new_source
        elif option == "9":
            print("Client update cancelled")
            return
        print(f"--- Client {client_to_update.first_name} {client_to_update.last_name} updated---")
        save_clients(clients)
        
    else:
        return
    
def delete_client(clients: list):
    client_to_delete = search_client(clients)

    if client_to_delete:
        print(f"--- Deleting client {client_to_delete.first_name} {client_to_delete.last_name} ---")
        clients.remove(client_to_delete)
        save_clients(clients)
        print(f"--- Client {client_to_delete.first_name} {client_to_delete.last_name} deleted---")


    







    

    


