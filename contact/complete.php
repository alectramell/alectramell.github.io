<?php
	$xtitle = 'Tramell Software Development (r)';
	$xmail = $_POST["email"];
	$hexmail = bin2hex("{$xmail}");
	$unhexmail = hex2bin("{$hexmail}");
	$hashmail = md5("{$xmail}");
	$reurl = 'https://alectramell.github.io';
?>
<html>
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
	font-size:24px;
	font-weight:bold;
	color:#ffffff;
}
</style>

<script type="text/javascript">
function toggleZoomScreen() {

	document.body.style.zoom = "290%";
}
</script>

<?php

	if (strpos(file_get_contents("xdata.txt"),$hashmail) !== false) {

		$zout = 'Umm..';
		$xout = 'That email already exists..';
		$reurl = 'https://tramellsoftware.000webhostapp.com/';

	} else {

		$zout = 'Success!';
		$xout = 'Please make sure to check '.$xmail.' for updates!';
		$reurl = 'https://alectramell.github.io';

		$dataLog = fopen("xdata.txt", "a") or die("Unable to Submit Data!");
		fwrite($dataLog, "{$hashmail}\n");
		fclose($dataLog);
	}
?>

<br />

<center>
<font class="plainText" style="position:relative;font-size:32;text-align:center;"><?php echo $zout; ?></font>
</center>
<center>
<font class="plainText" style="position:relative;text-align:center;"><?php echo $xout; ?></font>
</center>

<script type="text/javascript">
	setTimeout(function() {parent.location = "<?php echo $reurl; ?>"}, 8000);
</script>

</body>
</html>