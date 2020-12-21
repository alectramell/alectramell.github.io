function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function goTab(url) {

	var win = window.open(url, '_blank');
	win.focus();
}

function gotoFacebook() {

	goTab('https://www.facebook.com/tramelldev');
}
