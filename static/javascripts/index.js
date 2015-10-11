$(document).ready(function() {
	$('a.type-dropdown').click(function(e) {
		e.preventDefault();
		var type = $(this).text();
		$('.business-type').text(type);
	});

	
    var $container = $('.container-back');
    var backgrounds = [
      'url(static/images/restaurant1.jpg)'];
    var current = 0;

    function nextBackground() {
        $container.css(
            'background-image',
        backgrounds[current = ++current % backgrounds.length]);

        setTimeout(nextBackground, 5000);
    }
    setTimeout(nextBackground, 5000);
    $container.css('background', backgrounds[0]);

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

	var setCog = function() {
		$('.submit-section').html('<i class="fa fa-cog fa-spin"></i>');
		$('.submit-section').addClass('cog');
	}

	$('.submit-review').bind('click', function() {
		$.ajaxSetup({
		   beforeSend: setCog
		});
		if ($('.review-text').val().length <= 5000) {
			var review = $('.review-text').val();
			$.post(
				'/review',
				{stars: 0, review: review}
			).done(function(res) {
				var stars = parseInt(res);
				$('.submit-review').unbind('click');
				$('.submit-section').after(new EJS({url: 'static/stars.ejs'}).render());
				var $predicted = $('.predicted');
				$predicted.each(function(i) {
					if (i < stars) {
						$(this).removeClass('fa-star-o').addClass('fa-star');
					}
				});
				$('.submit-section').remove();
				$('.review-text').attr('disabled', true);
				$('.business').attr('disabled', true);
			}).fail(function(response) {
				$('.submit-review').unbind('click');
				$('.submit-section').after('<div>Fail</div>');
			});
		}
	});

	$(document).on('click', '.submit-stars', function() {
		if ($('.review-text').val().length <= 5000) {
			var review = $('.review-text').val();
			var stars = $('.star-select.fa-star').length;
			$.post(
				'/review_add',
				{stars: stars, review: review}
			).done(function(res) {
				$('.submit-stars').unbind('click');
				$('.stars-section').after("<div>Thank you!</div>");
			}).fail(function(response) {
				$('.submit-review').unbind('click');
				$('.stars-section').after('<div>Fail</div>');
			});
		}
	});

	$('.form-main').on({
	    mouseenter: function(){
	    	$(this).removeClass('fa-star-o').addClass('fa-star');
	        $(this).prevAll().removeClass('fa-star-o').addClass('fa-star');
	    },
	    mouseleave: function(){
	    	if ($(this).nextAll('.clicked').length === 0 && !$(this).hasClass('clicked')) {
		    	$(this).removeClass('fa-star').addClass('fa-star-o');
		    	setTimeout(function () {
		            if ($(".star-select:hover").length === 0 && $(".star-select.clicked").length === 0) {
		            	$('.star-select').removeClass('fa-star').addClass('fa-star-o');
		            }
	        	}, 100);  
        	}   
	    }
	}, '.star-select');

	$('.form-main').on('click', '.star-select', function() {
		$(this).siblings().removeClass('clicked');
		$(this).addClass('clicked');
		$(this).nextAll().removeClass('fa-star').addClass('fa-star-o');
		$(this).removeClass('fa-star-o').addClass('fa-star');
	    $(this).prevAll().removeClass('fa-star-o').addClass('fa-star');
	});
});