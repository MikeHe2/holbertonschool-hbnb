from .basemodel import BaseModel

"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class Amenities(BaseModel):
    """
    Represents amenities for a place.
    """

    def __init__(self, id, number_of_rooms, bathrooms, Wifi, pools):
        """
        Initializes a new instance of the Amenities class.

        Args:
            id (str): The ID of the amenities.
            number_of_rooms (int): The number of rooms in the place.
            bathrooms (int): The number of bathrooms in the place.
            Wifi (bool): Indicates if the place has WiFi.
            pools (int): The number of pools in the place.
        """
        super().__init__(id)
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.Wifi = Wifi
        self.pools = pools
        self.places = []  # Place one-to-many relation

    def add_place(self, place):
        """
        Adds a place to the list of places associated with the amenities.

        Args:
            place (Place): The place to add.
        """
        self.places.append(place)

    def remove_place(self, place):
        """
        Removes a place from the list of places associated with the amenities.

        Args:
            place (Place): The place to remove.
        """
        self.places.remove(place)
