from basemodel import BaseModel

class Reviews(BaseModel):

    def __int__(self, id, place, rating, feedback):
        super().__init__(id)
        self.place = place
        self.rating = rating
        self.feeback = feedback
