<main role="main" class="inner cover">
	<h1 class="cover-heading">Velkommen</h1>
	<p class="lead">Disse hashing funksjonene er helt magiske! Det er mulig å sende <a href="mailto:admin@minkulewebapp.finnesikke">epost</a> til meg, men jeg lover å ikke svare! :)</p>
    <?php
        session_start();
        if(isset($_SESSION["user_id"])){
            echo '<p>UIACTF{må være obs på strict vs loose comparison}</p>';
        }
    ?>
</main>
