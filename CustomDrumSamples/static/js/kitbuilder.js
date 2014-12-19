/**
 * Created by brandonantonelli on 12/18/14.
 */

( function () {

    var app = angular.module("kitbuilder", []);

    var tabController = app.controller("TabController", function ($rootScope) {

        $rootScope.tab = 1;
        this.isSelected = function (tab) {
            return tab === $rootScope.tab;
        };

        this.tabSelect = function (tab){
            $rootScope.tab = tab;
        };

    });

    app.controller("SlideController", function ($rootScope){

        this.isSelected = function (tab) {
            return $rootScope.tab === tab;
        };
    });

})();