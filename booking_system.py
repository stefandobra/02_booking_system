from client import Client
from client_service import add_client
import json

clients = []

def display_menu():
    print(f"\n--- Booking System ---")
    print("1. View clients")
    print("2. Add client")
    print("3. Update client")
    print("4. Delete client")
    print("0. Exit")

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
        
        return clients
    
    except json.JSONDecodeError as error:
        print("Invalid JSON syntax:", error)
        return clients
        
clients = load_clients()

while True:

    display_menu()
    option = input("Please select an option: ")

    if option == "1":
        continue
    elif option == "2":
        new_client = add_client()
        clients.append(new_client)
        print(f"\nNew client ({new_client.first_name} {new_client.last_name}) added succesfully!")
    elif option == "3":
        continue
    elif option == "4":
        continue
    elif option == "0":
        print("Have a good day!")
        save_clients(clients)
        break

