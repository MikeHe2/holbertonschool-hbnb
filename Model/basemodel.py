import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "Your ID is" + str(self.id)
