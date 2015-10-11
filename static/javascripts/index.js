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

	$('.submit-review').bind('click', function() {
		if ($('.review-text').val().length <= 5000) {
			var review = $('.review-text').val();
			$.post(
				'/',
				{stars: 0, review: review}
			).done(function(res) {
				$('.submit-review').unbind('click');
				$('.submit-section').after(new EJS({url: 'static/stars.ejs'}).render());
			}).fail(function(response) {
				$('.submit-review').unbind('click');
				//var res = $.parseJSON(response.responseText);
				$('.submit-section').after(new EJS({url: 'static/stars.ejs'}).render());
			});
		}
	});

	$('.form-main').on({
	    mouseenter: function(){
	    	$(this).removeClass('fa-star-o').addClass('fa-star');
	        $(this).prevAll().removeClass('fa-star-o').addClass('fa-star');
	    },
	    mouseleave: function(){
	    	$(this).removeClass('fa-star').addClass('fa-star-o');
	    	setTimeout(function () {
	            if ($(".star-select:hover").length === 0) {
	            	$('.star-select').removeClass('fa-star').addClass('fa-star-o');
	            }
        	}, 100);     
	    }
	}, '.star-select');
});