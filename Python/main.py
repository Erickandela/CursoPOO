from car import Car
from account import Account
from uberX import UberX




if __name__ == '__main__':
    print('Hola Mundo')
    car = Car("MHL3241", Account("Erick Candela", "Licencia"))
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("POK6532", Account("Kirin Koron", "INE"))
    print(vars(car2))
    print(vars(car2.driver))

    uberX = UberX("GPF3456", Account("Erick Arana", "INE"), "Dodge", "RAM")
    print(vars(uberX))
    print(vars(uberX.driver))