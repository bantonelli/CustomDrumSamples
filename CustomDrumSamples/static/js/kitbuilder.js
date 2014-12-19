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

    app.controller("KitFilterController", function () {
        this.tags = false;
        this.newKits = false;
        this.alphabetical = false;
        this.onSale = false;

        this.showNewKits = function () {
            this.newKits = !(this.newKits);
        };

        this.showAlphabetical = function () {
            this.alphabetical = !(this.alphabetical);
        };

        this.showOnSale = function () {
            this.onSale = !(this.onSale);
        };

        this.showTags = function () {
            this.tags = !(this.tags);
        };

    });

    app.controller("SampleFilterController", function (){
        this.description = false;

        this.showDescription = function () {
            this.description = !(this.description);
        };

    });

})();