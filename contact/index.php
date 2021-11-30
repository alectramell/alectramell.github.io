<?php
	$xtitle = 'Tramell Software Development (r)';
	$email = '';
?>
<html class="mobile">
<head>
<title>
<?php echo $xtitle; ?>
</title>
<meta name="viewport" content="width=800">
</head>
<body onload="toggleZoomScreen();">

<style type="text/css" rel="stylesheet">
body, html {

	background:#050505;
	width:100%;
	height:100%;
	overflow:hidden;
	cursor:arrow;
}

.mobile, html {

	background:#050505;
	background-size:cover;
	width:100%;
	height:100%;
	overflow:hidden;
	cursor:arrow;
	color:#000000;
}

@font-face {

	font-family:'Josefin';
	src:url('josefin.otf');
}

.plainText {

	font-family:Josefin;
	font-size:32px;
	font-weight:bold;
	color:#ffffff;
}
</style>

<script type="text/javascript">
function toggleZoomScreen() {

	document.body.style.zoom = "290%";
}
</script>

<br />

<center>
<form action="complete.php" method="post">
<font class="plainText" style="position:relative;text-align:center;">Email </font>
<br />
<input type="text" name="email" value="<?php echo $email;?>">
<br />
<br />
<input type="submit" value="signup">
</form>
</center>

</body>
</html>