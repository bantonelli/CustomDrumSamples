'use strict';

/* jasmine specs for controllers go here */
// Use command+N to generate code for test suites.
    var app = angular.module("kitbuilder", []);

    app.controller("SampleFilterController", function (){
        this.description = false;

        this.showDescription = function () {
            this.description = !(this.description);
        };

    });


describe("tabController", function () {

    beforeEach(module('kitbuilder'));

//    var $rootScope;
//    beforeEach(inject(function(_$rootScope_) {
//        $rootScope = _$rootScope_;
//    }));

    it("should work", inject(function ($controller) {
        var scope = {};
        var ctrl = $controller('SampleFilterController', {$scope: scope});
        expect(ctrl.description).toBe(false);
    }));
});
