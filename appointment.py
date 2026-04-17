import uuid

class Appointment:
    def __init__(self, id=None, client_id=None, therapist_name=None, datetime=None, treatment=None
                 ):
        self.id = id if id else uuid.uuid4().hex
        self.client_id = client_id
        self.therapist_name = therapist_name
        self.datetime = datetime
        self.treatment = treatment