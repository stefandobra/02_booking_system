from appointment import Appointment
import json

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
    