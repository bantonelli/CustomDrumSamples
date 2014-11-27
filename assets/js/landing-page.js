/**
 * Created by brandonantonelli on 11/16/14.
 */



/*
landingRow2.removeClass("down-low");
    landingRow1.addClass("down-low");
    landingRow2.removeClass("below");
    landingRow2.addClass("on-top");
    landingRow1.removeClass("on-top");
    landingRow1.addClass("below");
*/

$('.frontpage-arrow a').on("click", function() {

    var landingRow1 = $("#slide-1");
    var landingRow2 = $("#slide-2");

    if (landingRow1.hasClass("on-top")) {
        landingRow2.animate({ top: "0", opacity: "1"}, 0, "linear", function() {
            landingRow1.animate({top: "100%", opacity: "0.2"}, 750, "linear", function () {
                landingRow2.removeClass("below").addClass("on-top");
                landingRow1.removeClass("on-top").addClass("below");
            });
        });
    } else {
        landingRow1.animate({ top: "0", opacity: "1"}, 0, "linear", function() {
            landingRow2.animate({top: "100%", opacity: "0.2"}, 750, "linear", function () {
                landingRow1.removeClass("below").addClass("on-top");
                landingRow2.removeClass("on-top").addClass("below");
            });
        });
    }

});

// Morphing buttons
//
