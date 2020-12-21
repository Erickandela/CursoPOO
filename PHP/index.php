<?php
require_once('car.php');
require_once('uberX.php');
require_once('uberPool.php');
require_once('account.php');

$uberX = new UberX("NHL9543 ", new Account("Erick Candela", "Licencia A"), "Mitsubishi", "Lancer");
$uberX->printDataCar();

$uberPool = new UberPool("PGF9030", new Account("Jovani Arana", "Licencia B"), "Ferrari", "Spider");
$uberPool->printDataCar();


?>