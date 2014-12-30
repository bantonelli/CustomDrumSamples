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
        this.tagsVisible = false;
        this.newKits = false;
        this.alphabetical = false;
        this.onSale = false;
        this.kits = kitTestData;
        this.tagsChecked =

        // Finish Coding this
        this.getTags = function () {
            var totalTags = [];
            for (var kit = 0; kit < this.kits.length; kit++){
                var tags = this.kits[kit].tags;
                for (var tagIndex = 0; tagIndex < tags.length; tagIndex++) {
                    if ($.inArray(tags[tagIndex], totalTags) === -1) {
                        totalTags.push(tags[tagIndex]);
                    }
                }
            }
            return totalTags;
        };

        this.tags = this.getTags();

        // Sample Selection
        this.description = false;
        this.currentKit = this.kits[0];

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
            this.tagsVisible = !(this.tagsVisible);
        };

    }]);

    app.filter('kitfilter', function() {
    return function(items, options ) {
      // loop over all the options and if true ensure the car has them
      // I cant do this for you beacause I don't know how you would store this info in the car object but it should not be difficult
      return carMatches;
    };
});

})();