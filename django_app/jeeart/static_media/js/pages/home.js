;$(function () {
	var dom = {};
	var MIN_H = 520;
    var MAX_W = 800;

	function _getDom () {
		dom.$ctrls = $('.shortcut-ctrl li');
		dom.$ctrlPages = $('#shortcut-list ul');
        dom.$list = $('#shortcut-list');
        dom.$listVP = dom.$list.find('.sl-viewport');
        dom.$listCW = dom.$list.find('.sl-con-wrapper');

        dom.$nav = $('#nav');
        dom.$hd = $('#header');
        dom.$con = $('#content');
        dom.$gallery = $('#gallery');
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

		$(window).on('resize', function () {
			resize();
		})

	}
    
    function _setupList () {
        var uln = dom.$list.find('.sl-con-wrapper>ul').length,
            sw = dom.$listVP.width();
            
        dom.$listCW.width(uln*sw);

        $('.shortcut-ctrl').slideDown();
    }

    function _getWorksList () {
        $.get('/cgi/home/getWorksList', {
            s:9,
            n:9
        }, function (data) {
            console.log(data);
        })

    }
    
    function _lazyHome () {
        $('.lazy img').lazyload({
        	effect: 'fadeIn',
        	container: $("#content")
        });
    }

    function _startAnim () {
        if (Modernizr.csstransitions) {
            dom.$nav.addClass('show');
        }
    }

    function resize () {
    	$('body').addClass('ofh');

        if (window.innerWidth < 1024) {
            return;
        }

    	var h = Math.max(MIN_H, window.innerHeight);
    	dom.$hd.css({
    		height: h,
    		overflow: 'hidden',
    		width: '29.9%'
    	});
    	dom.$con.css({
    		height: h,
    		overflow: 'auto',
    		webkitOverflowScrolling: 'touch',
    		width: (window.innerWidth*0.7 - 40)
    	});
        dom.$con.find('.con-inner').css({
            width: Math.min(850, dom.$con.width())
        });

    	dom.$gallery.find('.gallery-scr').css({
    		width: dom.$gallery.width() - 20,
    		height: 'auto'
    	});
    	dom.$gallery.find('.gallery-scr img').css({
    		width: '100%',
    		height: 'auto'
    	});

    	var galleryW = dom.$gallery.width();
    	dom.$listVP.css({
    		width: galleryW
    	});
    	_setupList();

    	dom.$list.find('ul').css({
    		width: galleryW
    	});
    	dom.$listVP.find('li').css({
    		width: ((galleryW - 42)/3 -20)
    	});
    	dom.$list.find('img').css({
    		width: '100%'
    	});

    	//resize left
    	var l = -(dom.$list.find('ul.current').index()*dom.$listVP.width());
        dom.$listCW.css({
            'left': l
        });
    }

	function __init () {
		_getDom();
		resize();
		_bind();
        //_getWorksList();
        _lazyHome();
        _startAnim();

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