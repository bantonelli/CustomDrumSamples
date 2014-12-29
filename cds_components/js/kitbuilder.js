/**
 * Created by brandonantonelli on 12/18/14.
 */

( function () {

    var app = angular.module("kitbuilder", []);

    app.controller("defaultCtrl",['$scope', '$http', function ($scope, $http) {

        var config = {
            headers: {
                Authorization: "Bearer rbY67hpqxtFEGGumpMFOQIPwsXu90p"
            }
        };

        $scope.loadData = function () {
            $http.get("/api/kits/?format.json", config).success(function (data) {
                $scope.products = data;
            });
        };
    }]);

    app.controller("TabController", ['$rootScope', function ($rootScope) {

        $rootScope.tab = 1;
        this.isSelected = function (tab) {
            return tab === $rootScope.tab;
        };

        this.tabSelect = function (tab){
            $rootScope.tab = tab;
        };

    }]);

    app.controller("SlideController", ['$rootScope', function ($rootScope){

        this.isSelected = function (tab) {
            return $rootScope.tab === tab;
        };
    }]);

    app.controller("KitFilterController", ['$rootScope', function ($rootScope) {
        // Kit Selection
        this.tags = false;
        this.newKits = false;
        this.alphabetical = false;
        this.onSale = false;
        this.kits = kitTestData;

        // Sample Selection
        this.description = false;
        this.currentKit = this.kits[0];

        // Finish Coding this
        var getTags = function () {
            for (var i = 0; i < this.kits.length; i++){

            }
        };

        this.showDescription = function () {
            this.description = !(this.description);
        };

        this.setCurrent = function (kit) {
            this.currentKit = kit;
        };

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

    }]);

})();