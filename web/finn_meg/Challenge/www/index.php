<?php
  if (isset($_GET['hent_side'])) {
	$f_contents = file("../random.txt"); 
    $line = $f_contents[rand(0, count($f_contents) - 1)];
	header("Location: /" . $line);
  }
?>

<html>
<body>
<div style="text-align: center">
<img style="display: inline-block;max-width: 50%;max-height: 50%" src="finnmeg.jpg">

<form action="index.php" method="get">
  <input type="hidden" name="hent_side" value="true">
  <input type="submit" value="Hent en tilfeldig side!">
</form>

</div>
</body>
</html>