from .basemodel import BaseModel


"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class Country:
    """
    Represents a country.

    Attributes:
        name (str): The name of the country.
    """

    def __init__(self, name):
        self.name = name
