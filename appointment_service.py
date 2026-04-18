from appointment import Appointment
import json
from client_service import search_client
import datetime

def save_appointments(appointments: list): 
    appointments_dict = []
    for appointment in appointments:
        appointments_dict.append(appointment.__dict__) # using __dict__ to return Appointment attributes as a dictionary

    appointments_to_save = {
        "appointments": appointments_dict
    }

    with open ("appointments.json", "w") as file:
        json.dump(appointments_to_save, file)

def load_appointments():
    try:
        appointments_from_file = []
        with open ("appointments.json", "r") as file:
            appointments_to_load = json.load(file)

        for appointment in appointments_to_load["appointments"]:
            appointments_from_file.append(Appointment(**appointment)) # use **appointment to unpack dictionary into Appointment object
        
        return appointments_from_file
    
    except FileNotFoundError:
        print("No saved appointments, starting fresh")
        return []
    
    except json.JSONDecodeError as error:
        print("Invalid JSON syntax:", error)
        return []

def add_appointment(clients: list):
    client_to_add_appt = search_client(clients)

    if not client_to_add_appt:
        return

    print(f"\n--- Add appointment for client {client_to_add_appt.first_name} {client_to_add_appt.last_name} ---")
    client_id = client_to_add_appt.id
    therapist_name = input("Please enter therapist name: ")
    date_time = validate_datetime()
    treatment = input("Please enter treatment required: ")
    
    print(f"\nNew appointment added for {client_to_add_appt.first_name} {client_to_add_appt.last_name}")


    return Appointment(
        client_id = client_id,
        therapist_name = therapist_name,
        datetime = date_time,
        treatment = treatment
        )

def validate_datetime():
    while True:
        date_time_str = input("Please enter date and time for appointment (DD/MM/YYYY HH:mm): ")
        try:
            date_time = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
            break
        except ValueError:
            print("Invalid date and time format. Please use (DD/MM/YYYY HH:mm).")
    return date_time.isoformat()

def view_all_appointments(appointments: list, clients: list):
    if not appointments:
        print("\nNo appointments saved")
        return
    print("\n--- Appointment list ---")
    for i, appt in enumerate(appointments, start=1):
        client_id = appt.client_id
        date_time = datetime.datetime.strptime(appt.datetime, '%Y-%m-%dT%H:%M:%S')
        date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
        for client in clients:
            if client.id == client_id:
                print(f"{i}. {date_and_time} - {client.first_name} {client.last_name} - {appt.treatment} with {appt.therapist_name}")

def view_client_appointments(appointments: list, clients: list):
    if not appointments:
        print("\nNo appointments saved")
        return
    found = False
    i = 1
    client_to_view = search_client(clients)
    if client_to_view:
        client_id = client_to_view.id
        for appt in appointments:
            if client_id == appt.client_id:
                if not found:
                    print(f"\n--- Appointments for {client_to_view.first_name} {client_to_view.last_name} ---") 
                found = True
                date_time = datetime.datetime.strptime(appt.datetime, '%Y-%m-%dT%H:%M:%S')
                date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
                print(f"{i}. {date_and_time} - {client_to_view.first_name} {client_to_view.last_name} - {appt.treatment} with {appt.therapist_name}")
                i += 1
        if not found:
            print(f"\n--- No appointments for {client_to_view.first_name} {client_to_view.last_name}")




    