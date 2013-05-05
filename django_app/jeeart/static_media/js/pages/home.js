;$(function () {
	var dom = {};

	function _getDom () {
		dom.$ctrls = $('.shortcut-ctrl li');
		dom.$ctrlPages = $('#shortcut-list ul');
	}

	function _bind () { 
		dom.$ctrls.find('a').click(function (e) {
			e.preventDefault();
			var _ind = $(this).parents('li').index();
			//console.log(_ind)
			dom.$ctrlPages.removeClass('current');
			dom.$ctrlPages.eq(_ind).addClass('current');

			dom.$ctrls.removeClass('current');
			$(this).parents('li').addClass('current');
		});
	}

	function __init () {
		_getDom();
		_bind();

		//init gallery
		$('.gallery-scr').flexslider({
	        animation: "slide",
	        slideshow: true,
	        controlNav: false,               //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
	        directionNav: true
	    });
	}
	
	__init();

});