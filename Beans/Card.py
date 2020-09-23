
class Card():
    def __init__(self,type,suit):
        self.suit=suit
        self.type=type
    def __str__(self):
        return f"({self.suit},{self.type})"