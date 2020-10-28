//===================Phần menu======================//
//Dong mo menu khi view tren phone
$('#expand').click(function () {
    var left = $('.menu').position().left;
    if (left != 0) {
        $('.menu').animate({ 'left': '0' }, 300);
        $('.nav_bar').css({ 'width': 'calc(100% - 240px)' });
        $('.nav_bar').animate({ 'left': '240px' }, 300);
        //$('#close').hide();
    }
    else {
        $('.menu').animate({ 'left': '-240px' }, 300);
        $('.nav_bar').css({ 'width': '100%' });
        $('.nav_bar').animate({ 'left': '0' }, 300);
        //$('#close').show();
    }
});
//click vao body se dong menu
var isMobile = {
    Android: function () {
        return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function () {
        return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function () {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function () {
        return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function () {
        return navigator.userAgent.match(/IEMobile/i);
    },
    any: function () {
        return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
    }
};
if (isMobile.any()) {
    $('body').click(function (event) {
        if (event.target.id != 'menu_expand' && event.target.id != 'Menu_txtSearch1') {
            $('.menu').animate({ 'left': '-240px' }, 300);
            $('.nav_bar').css({ 'width': '100%' });
            $('.nav_bar').animate({ 'left': '0' }, 300);
            //$('#close').show();
        }
    })
    $('body').addClass('mobi-font');
}
//gan active vao menu duoc chon
if (!$.session.get('_menuselect')) {
    $('#_menu00').addClass('active');
}
else {
    $('#' + $.session.get('_menuselect')).addClass('active');
}
//gan id cua menu duoc chon vao session
$('.menu > ul > li').click(function () {
    $.session.set('_menuselect', $(this).attr('id'));
});

//==============Kết thúc phần menu====================//

//===============Phần tin nổi bật=====================//
$(document).ready(function () {
    var currentSlide = 0;
    var rCurrent = 0;
    var myInterval;
    var _SumCount = $('.slides > div').length-1;    
    $('#slides0').show();
    $('#il0').addClass('left-active');
    function _Slider() {
        $('.Topright div.items').removeClass('left-active');
        $('#slides' + currentSlide).fadeOut(300, function () {            
            if (currentSlide == _SumCount) {
                currentSlide = 0;
            }
            else {
                currentSlide++;
            }
            $('#slides' + (currentSlide)).fadeIn(2000);
        });
        if (rCurrent == _SumCount) {
            rCurrent = 0;
        }
        else {
            rCurrent++;
        }
        $('#il' + rCurrent).addClass('left-active');
    }    
    function startSlider() {
        myInterval = setInterval(_Slider, 8000)
    }
    startSlider();
});
//===============Phần cắt bớt từ===============================//
//dem so tu
function countWords(value) {
    s = value;
    s = s.replace(/(^\s*)|(\s*$)/gi, "");
    s = s.replace(/[ ]{2,}/gi, " ");
    s = s.replace(/\n /, "\n");
    return s.split(' ').length;
}
var arr;
var _str;
var count;
$(document).ready(function () {
    $('.import-content > .items').each(function () {
        count = countWords($('span', this).text());
        _str = '';
        if (count > 15) {
            arr = $('span', this).text().trim().split(' ')
            for (i = 0; i < 15; i++) {
                _str += arr[i] + ' ';
            }
            $('span', this).text(_str.trimRight() + '...');
        }
    });
});
//===============Kết thúc phần cắt bớt từ======================//

$('.txtSearch').focus(function () {
    $('.linkSearch').addClass('linkSearch_focus');
});
$('.txtSearch').blur(function () {
    $('.linkSearch').removeClass('linkSearch_focus');
});
$('.txtSearch1').focus(function () {
    $('.linkSearch').addClass('linkSearch_focus');
});
$('.txtSearch1').blur(function () {
    $('.linkSearch').removeClass('linkSearch_focus');
});

$('#_video').enscroll({
    showOnHover: true,
    verticalTrackClass: 'track3',
    verticalHandleClass: 'handle3'
});

//phan thong bao
$('#_thongbaobar').enscroll({
    showOnHover: true,
    verticalTrackClass: 'track3',
    verticalHandleClass: 'handle3'
});
//Begin image slide
$('.hinh-anh-hoat-dong').cycle({
    fx: 'scrollHorz',
    next: '.next',
    prev: '.previous',
    pager: '.pager'
});

//show image slide show
$().piroBox({
    my_speed: 300, //animation speed
    bg_alpha: 0.5, //background opacity
    radius: 4, //caption rounded corner
    scrollImage: false, // true == image follows the page _|_ false == image remains in the same open position
    // in some cases of very large images or long description could be useful.
    slideShow: 'true', // true == slideshow on, false == slideshow off
    slideSpeed: 3, //slideshow 
    pirobox_next: 'piro_next', // Nav buttons -> piro_next == inside piroBox , piro_next_out == outside piroBox
    pirobox_prev: 'piro_prev', // Nav buttons -> piro_prev == inside piroBox , piro_prev_out == outside piroBox
    close_all: '.piro_close' // add class .piro_overlay(with comma)if you want overlay click close piroBox
});

//End image slide
//===============navRight============================//
//Phan video
$('#_video > ul >li').click(function () {
    var source = $('span', this).text();
    st = "<iframe width='100%' height='100%' src='//www.youtube.com/embed/" + source + "?showinfo=0&autoplay=1' frameborder='0' allowfullscreen></iframe>";
    $('.video-content').html(st);
});

function KiemTraNhapLieu(textbox) {
    var str = textbox.val().toLowerCase();
    var strarrDanhSachDen = new Array(
        "char", "nchar", "varchar", "nvarchar",
        "alter", "begin", "cast", "create", "cursor",
        "declare", "delete", "drop", "end", "exec",
        "execute", "fetch", "insert", "kill", "open",
        "select", "sys", "sysobjects", "syscolumns",
        "table", "update", "script"
    );
    for (x in strarrDanhSachDen) {
        if (str.indexOf(strarrDanhSachDen[x]) != -1) {
            alert("Không được nhập '" + strarrDanhSachDen[x] + "' vào đây, Hãy nhập lại!");
            $(textbox).val('');
            $(textbox).focus();
            return;
        }
    }
}

function _CheckInputValid(_arrID) {
    for (i = 0; i < _arrID.length; i++) {
        $('#' + _arrID[i]).change(function () {
            KiemTraNhapLieu($(this));
        });
    }
}


function _DoiMatKhau() {
    $('.overlay').fadeIn(100, function () {
        var height = $('#_changepassword').height();
        $('#_changepassword').css({ 'top': '-' + height + 'px' }).show().animate({ top: '100' }, 500);
    });
}
function _Close_form_dangnhap() {
    var height = $('.model_content').height();
    $('.overlay').removeClass('display_div').hide();
    $('.model_content').animate({ top: '-' + height + 'px' }, 500, function () {
        $('.model_content').removeClass('display_div').hide();
    });
}
