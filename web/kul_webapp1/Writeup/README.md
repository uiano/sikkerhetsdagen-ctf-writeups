# Taskname
> Author: Mx. Task

## Challenge

## Solution
Siden er sårbar for Local File Inclusion, benytt `php://filter/convert.base64-encode/resource=` for å hente ut kildekoden.
Graver enn litt rundt så finner enn `require_once "database_config.php";` i `login.php`.
Gjør enn da `php://filter/convert.base64-encode/resource=database_config.php` og dekoder, så får enn flagget som passordet til databasen.


