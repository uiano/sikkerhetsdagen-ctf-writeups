# Taskname
> Author: Mx. Task

## Challenge

## Solution

Her er det også 2 muligheter, den enkleste er å observere at det er en wordpress applikasjon og se på login forespørselen som gir en vellykket pålogging. Her må enn være obs på at angriper skrev feil første gang, og manglet 1 tegn i passordet. Det vellykkede inneholder følgende POST data.
```
HTML Form URL Encoded: application/x-www-form-urlencoded
    Form item: "log" = "admin"
    Form item: "pwd" = "qwertyui"
    Form item: "wp-submit" = "Log In"
    Form item: "redirect_to" = "http://kulebloggen.uiactf/wp-admin/"
    Form item: "testcookie" = "1"
```

Alternativt er å se på alle bruteforce forsøkene mot `/xmlrpc.php`, der angriper angir brukernavn og passord samtidig som enn etterspør `wp.getPosts`, ved feil brukernavn/passord får enn responsen `Incorrect username or password.`, samt at den vellykkede påloggingen vil ha en vesentlig større respons enn de andre.
