from basemodel import BaseModel


class City(BaseModel):

    def __init__(self, id, name, area_code):
        super().__init__(id)
        self.name = name
        self.area_code = area_code

    def zip_code(self, area_code):
        if area_code.isnumeric():
            return True
        else:
            raise ValueError("Area code must be in numbers")
