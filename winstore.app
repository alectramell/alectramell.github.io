<hta:application

        id="winstore"
        version="1.0"
        border="none"
        innerborder="no"
        caption="no"
        sysmenu="no"
        maximizebutton="no"
        minimizebutton="no"
        icon="img/favicon.ico"
        scroll="no"
        scrollflat="yes"
        singleinstance="yes"
        showintaskbar="yes"
        contextmenu="no"
        selection="no"
	navigable="yes"
/>
<html>
<head>
<title>
Tramell Software Development (r)
</title>
</head>
<body>

<style type="text/css">

body, html {

	background:url(https://alectramell.github.io/img/winbg.png);
	background-size:cover;
	overflow:hidden;
	cursor:auto;
}

#exitButton {

	position:absolute;
	top:5px;
	left:6px;
	font-family:Arial;
	font-size:17px;
	text-decoration:bold;
	color:#c4c4c4;
	cursor:pointer;
}

#infoText {

	position:absolute;
	top:100px;
	padding:50px;
	font-family:Arial;
	font-size:24px;
	text-decoration:bold;
	color:#4c4c4c;
	cursor:none;
}

</style>

<script type="text/javascript">

	window.resizeTo(650,450);
	window.moveTo(320,50);

	function exitApp() {

		setTimeout(function(){window.close();}, 500);
	}

</script>

<font id="exitButton" onclick="exitApp();">close</font>

<br />

<font id="infoText">Sorry.. We're updating our Windows App-Store.. Please check back soon!</font>

</body>
</html>