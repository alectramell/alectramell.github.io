function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

document.addEventListener('load', reLoad(5000););
