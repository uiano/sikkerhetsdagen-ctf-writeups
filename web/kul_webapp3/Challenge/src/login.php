<?php
session_start();
require_once "database_config.php";
if(isset($_SESSION["user_id"]))
{
    header("location: index.php");
    exit;
}

if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_REQUEST['login']))
{
    $epost = $_REQUEST['epost'];
    $passord = $_REQUEST['passord'];
    $stmt = $con->prepare("SELECT id,passord FROM `brukere` WHERE epost=:epost LIMIT 1");
    $stmt->bindValue(':epost', $epost, PDO::PARAM_STR);
    $stmt->execute();
    $resultat = $stmt->fetch(PDO::FETCH_ASSOC);
    $passord = md5($passord);
    if($resultat["passord"] == $passord)
    {
        $_SESSION['user_id'] = $resultat["id"];
        header("location: index.php");
    }
    else
    {
        echo '<p class="text-danger">Feil brukernavn eller passord</p>';
    }
}
?>
<main role="main" class="inner cover">
    <form class="form-signin" action="index.php?page=login.php" method="POST">
        <h1 class="h3 mb-3 font-weight-normal">Vennligst logg inn</h1>
        <label for="epost" class="sr-only">Epost</label>
        <input name="epost" type="email" id="epost" class="form-control" placeholder="ola@example.com" required autofocus>
        <label for="passord" class="sr-only">Passord</label>
        <input name="passord" type=password" id="passord" class="form-control" placeholder="Passord" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit" name="login" value="login">Logg inn</button>
    </form>
</main>
<link rel="stylesheet" href="login.css">
