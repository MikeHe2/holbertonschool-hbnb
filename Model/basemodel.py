import uuid
from datetime import datetime
"""
The uuid import, this  module provides functionality for
generating UUIDs (Universally Unique Identifiers)

This module datetime provides classes for working with dates and times
"""


class BaseModel:
    """
    A base model class representing a generic model.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            created_at (datetime): The creation date and time of the model.
            updated_at (datetime): The last update date and time of the model.
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at


    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "Your ID is" + str(self.id)
