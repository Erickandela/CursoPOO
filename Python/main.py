from car import Car
from account import Account


if __name__ == '__main__':
    print('Hola Mundo')
    car = Car("MHL3241", Account("Erick Candela", "Licencia"))
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("POK6532", Account("Kirin Koron", "INE"))
    print(vars(car2))
    print(vars(car2.driver))