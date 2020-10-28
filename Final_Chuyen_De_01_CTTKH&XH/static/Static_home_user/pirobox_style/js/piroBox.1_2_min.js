(function (a) {
    a.fn.piroBox = function (b) {
        b = jQuery.extend({
            my_speed: null,
            close_speed: 300,
            bg_alpha: 0.5,
            scrollImage: null,
            pirobox_next: "piro_next_out",
            pirobox_prev: "piro_prev_out",
            radius: 4,
            close_all: ".piro_close,.piro_overlay",
            slideShow: null,
            slideSpeed: null
        }, b);

        function c() {
            var s = '<tr><td colspan="3" class="pirobox_up"></td></tr><tr><td class="t_l"></td><td class="t_c"></td><td class="t_r"></td></tr><tr><td class="c_l"></td><td class="c_c"><span><span></span></span><div></div></td><td class="c_r"></td></tr><tr><td class="b_l"></td><td class="b_c"></td><td class="b_r"></td></tr><tr><td colspan="3" class="pirobox_down"></td></tr>';
            var q = a(window).height();
            var p = a(jQuery('<div class="piro_overlay"></div>').hide().css({
                opacity: +b.bg_alpha,
                height: q + "px"
            }));
            var l = a(jQuery('<table class="pirobox_content" cellpadding="0" cellspacing="0"></table>'));
            var w = a(jQuery('<div class="caption"></div>').css({
                opacity: "0.8",
                "-moz-border-radius": b.radius + "px",
                "-khtml-border-radius": b.radius + "px",
                "-webkit-border-radius": b.radius + "px",
                "border-radius": b.radius + "px"
            }));
            var f = a(jQuery('<div class="piro_nav"></div>'));
            var t = a(jQuery('<div class="piro_close"></div>'));
            var r = a(jQuery('<a href="#play" class="play"></a>'));
            var n = a(jQuery('<a href="#stop" class="stop"></a>'));
            var j = a(jQuery('<a href="#prev" class="' + b.pirobox_prev + '"></a>'));
            var k = a(jQuery('<a href="#next" class="' + b.pirobox_next + '"></a>'));
            a("body").append(p).append(l);
            l.append(s);
            a(".pirobox_up").append(t);
            a(".pirobox_down").append(f);
            a(".c_c").append(r);
            r.hide();
            f.append(j).append(k).append(w);
            if (j.is(".piro_prev_out") || k.is(".piro_next_out")) {
                a("body").append(j).append(k);
                j.add(k).hide()
            } else {
                f.append(j).append(k)
            }
            var e = j.width();
            l.hide();
            var x = a("a[class^='pirobox_gall']");
            var y = new Object();
            for (var v = 0; v < x.length; v++) {
                var h = a(x[v]);
                y["a." + h.attr("class")] = 0
            }
            var o = new Array();
            for (var B in y) {
                o.push(B);
                if (a(B).length === 1) {
                    //alert("For single image is recommended to use class pirobox"); //bỏ dòng này để khi chỉ có 1 hình slide sẽ không thông báo lỗi.
                    a(B).css("border", "2px dotted red")
                }
            }
            for (var v = 0; v < o.length; v++) {
                a(o[v]).each(function (i) {
                    this.rel = i + 1 + "&nbsp;of&nbsp;" + a(o[v]).length
                });
                var d = a(o[v] + ":first").addClass("first");
                var u = a(o[v] + ":last").addClass("last")
            }
            a(x).each(function (i) {
                this.rev = i + 0
            });
            var m = a(x);
            var z = a("a.pirobox");
            a.fn.fixPNG = function () {
                return this.each(function () {
                    var i = a(this).css("backgroundImage");
                    if (i.match(/^url\(["']?(.*\.png)["']?\)$/i)) {
                        i = RegExp.$1;
                        a(this).css({
                            backgroundImage: "none",
                            filter: "progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true, sizingMethod=" + (a(this).css("backgroundRepeat") == "no-repeat" ? "crop" : "scale") + ", src='" + i + "')"
                        }).each(function () {
                            var C = a(this).css("position");
                            if (C != "absolute" && C != "relative") {
                                a(this).css("position", "relative")
                            }
                        })
                    }
                })
            };
            a(window).resize(function () {
                var i = a(window).height();
                p.css({
                    visibility: "visible",
                    height: +i + "px"
                })
            });
            j.add(k).bind("click", function (D) {
                D.preventDefault();
                var i = parseInt(a(m).filter(".item").attr("rev"));
                var C = a(this).is(".piro_prev_out,.piro_prev") ? a(m).eq(i - 1) : a(m).eq(i + 1);
                C.click();
                t.add(w).add(k).add(j).css("visibility", "hidden")
            });
            z.each(function (C) {
                var i = a(this);
                i.bind("click", function (F) {
                    F.preventDefault();
                    g(i.attr("href"));
                    var D = i.attr("href");
                    var E = i.attr("title");
                    if (E == "") {
                        w.html("<p>" + D + "<a href=" + D + ' class="link_to" target="_blank" title="Open Image in a new window"></a></p>')
                    } else {
                        w.html("<p>" + E + "<a href=" + D + ' class="link_to" target="_blank" title="Open Image in a new window"></a></p>')
                    }
                    a(".c_c").addClass("unique");
                    k.add(j).add(t).add(w).hide();
                    a(".play").remove()
                })
            });
            a(m).each(function (C) {
                var i = a(this);
                i.bind("click", function (G) {
                    G.preventDefault();
                    g(i.attr("href"));
                    var D = i.attr("href");
                    var F = i.attr("title");
                    var E = i.attr("rel");
                    if (F == "") {
                        w.html("<p>" + D + '<em class="number">' + E + "</em><a href=" + D + ' class="link_to" target="_blank" title="Open Image in a new window"></a></p>')
                    } else {
                        w.html("<p>" + F + '<em class="number">' + E + "</em><a href=" + D + ' class="link_to" target="_blank" title="Open Image in a new window"></a></p>')
                    }
                    if (i.is(".last")) {
                        a(".number").css("text-decoration", "underline")
                    } else {
                        a(".number").css("text-decoration", "none")
                    }
                    if (i.is(".first")) {
                        j.hide();
                        k.show()
                    } else {
                        k.add(j).show()
                    }
                    if (i.is(".last")) {
                        j.show();
                        k.hide()
                    }
                    if (i.is(".last") && i.is(".first")) {
                        j.add(k).hide();
                        a(".number").hide();
                        r.remove()
                    }
                    a(m).filter(".item").removeClass("item");
                    i.addClass("item");
                    a(".c_c").removeClass("unique")
                })
            });
            var g = function (i) {
                r.add(n).hide();
                t.add(w).add(k).add(j).css("visibility", "hidden");
                if (l.is(":visible")) {
                    a(".c_c div").children().fadeOut(300, function () {
                        a(".c_c div").children().remove();
                        A(i)
                    })
                } else {
                    a(".c_c div").children().remove();
                    l.show();
                    p.fadeIn(300, function () {
                        A(i)
                    })
                }
            };
            var A = function (H) {
                if (l.is(".loading")) {
                    return
                }
                l.addClass("loading");
                var C = new Image();
                C.onerror = function () {
                    var J = a(l).height();
                    l.css({
                        marginTop: parseInt(a(document).scrollTop()) - (J / 1.9)
                    });
                    a(".c_c div").append('<p class="err_mess">There seems to be an Error:&nbsp;<a href="#close" class="close_pirobox">Close Pirobox</a></p>');
                    a(".close_pirobox").bind("click", function () {
                        a(".err_mess").remove();
                        l.add(p).fadeOut(b.close_speed);
                        l.removeClass("loading");
                        a(".c_c").append(r);
                        return false
                    })
                };
                C.onload = function () {
                    var M = C.height;
                    var O = C.width;
                    var L = a(l).height();
                    var Q = a(window).height();
                    var K = a(window).width();
                    if (M + 100 > Q || O + 100 > K) {
                        var J = O;
                        var P = M;
                        var R = (O + 250) / K;
                        var N = (M + 250) / Q;
                        if (N > R) {
                            J = Math.round(O * (1 / N));
                            P = Math.round(M * (1 / N))
                        } else {
                            J = Math.round(O * (1 / R));
                            P = Math.round(M * (1 / R))
                        }
                        M += P;
                        O += J;
                        a(C).height(P).width(J).hide();
                        a(".c_c div").animate({
                            height: P + "px",
                            width: J + "px"
                        }, b.my_speed);
                        l.animate({
                            height: (P + 20) + "px",
                            width: (J + 20) + "px",
                            marginLeft: "-" + ((J) / 2 + 10) + "px",
                            marginTop: parseInt(a(document).scrollTop()) - (P / 1.9) - 20
                        }, b.my_speed, function () {
                            a(".piro_nav,.caption").css({
                                width: (J) + "px"
                            });
                            a(".piro_nav").css("margin-left", "-" + (J + 5) / 2 + "px");
                            var S = w.height();
                            w.css({
                                bottom: "-" + (S + 5) + "px"
                            });
                            a(".c_c div").append(C);
                            t.css("display", "block");
                            k.add(j).add(t).css("visibility", "visible");
                            w.css({
                                visibility: "visible",
                                display: "block"
                            });
                            a(C).show().fadeIn(300);
                            l.removeClass("loading");
                            if (b.slideShow == "slideshow") {
                                r.add(n).show()
                            } else {
                                r.add(n).hide()
                            }
                        })
                    } else {
                        a(C).height(M).width(O).hide();
                        a(".c_c div").animate({
                            height: M + "px",
                            width: O + "px"
                        }, b.my_speed);
                        l.animate({
                            height: (M + 20) + "px",
                            width: (O + 20) + "px",
                            marginLeft: "-" + ((O) / 2 + 10) + "px",
                            marginTop: parseInt(a(document).scrollTop()) - (M / 1.9) - 20
                        }, b.my_speed, function () {
                            a(".piro_nav,.caption").css({
                                width: (O) + "px"
                            });
                            a(".piro_nav").css("margin-left", "-" + (O + 5) / 2 + "px");
                            var S = w.height();
                            w.css({
                                bottom: "-" + (S + 5) + "px"
                            });
                            a(".c_c div").append(C);
                            t.css("display", "block");
                            k.add(j).add(t).css("visibility", "visible");
                            w.css({
                                visibility: "visible",
                                display: "block"
                            });
                            a(C).fadeIn(300);
                            l.removeClass("loading");
                            if (b.slideShow == "slideshow") {
                                r.add(n).show()
                            } else {
                                r.add(n).hide()
                            }
                        })
                    }
                };
                C.src = H;
                var i = a(window).height();
                var F = a(".piro_prev_out").height();
                a(".piro_prev_out").add(".piro_next_out").css({
                    marginTop: parseInt(a(document).scrollTop()) + (i / F - 125)
                });
                a(".caption p").css({
                    "-moz-border-radius": b.radius + "px",
                    "-khtml-border-radius": b.radius + "px",
                    "-webkit-border-radius": b.radius + "px",
                    "border-radius": b.radius + "px"
                });
                n.bind("click", function (J) {
                    J.preventDefault();
                    clearTimeout(I);
                    a(m).children().removeAttr("class");
                    a(".stop").remove();
                    a(".c_c").append(r);
                    k.add(j).css("width", e + "px")
                });
                r.bind("click", function (J) {
                    J.preventDefault();
                    clearTimeout(I);
                    if (a(C).is(":visible")) {
                        a(m).children().addClass(b.slideShow);
                        a(".play").remove();
                        a(".c_c").append(n)
                    }
                    k.add(j).css({
                        width: "0px"
                    });
                    return E()
                });
                a(b.close_all).bind("click", function (J) {
                    clearTimeout(I);
                    if (a(C).is(":visible")) {
                        J.preventDefault();
                        t.add(p).add(l).add(w).add(k).add(j).fadeOut(b.close_speed);
                        l.removeClass("loading");
                        a(m).children().removeAttr("class");
                        k.add(j).css("width", e + "px").hide();
                        a(".stop").remove();
                        a(".c_c").append(r);
                        r.hide()
                        $('.piro_overlay').remove(); //dòng này Quan mới làm thêm, nếu không có dòng này thì khi close sẽ không đóng div có class="piro_overlay"
                    }
                });

                function E() {
                    clearTimeout(I);
                    if (a(m).filter(".item").is(".last")) {
                        a(m).children().removeAttr("class");
                        k.add(j).css("width", e + "px");
                        a(".stop").remove();
                        a(".c_c").append(r);
                        r.hide()
                    } else {
                        if (a(m).children().is("." + b.slideShow)) {
                            k.click()
                        }
                    }
                }
                var I = setInterval(E, b.slideSpeed * 1000);
                a().bind("keydown", function (J) {
                    if (J.keyCode === 27) {
                        J.preventDefault();
                        if (a(C).is(":visible") || a(".c_c>div>p>a").is(".close_pirobox")) {
                            t.add(p).add(l).add(w).add(k).add(j).fadeOut(b.close_speed);
                            l.removeClass("loading");
                            clearTimeout(I);
                            a(m).children().removeAttr("class");
                            a(".stop").remove();
                            a(".c_c").append(r);
                            k.add(j).css("width", e + "px");
                            a(m).add(z).children().fadeTo(100, 1)
                        }
                    }
                }).bind("keydown", function (J) {
                    if (a(".c_c").is(".unique") || a(".item").is(".first")) { } else {
                        if (a(".c_c").is(".c_c") && (J.keyCode === 37)) {
                            J.preventDefault();
                            if (a(C).is(":visible")) {
                                clearTimeout(I);
                                a(m).children().removeAttr("class");
                                a(".stop").remove();
                                a(".c_c").append(r);
                                k.add(j).css("width", e + "px");
                                j.click()
                            }
                        }
                    }
                    if (a(".c_c").is(".unique") || a(".item").is(".last")) { } else {
                        if (a(".c_c").is(".c_c") && (J.keyCode === 39)) {
                            J.preventDefault();
                            if (a(C).is(":visible")) {
                                clearTimeout(I);
                                a(m).children().removeAttr("class");
                                a(".stop").remove();
                                a(".c_c").append(r);
                                k.add(j).css("width", e + "px");
                                k.click()
                            }
                        }
                    }
                });
                a.browser.msie6 = (a.browser.msie && /MSIE 6\.0/i.test(window.navigator.userAgent));
                if (a.browser.msie6 && !/MSIE 8\.0/i.test(window.navigator.userAgent)) {
                    a(".t_l,.t_c,.t_r,.c_l,.c_r,.b_l,.b_c,.b_r,a.piro_next, a.piro_prev,a.piro_prev_out,a.piro_next_out,.c_c,.piro_close,a.play,a.stop").fixPNG();
                    var D = a(document).height();
                    p.css("height", D + "px")
                }
                if (a.browser.msie) {
                    b.close_speed = 0
                }

                function G() {
                    if (a(l).is(":visible")) {
                        window.onscroll = function () {
                            var L = a(l).height();
                            l.css({
                                marginTop: parseInt(a(this).scrollTop()) - (L / 1.9) - 10
                            });
                            var J = a(window).height();
                            var K = a(".piro_prev_out").height();
                            a(".piro_prev_out").add(".piro_next_out").css({
                                marginTop: parseInt(a(document).scrollTop()) + (J / K - 125)
                            })
                        }
                    }
                }
                if (b.scrollImage == true) {
                    return G()
                }
            }
        }
        c()
    }
})(jQuery);