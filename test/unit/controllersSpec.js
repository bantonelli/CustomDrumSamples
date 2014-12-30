'use strict';

/* jasmine specs for controllers go here */
// Use command+N to generate code for test suites.

describe("FilterController", function () {

    beforeEach(module('kitbuilder'));

    it("should consolidate tags from kits into the tags array", inject(function ($controller) {
        var scope = {};
        var ctrl = $controller('FilterController', {$scope: scope});
        expect(ctrl.tags).toContain("Hip-Hop");
    }));
});

