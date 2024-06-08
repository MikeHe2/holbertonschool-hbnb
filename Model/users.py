from basemodel import BaseModel

class Users(BaseModel):

    def __init__(self, id, email, password, first_name, last_name):
        super().__init__(id)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = [] #Place ont-to-many relation


    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)


    def verify_email(self, email, users):#verifying if email is unique
        for user in users:
            if user.email == email:
                raise ValueError("This email is already logged")
        return True