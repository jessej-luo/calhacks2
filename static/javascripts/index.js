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

	$('.submit-review').bind('click', function() {
		if ($('.review-text').val().length <= 5000) {
			var review = $('.review-text').val();
			$.post(
				'/review',
				{stars: 0, review: review}
			).done(function(res) {
				$('.submit-review').unbind('click');
				$('.submit-section').after(new EJS({url: 'static/stars.ejs'}).render());
				var $predicted = $('.predicted');
				for (var i = 0; i < res; i++) {
					$predicted[i].removeClass('fa-star-o').addClass('fa-star');
				}
			}).fail(function(response) {
				$('.submit-review').unbind('click');
				$('.submit-section').after('<div>Fail</div>');
			});
		}
	});

	$('.form-main').on({
	    mouseenter: function(){
	    	$(this).removeClass('fa-star-o').addClass('fa-star');
	        $(this).prevAll().removeClass('fa-star-o').addClass('fa-star');
	    },
	    mouseleave: function(){
	    	if ($(".star-select.clicked") != $(this)) {
		    	$(this).removeClass('fa-star').addClass('fa-star-o');
		    	setTimeout(function () {
		            if ($(".star-select:hover").length === 0) {
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