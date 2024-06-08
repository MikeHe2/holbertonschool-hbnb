from basemodel import BaseModel

class Users(BaseModel):

    def __init__(self, id, email, password, first_name, last_name):
        super().__init__(id)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = [] #here we are creating the relation one-to-many


    def add_place(self, place):
        if place.host is not None:
            raise ValueError("Place already has a host")
        self.places.append(place)
        place.host = self

        
    @staticmethod  
    def verify_email(email, users):
        for user in users:
            if user.email == email:
                return False
        return True
