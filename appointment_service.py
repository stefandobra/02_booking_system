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

    appointment = Appointment(
        client_id = client_id,
        therapist_name = therapist_name,
        datetime = date_time,
        treatment = treatment
        )

    client_to_add_appt.upcoming_appts.append(appointment.__dict__)
    
    print(f"\nNew appointment added for {client_to_add_appt.first_name} {client_to_add_appt.last_name}")

    return appointment

def validate_datetime():
    while True:
        date_time_str = input("Please enter date and time for appointment (DD/MM/YYYY HH:mm): ")
        try:
            date_time = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
            if date_time > datetime.datetime.today():
                break
            else:
                print(f"\nInvalid date. Please enter future date!")
        except ValueError:
            print("Invalid date and time format. Please use (DD/MM/YYYY HH:mm).")
    return date_time.isoformat()

def view_all_appointments(appointments: list, clients: list):
    if not appointments:
        print("\nNo appointments saved")
        return
    print("\n--- Appointment list ---")
    i = 1
    for appt in appointments:
        client_id = appt.client_id
        date_time = datetime.datetime.strptime(appt.datetime, '%Y-%m-%dT%H:%M:%S')
        date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
        for client in clients:
            if client.id == client_id and date_time > datetime.datetime.today():
                print(f"{i}. {date_and_time} - {client.first_name} {client.last_name} - {appt.treatment} with {appt.therapist_name}")
                i += 1
                
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
    return 

def view_client_upcoming(appointments: list, clients: list):
    if not appointments:
        print("\nNo appointments saved")
        return []
    found = False
    i = 1
    client_appointments = []
    client_to_view = search_client(clients)
    if client_to_view:
        client_id = client_to_view.id
        for appt in appointments:
            date_time = datetime.datetime.strptime(appt.datetime, '%Y-%m-%dT%H:%M:%S')
            date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
            if client_id == appt.client_id and date_time > datetime.datetime.today():
                if not found:
                    print(f"\n--- Upcoming appointments for {client_to_view.first_name} {client_to_view.last_name} ---")
                found = True
                print(f"{i}. {date_and_time} - {client_to_view.first_name} {client_to_view.last_name} - {appt.treatment} with {appt.therapist_name}")
                i += 1
                client_appointments.append(appt)
        if not found:
            print(f"\n--- No upcoming appointments for {client_to_view.first_name} {client_to_view.last_name}")
    return client_appointments
        
def view_client_past(appointments: list, clients: list):
    if not appointments:
        print("\nNo appointments saved")
        return
    found = False
    i = 1
    client_to_view = search_client(clients)
    if client_to_view:
        client_id = client_to_view.id
        for appt in appointments:
            date_time = datetime.datetime.strptime(appt.datetime, '%Y-%m-%dT%H:%M:%S')
            date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
            if client_id == appt.client_id and date_time < datetime.datetime.today():
                if not found:
                    print(f"\n--- Past appointments for {client_to_view.first_name} {client_to_view.last_name} ---")
                found = True
                print(f"{i}. {date_and_time} - {client_to_view.first_name} {client_to_view.last_name} - {appt.treatment} with {appt.therapist_name}")
                i += 1
        if not found:
            print(f"\n--- No past appointments for {client_to_view.first_name} {client_to_view.last_name}")
            return


def cancel_appointment(appointments: list, clients: list):
    client_appointments = view_client_upcoming(appointments, clients)

    if client_appointments:
        selected_appointment = select_appointment(client_appointments)
        if selected_appointment:
            client_id = selected_appointment.client_id
            client = next((c for c in clients if c.id == client_id), None)
            if client:
                date_time = datetime.datetime.strptime(selected_appointment.datetime, '%Y-%m-%dT%H:%M:%S')
                date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
                print(f"\n{selected_appointment.treatment} with {selected_appointment.therapist_name} for {client.first_name} {client.last_name} on {date_and_time}")
            while True:
                confirmation = input(f"\nAre you sure you want to cancel this appointment Y/N?").strip().upper()
                if confirmation not in ["Y", "N"]:
                    print(f"\nPlease select Y/N")
                else:
                    break
            if confirmation == "Y" and client:
                appointments.remove(selected_appointment)
                appt_to_remove = next((appt for appt in client.upcoming_appts if appt["id"] == selected_appointment.id), None)
                if appt_to_remove: 
                    client.upcoming_appts.remove(appt_to_remove)
                print(f"\nAppointment cancelled")
            else:
                print("\nAppointment not cancelled!")
        
def select_appointment(appointments: list):
    selected_appointment = None
    if appointments:
        while True:
            appointment_to_cancel = input(f"\nPlease select appointment 1-{len(appointments)}: ").strip()
            try:
                option = int(appointment_to_cancel)
                if option > len(appointments):
                    print(f"\nInvalid selection. Please select from 1-{len(appointments)}!")
                else:
                    selected_appointment = appointments[option - 1]
                    break
            except ValueError:
                print(f"\nInvalid selection. Please use numbers from 1-{len(appointments)}: ")

    return selected_appointment

def reschedule_appointment(appointments: list, clients: list):
    client_appointments = view_client_upcoming(appointments, clients)
    if client_appointments:
        selected_appointment = select_appointment(client_appointments)
        if selected_appointment:
            client_id = selected_appointment.client_id
            client = next((c for c in clients if c.id == client_id), None)
            if client:
                date_time = datetime.datetime.strptime(selected_appointment.datetime, '%Y-%m-%dT%H:%M:%S')
                date_and_time = datetime.datetime.strftime(date_time, 'Day: %d/%m/%Y Time: %H:%M')
                print(f"\n{selected_appointment.treatment} with {selected_appointment.therapist_name} for {client.first_name} {client.last_name} on {date_and_time}")
            while True:
                confirmation = input(f"\nReschedule this appointment Y/N?").strip().upper()
                if confirmation not in ["Y", "N"]:
                    print(f"\nPlease select Y/N")
                else:
                    break
            if confirmation == "Y":
                selected_appointment.datetime = validate_datetime()
                print(f"\nAppointment rescheduled!")
            else:
                print("\nAppointment not rescheduled!")
