function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function offSwitch() {

	alert('This Function is Temporarily Disabled.');
}

function goTab(url) {

	var win = window.open(url, '_blank');
	win.focus();
}

function gotoFacebook() {

	goTab('https://www.facebook.com/tramelldev');
}

function winStoreOpen() {

	parent.location = 'https://alectramell.github.io/winstore.html';
}

function macStoreOpen() {

	parent.location = 'https://alectramell.github.io/macstore.html';
}

function goHome() {

	parent.location = 'https://alectramell.github.io/index.html';
}
