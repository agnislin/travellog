
jQuery(document).ready(function() {

    /*
        Fullscreen background
    */
    $.backstretch("/static/travellog/img/IMG_0095.JPG");

    /*
        Form validation
    */
    $('.service-form input[type="text"], .service-form input[type="password"], .service-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    $('.service-form').on('submit', function(e) {

    	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});

    });


});
