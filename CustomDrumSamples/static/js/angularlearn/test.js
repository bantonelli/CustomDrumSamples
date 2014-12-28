/**
 * Created by brandonantonelli on 12/27/14.
 */


var app = angular.module("learning", []);

app.controller("defaultCtrl", function ($scope, $http) {

    var config = {
        headers: {
            Authorization: "Bearer XMrPJCExlOem0cXyPTJxhGyvyZqVB8"
        }
    }

    $scope.loadData = function () {
        $http.get("/api/kits/?format.json", config).success(function (data) {
            $scope.kits = data;
        });
    }
});



var HelloCtrl = function ($scope) {
    $scope.name = 'World';
    // Creating an object on the parent controller that
    // can be accessed from child scopes.
    this.myObject = {name: "myObject"};
};

var ChildCtrl = function ($scope) {
    // Example use of accessing parent scope's models
    // $scope.name = $scope.$parent.name;
};

app.controller("HelloCtrl", HelloCtrl);

app.controller("ChildCtrl", ChildCtrl);