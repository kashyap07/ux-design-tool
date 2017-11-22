$(document).ready(function() {
	$("*").draggable();
	$("*").droppable();
    $("*").draggable();
	$("*").droppable();

	$('body').append($('<button class="btn btn-primary" id="screenshot-btn">Take Screenshot</button>'));

	var takeScreenShot = function() {
		console.log('aaaaaa');
		html2canvas(document.body, {
			onrendered: function (canvas) {
				 var tempcanvas = document.createElement('canvas');
				tempcanvas.width = $(window).width();
				tempcanvas.height = $(window).height();
				var context = tempcanvas.getContext('2d');
				context.drawImage(canvas,0,0);
				var link = document.createElement("a");
				link.href = tempcanvas.toDataURL('image/jpg');   //function blocks CORS
				link.download = 'screenshot'+ window.location.href+'.jpg';
				link.click();
			}
		});
	}
});