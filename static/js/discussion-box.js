function expand(obj) {
	if (obj.className == 'btn-expand-clicked btn-expand') {
		obj.className = 'btn-expand';
	} else {
		obj.className = 'btn-expand-clicked btn-expand';
		setTimeout(function () {
				$('.discussion-box').removeClass('hidden');
				$('.discussion-qs').removeClass('hidden');
		}, 300);
	}
}

function closeBox() {
	$('.discussion-box').addClass('hidden');
	$('.discussion-qs').addClass('hidden');
	$('.btn-expand-clicked.btn-expand').removeClass('btn-expand-clicked');
}