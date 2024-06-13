from .basemodel import BaseModel


"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class Users(BaseModel):
    """
    Represents a user in the system.
    """

    users = []

    @staticmethod
    def populate_user(user_instance):
        """
        Adds a user instance to the list of users.

        Args:
            user_instance (Users): The user instance to add.
        """
        if user_instance not in Users.users:
            Users.users.append(user_instance)

    @staticmethod
    def verify_email(email):
        """
        Verifies if an email is valid and not already registered.

        Args:
            email (str): The email to verify.

        Returns:
            bool: True if the email is valid and not already registered.

        Raises:
            ValueError: If the email is in an invalid format
            or already registered.
        """
        print("Verifying email:", email)
        print("Existing user emails:", [user.email for user in Users.users])
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        if any(user.email == email for user in Users.users):
            raise ValueError("This email is already registered")
        return True

    def __init__(self, id, created_at, updated_at, email, first_name,
                 last_name, host_id, place_id, review):
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
        super().__init__(id, created_at, updated_at)
        Users.verify_email(email)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []  # Place one-to-many relation
        Users.populate_user(self)
        self.host_id = host_id
        self.place_id = place_id
        self.review = review

    def not_own_review(self, host_id, place_id, review):
        self.host_id = host_id
        self.place_id = place_id
        self.review = review

        if host_id == place_id:
            raise ValueError("Owners cannot review their own place")
