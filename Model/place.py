from basemodel import BaseModel

class Place(BaseModel):

    def __init__(self, id, name, description, address, latitude, longitude, host, price_per_night, max_guests):
        super().__init__(id)
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude 
        self.host = host
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = [] #Amenity one-to-many relation


    def add_amenity(self, amenity):
        self.amenities.append(amenity)


    def remove_amenity(self, amenity):
        self.amenities.remove(amenity)


    def new_host(self, new_host):#verifying if Place has only one host
        if self.host is not None:
            raise ValueError("This place already has a host")
        self.host = new_host
