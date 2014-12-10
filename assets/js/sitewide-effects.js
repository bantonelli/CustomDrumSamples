/**
 * Created by brandonantonelli on 12/10/14.
 */


$(document).ready(function () {


    var tb = $('.cds-navbar');
    var tbs = "top-bar-scrolled";

    $('.slide').scroll(function() {
      if($(this).scrollTop()) {
        tb.addClass(tbs);
      } else {
        tb.removeClass(tbs);
      }
    });

    if (jQuery.browser.mobile == true) {
        // Defined in landing-page.js
        tapToTouch();

        // For mobile Sidebar
        $('.st-content').removeClass('z-index-fix');
    }
});