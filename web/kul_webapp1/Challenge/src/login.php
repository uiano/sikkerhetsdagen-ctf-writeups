<?php
session_start();
require_once "database_config.php";
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true)
{
    header("location: index.php");
    exit;
}

if($_SERVER["REQUEST_METHOD"] == "POST")
{
    // todo: Process the login request
    echo '<p class="text-danger">Login feature currently not working. Try again later.</p>';
}
?>
<main role="main" class="inner cover">
    <form class="form-signin" action="index.php?page=login.php" method="POST">
        <h1 class="h3 mb-3 font-weight-normal">Vennligst logg inn</h1>
        <label for="epost" class="sr-only">Epost</label>
        <input type="email" id="epost" class="form-control" placeholder="ola@example.com" required autofocus>
        <label for="passord" class="sr-only">Passord</label>
        <input type=password" id="passord" class="form-control" placeholder="Passord" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Logg inn</button>
    </form>
</main>
<link rel="stylesheet" href="login.css">
