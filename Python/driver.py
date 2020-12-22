from account import Account

class Driver(Account):
    matricula = str

    def __init__(self, name, document, matricula):
        super().__init__(name, document)
        self.matricula = matricula
