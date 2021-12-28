function goFullScreen() {

	document.documentElement.requestFullscreen()
}

function sendDArequest() {

    window.open('mailto:alectramell@gmail.com?subject=(TSD) Data Analyst Request&body=This is a potential Data Analyst request.%0d%0a%0d%0aTramell Software Development will reply to the email sending this request within a 12 hour business timeframe. If you would like to add any other information to the request (contact info, confirmation requirements, agent preferences, etc.) please add the information below before sending the request..%0d%0a');
}

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

function gotoFacebookMob() {

	goTab('https://m.facebook.com/tramelldev');
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

	parent.location = 'https://alectramell.github.io';
}

function offNote() {

	setTimeout(function(){alert('This Page is Temporarily Not Available.')}, 1500);
	setTimeout(function(){goHome()}, 1500);
}

function callUS() {

	parent.location = 'tel:8018931187';
}

function emailUS() {

	parent.location = 'mailto:alectramell@gmail.com';
}

function toggleZoomScreen() {

	document.body.style.zoom = "125%";
}
