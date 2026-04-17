from client import Client
from client_service import add_client, save_clients, load_clients, update_client, search_client, view_clients, delete_client
from appointment import Appointment
from appointment_service import save_appointments, load_appointments, add_appointment, view_all_appointments

clients = []

def display_menu():
    print(f"\n--- Booking System ---")
    print("1. View clients")
    print("2. Add client")
    print("3. Search client")
    print("4. Update client")
    print("5. Delete client")
    print("6. Add appointment")
    print("7. View all appointments")
    print("0. Exit")

        
clients = load_clients()
appointments = load_appointments()

while True:

    display_menu()
    option = input("Please select an option: ")

    if option == "1":
        view_clients(clients)
    elif option == "2":
        new_client = add_client()
        clients.append(new_client)
        print(f"\nNew client ({new_client.first_name} {new_client.last_name}) added succesfully!")
    elif option == "3":
        search_client(clients)
    elif option == "4":
        update_client(clients)
    elif option == "5":
        delete_client(clients)
    elif option == "6":
        new_appointment = add_appointment(clients)
        if new_appointment:
            appointments.append(new_appointment)
        else:
            print("\nClient not found")  
    elif option == "7":
        view_all_appointments(appointments, clients)
    elif option == "0":
        print("Have a good day!")
        save_clients(clients)
        save_appointments(appointments)
        break

