class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("GLF342", new Account("Erick Candela", "ECAN32"), "Dodge", "Charger");
        uberX.setPassenger(3);
        uberX.printDataCar();

        // Car car2 = new Car("NLH1034", new Account("Jovani Arana", "JARA04"));
        // car2.passenger = 5;
        // car2.printDataCar();
    }
}