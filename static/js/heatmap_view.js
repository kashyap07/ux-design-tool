// create instance
var heatmapInstance = h337.create({
	container: document.querySelector('.heatmap'),
	radius: 40
});

document.querySelector('.demo-wrapper').onclick = function(ev) {
	heatmapInstance.addData({
		x: ev.layerX,
		y: ev.layerY,
		value: 1
	});
};

var heatmap = h337.create({
	container:  document.getElementById('chartContainer')
});