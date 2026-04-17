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
        print("No saved data found, starting fresh")
        return []
    
    except json.JSONDecodeError as error:
        print("Invalid JSON syntax:", error)
        return []

def add_appointment(clients, appointments):
    client_to_add_appt = search_client(clients)

    if not client_to_add_appt:
        return

    print(f"\n--- Add appointment for client {client_to_add_appt.first_name} {client_to_add_appt.last_name} ---")
    client_id = client_to_add_appt.id
    therapist_name = input("Please enter therapist name: ")
    date_time = validate_datetime()
    treatment = input("Please enter treatment required: ")
    
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





    