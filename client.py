import uuid

class Client:
    def __init__(self, first_name, last_name, phone_number, email_address, notes=None, intake_forms=None, upcoming_appts=None, past_appts=None, gender=None, dob=None, source=None, id=None
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.notes = notes
        self.intake_forms = intake_forms
        self.upcoming_appts = upcoming_appts
        self.past_appts = past_appts
        self.gender = gender
        self.dob = dob
        self.source = source
        self.id = id if id else uuid.uuid4().hex

# client1 = Client("Stefan", "Dobra", "07710898393", "dobrastefan@gmail.com")
# client2 = Client("Cristina", "Dobra", "0771234567", "xxxxxx@gmail.com", gender="F")

# print(client1.id)
# print(client2.id)


# print(client1.__dict__)

