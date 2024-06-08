from basemodel import BaseModel


class Amenities(BaseModel):

    def __init__(self, id, number_of_rooms, bathrooms, Wifi, pools):
        super().__init__(id)
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.Wifi = Wifi
        self.pools = pools
        self.places = []#Place one-to-many relation

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)
