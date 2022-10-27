<?php session_start() ?>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body class="text-center">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <ul class="navbar-nav">
            <li class="nav-item">
            <?php
            if(isset($_SESSION["user_id"])) {
                echo '<a class="nav-link" href="?page=logout.php">Logout<a/>';
            } else {
                echo '<a class="nav-link" href="?page=login.php">Login<a/>';
            }
            ?>
            </li>
        </ul>
    </nav>
    <?php
    $allowed = array('home.php','login.php','logout.php');
    if(isset($_REQUEST["page"]) && in_array($_REQUEST["page"], $allowed)){
        include($_REQUEST["page"]);
    }
    else {
        include("home.php");
    }
    ?>
</body>
