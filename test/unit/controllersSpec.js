'use strict';

/* jasmine specs for controllers go here */
// Use command+N to generate code for test suites.


describe("FilterController", function () {

    beforeEach(module('kitbuilder'));

//    var $rootScope;
//    beforeEach(inject(function(_$rootScope_) {
//        $rootScope = _$rootScope_;
//    }));

    it("should work", inject(function ($controller) {
        var scope = {};
        var ctrl = $controller('FilterController', {$scope: scope});
        expect(ctrl.tags).toContain("Hip-Hop");
    }));
});
