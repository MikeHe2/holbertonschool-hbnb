from .basemodel import BaseModel


"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class City(BaseModel):
    """
    A class representing a city.

    Attributes:
        id (str): The unique identifier of the city.
        name (str): The name of the city.
        area_code (str): The area code of the city.
    """

    def __init__(self, id, name, area_code):
        """
        Initializes a new instance of the City class.

        Args:
            id (str): The unique identifier of the city.
            name (str): The name of the city.
            area_code (str): The area code of the city.
        """
        super().__init__(id)
        self.name = name
        self.area_code = area_code

    def zip_code(self, area_code):
        """
        Checks if the given area code is numeric.

        Args:
            area_code (str): The area code to be checked.

        Returns:
            bool: True if the area code is numeric, False otherwise.

        Raises:
            ValueError: If the area code is not numeric.
        """
        if area_code.isnumeric():
            return True
        else:
            raise ValueError("Area code must be in numbers")
