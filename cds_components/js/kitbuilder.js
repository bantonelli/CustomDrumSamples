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

//    app.controller('DrawingsController', ['$scope', function ($scope) {
//        $scope.categories = ['Soft', 'Elements'];
//
//        $scope.drawings = [{
//            name: 'Water',
//            category: 'Elements',
//            value: '2'
//        }, {
//            name: 'Fire',
//            category: 'Elements',
//            value: '1'
//        }, {
//            name: 'Air',
//            category: 'Elements',
//            value: '4'
//        }, {
//            name: 'Coton',
//            category: 'Soft',
//            value: '3'
//        }, {
//            name: 'Whool',
//            category: 'Soft',
//            value: '5'
//        }];
//
//
//    }]);

//    $(function () {
//        $('#MixItUpContainer1').mixItUp();
//    });

    $(function () {
        $('#kitmix').mixItUp();
    });

})();