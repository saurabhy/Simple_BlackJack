
class CardListEmpty(Exception):
    def __init__(self):
        super().__init__('There is no cards left')