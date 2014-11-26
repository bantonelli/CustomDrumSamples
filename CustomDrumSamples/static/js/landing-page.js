/**
 * Created by brandonantonelli on 11/16/14.
 */


//var landingRow1 = $("#slide-1");
//var landingRow2 = $("#slide-2");
///*
//landingRow2.removeClass("down-low");
//    landingRow1.addClass("down-low");
//    landingRow2.removeClass("below");
//    landingRow2.addClass("on-top");
//    landingRow1.removeClass("on-top");
//    landingRow1.addClass("below");
// */
//
//$('.cds-arrow').on("click", function() {
//
//    if (landingRow1.hasClass("on-top")) {
//        landingRow2.animate({ "top": "0", opacity: "1"}, 0, "linear", function()
//           {    landingRow1.animate ({ "top": "100%", opacity: "0.2"}, 750, "easeInOutQuart", function()
//                {
//                    landingRow2.removeClass("below", function (){
//                        landingRow2.addClass("on-top", function () {
//                            landingRow1.removeClass("on-top", function(){
//                                landingRow1.addClass("below");
//                            })
//                        })
//                    })
//                })
//            }
//        );
//    } else {
//        landingRow1.animate ({ "top": "0", opacity: "1"}, 0, "linear", function()
//           {    landingRow2.animate ({ "top": "100%", opacity: "0.2"}, 750, "easeInOutQuart", function()
//                {
//                    landingRow1.removeClass("below", function (){
//                        landingRow1.addClass("on-top", function () {
//                            landingRow2.removeClass("on-top", function(){
//                                landingRow2.addClass("below");
//                            })
//                        })
//                    })
//                })
//            }
//        );
//    }
//
//});

// Morphing buttons
//
if (Modernizr.touch) {
/* bind events */
$(document)
    .on('focus', 'input', function(e) {
    $('.morph-content-nav').addClass('fixfixed');
    })
    .on('blur', 'input', function(e) {
    $('.morph-content-nav').removeClass('fixfixed');
});
}