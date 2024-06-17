from .basemodel import BaseModel
from Persistence.data_manager import DataManager

"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class User(BaseModel):
    """
    Represents a user in the system.
    """
    users = []

    def __init__(self, email, first_name, last_name):
        """
        Initializes a new user instance.

        Args:
            id (str): The user ID.
            updated_at (datetime): The date and time of the last update.
            email (str): The user's email.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        User.populate_user(self)

    @staticmethod
    def populate_user(user_instance):
        """
        Adds a user instance to the list of users.

        Args:
            user_instance (Users): The user instance to add.
        """
        if user_instance not in User.users:
            User.users.append(user_instance)


    @staticmethod
    def email_exists(email):
        """
        Checks if an email is already registered.
        """
        data_manager = DataManager()  # Crear una instancia de DataManager
        all_users = data_manager.get_all('User')  # Obtener todos los usuarios
        return any(user['email'] == email for user in all_users)


    def not_own_review(self, host_id, place_id, review):
        self.host_id = host_id
        self.place_id = place_id
        self.review = review

        if host_id == place_id:
            raise ValueError("Owners cannot review their own place")
