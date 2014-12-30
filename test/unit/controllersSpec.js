'use strict';

/* jasmine specs for controllers go here */
// Use command+N to generate code for test suites.


describe("kitController", function () {

    beforeEach(module('kitbuilder'));

//    var $rootScope;
//    beforeEach(inject(function(_$rootScope_) {
//        $rootScope = _$rootScope_;
//    }));

    it("should work", inject(function ($controller) {
        var scope = {};
        var ctrl = $controller('KitFilterController', {$scope: scope});
        expect(ctrl.tags).toContain("Hip Hop");
    }));
});
