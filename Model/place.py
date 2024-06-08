from basemodel import BaseModel

class Place(BaseModel):

    def __init__(self, id, name, description, address, latitude, longitude, host, price_per_night, max_guests, review):
        super().__init__(id)
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude 
        self.host = None
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = [] #one-to-many relation