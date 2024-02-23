from uuid import uuid4
from uuid import UUID, uuid4


class CardId:
    @staticmethod
    def generate() -> UUID:
        return uuid4()
