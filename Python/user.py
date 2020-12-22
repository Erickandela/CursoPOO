from account import Account

class User(Account):
    paymentType = str

    def __init__(self, name, document, paymentType):
        super().__init__(name, document)
        self.paymentType = paymentType