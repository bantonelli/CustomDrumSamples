/**
 * Created by brandonantonelli on 12/18/14.
 */

( function () {
    var app = angular.module("kitbuilder", []);

    app.controller("SlideController", function () {

        this.tab = 1;
        this.isSelected = function (tab) {
            return tab === this.tab;
        };

        this.tabSelect = function (tab){
            this.tab = tab;
        };

    });

})();