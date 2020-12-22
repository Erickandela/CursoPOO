from payment import Payment

class Card(Payment):
    date = str
    cvv = str

    def __init__(self, id, date, cvv):
        super().__init__(id)
        self.date = date
        self.cvv = cvv