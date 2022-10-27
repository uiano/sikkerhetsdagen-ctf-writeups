<?php
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'nopeitsnotheretryharder');
define('DB_NAME', 'coolio');

try {
    //$con = new PDO("mysql:host=".DB_SERVER.";dbname=".DB_NAME, DB_USERNAME, DB_PASSWORD);
    $con = new PDO('sqlite:superhemmeligdb.db');
} catch (PDOException $e)
{
    exit("Kunne ikke koble til database, kontakt CTF adm...");
}
?>
