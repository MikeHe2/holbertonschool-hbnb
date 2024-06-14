from .basemodel import BaseModel


"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class Place(BaseModel):
    """
    Represents a place in the application.
    """

    def __init__(self, id, updated_at, name, place, description, address,
                 latitude, longitude, host, price_per_night, max_guests):
        """
        Initializes a new instance of the Place class.

        Args:
            id (str): The unique identifier of the place.
            updated_at (datetime): The date and time when the
            place was last updated.
            name (str): The name of the place.
            place (str): The type of place (e.g., apartment, house, etc.).
            description (str): A description of the place.
            address (str): The address of the place.
            latitude (float): The latitude coordinate of the place.
            longitude (float): The longitude coordinate of the place.
            host (str): The host of the place.
            price_per_night (float): The price per night to stay at the place.
            max_guests (int): The maximum number of guests
            allowed in the place.
        """
        super().__init__(id, updated_at)
        self.name = name
        self.place = place
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []  # Amenity one-to-many relation

    def add_amenity(self, amenity):
        """
        Adds an amenity to the place.

        Args:
            amenity (str): The amenity to add.
        """
        self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        """
        Removes an amenity from the place.

        Args:
            amenity (str): The amenity to remove.
        """
        self.amenities.remove(amenity)

    def update_amenity(self, past_amenity, new_amenity):
        """
        Updates an amenity in the place.

        Args:
            past_amenity (str): The amenity to update.
            new_amenity (str): The new amenity value.

        Raises:
            ValueError: If the past_amenity is not found
            in the place's amenities list.
        """
        if past_amenity in self.amenities:
            i = self.amenities.index(past_amenity)
            self.amenities[i] = new_amenity
        else:
            raise ValueError(f"{past_amenity} not found")

    def new_host(self, new_host):
        """
        Sets a new host for the place.

        Args:
            new_host (str): The new host to set.

        Raises:
            ValueError: If the place already has a host.
        """
        if self.host is not None:
            raise ValueError("This place already has a host")
        self.host = new_host

    def delete(self):
        """
        Deletes the place by setting the host to None.
        """
        self.host = None
