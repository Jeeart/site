;$(function () {
	var dom = {};

	function _getDom () {
		dom.$ctrls = $('.shortcut-ctrl li');
		dom.$ctrlPages = $('#shortcut-list ul');
        dom.$list = $('#shortcut-list');
        dom.$listVP = dom.$list.find('.sl-viewport');
        dom.$listCW = dom.$list.find('.sl-con-wrapper');

        dom.$nav = $('#nav');
	}

	function _bind () { 
		dom.$ctrls.find('a').click(function (e) {
			e.preventDefault();
			var _ind = $(this).parents('li').index();
			//console.log(_ind)
			dom.$ctrlPages.removeClass('current');
			dom.$ctrlPages.eq(_ind).addClass('current');
            
            var l = -(_ind*dom.$listVP.width());
            dom.$listCW.animate({
                'left': l
            });

			dom.$ctrls.removeClass('current');
			$(this).parents('li').addClass('current');
		});

		dom.$nav.delegate('a', 'click', function (e) {
			//console.log(e.target);
			var tar = e.target,
				$tar = $(tar),
				href = $tar.attr('href');
			if (/^#/.test(href)) {
				e.preventDefault();
				var $d = $(href),
					_t = $d.position().top;
				$('html,body').animate({
					scrollTop: _t
				})
			}
		});

	}
    
    function _setupList () {
        var uln = dom.$list.find('.sl-con-wrapper>ul').length,
            sw = dom.$listVP.width();
            
        dom.$listCW.width(uln*sw);

        $('.shortcut-ctrl').slideDown();
    }

	function __init () {
		_getDom();
        _setupList();
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