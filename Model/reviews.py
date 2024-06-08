from basemodel import BaseModel

class Reviews(BaseModel):

    def __init__(self, id, place, rating, feedback):
        super().__init__(id)
        self.place = place
        self.rating = rating
        self.feedback = feedback

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Ratings must be from 1 to 5")
