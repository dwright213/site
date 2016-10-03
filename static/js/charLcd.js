$( document ).ready(function() {
	var
	dPixels = [4,9,11,12,14,15,18,19,20,24,25,29,31,32,33,34],
	aPixels = [11,12,13,19,21,22,23,24,25,29,31,32,33,34],
	nPixels = [10,12,13,15,16,19,20,24,25,29,30,34],
	clearPixels = [],
	char1 = $('.character-1 > div'),
	char2 = $('.character-2 > div'),
	char3 = $('.character-3 > div');

	function pushArray(pixels, character) {

		// clear it out
		for (var i = character.length - 1; i >= 0; i--) {
			$(character[i]).removeClass('pixel-on');
		}

		// and push the new pixels in
		for (var i = character.length - 1; i >= 0; i--) {
			if (pixels.indexOf(i) > -1) {
				$(character[i]).addClass('pixel-on');
			}
		}
	}

	pushArray(dPixels, char1);
	pushArray(aPixels, char2);
	pushArray(nPixels, char3);

	$('a.clickme').on('click',function(){
		pushArray(dPixels, char1);
	});

	$('a.clickme2').on('click',function(){
		pushArray(aPixels, char2);
	});

	$('a.clickme3').on('click',function(){
		pushArray(nPixels, char3);
	});

	$('a.clickme4').on('click',function(){
		pushArray(clearPixels, char1);
		pushArray(clearPixels, char2);
		pushArray(clearPixels, char3);
	});
});

