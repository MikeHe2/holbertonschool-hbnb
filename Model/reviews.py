from .basemodel import BaseModel


"""
This import statement allows access to the BaseModel class
defined in the basemodel.py
filelocated in the same directory as the current Python script or module.

"""


class Reviews(BaseModel):
    """
    Represents a review for a place.

    Attributes:
        id (str): The unique identifier for the review.
        updated_at (datetime): The date and time when the
        review was last updated.
        place (str): The place associated with the review.
        rating (int): The rating given to the place (from 1 to 5).
        feedback (str): The feedback provided for the place.
    """

    def __init__(self, id, updated_at, place, rating, feedback):
        """
        Initializes a new instance of the Reviews class.

        Args:
            id (str): The unique identifier for the review.
            updated_at (datetime): The date and time when the
            review was last updated.
            place (str): The place associated with the review.
            rating (int): The rating given to the place (from 1 to 5).
            feedback (str): The feedback provided for the place.
        """
        super().__init__(id, updated_at)
        self.place = place
        self.rating = rating
        self.feedback = feedback

    def add_rating(self, rating):
        """
        Adds a rating to the review.

        Args:
            rating (int): The rating to be added.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Ratings must be from 1 to 5")
