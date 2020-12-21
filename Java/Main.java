class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("GLF342", new Account("Erick Candela", "ECAN32"));
        car.passenger = 3;
        car.printDataCar();

        Car car2 = new Car("NLH1034", new Account("Jovani Arana", "JARA04"));
        car2.passenger = 5;
        car2.printDataCar();
    }
}