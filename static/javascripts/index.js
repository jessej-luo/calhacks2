$(document).ready(function() {
	$('a.type-dropdown').click(function(e) {
		e.preventDefault();
		var type = $(this).text();
		$('.business-type').text(type);
	});

	var calculateChars = function() {
		var used = $('.review-text').val().length;
		var left = 5000 - used;
		$('.chars-left').text(left);
		if (left < 0) {
			$('.chars-left').addClass('negative');
		} else {
			$('.chars-left').removeClass('negative');
		}
	}

	$('.review-text').on('keyup', function() {
		calculateChars();
	});

	calculateChars();

	$('.submit-review').click(function() {
		if ($('.review-text').val().length <= 5000) {
			var review = $('.review-text').val();
			$.post({
				
			})
		}
	});
});