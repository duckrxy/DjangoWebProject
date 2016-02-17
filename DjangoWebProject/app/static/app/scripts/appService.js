angular.module('appservice', []).factory('calculate', function () {
    var returnResult = function (a, b) {
        return a * b;
    };
    return returnResult;
});