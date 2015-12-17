var app = angular.module('ui.bootstrap.demo', ['ui.bootstrap', 'ngAnimate', 'ngTouch'])

app.controller('CarouselDemoCtrl', function ($scope) {
    $scope.myInterval = 5000;
    $scope.noWrapSlides = false;
    var slides = $scope.slides = [];
    $scope.addSlide = function () {
        var newWidth = 600 + slides.length + 1;
        slides.push({
            image: '//placekitten.com/' + newWidth + '/300',
            //image:'../../static/app/images/carousel1.jpg',
            text: ['More', 'Extra', 'Lots of', 'Surplus'][slides.length % 4] + ' ' +
              ['Cats', 'Kittys', 'Felines', 'Cutes'][slides.length % 4]
        });
    };
    for (var i = 0; i < 4; i++) {
        $scope.addSlide();
    }
    $scope.t = 'sksksksk';
});

app.controller('CollapseDemoCtrl', function ($scope) {
    $scope.isCollapsed = false;
});

app.controller('DropdownCtrl', function ($scope, $log) {
    $scope.items = [
      'The first choice!',
      'And another choice for you.',
      'but wait! A third!'
    ];

    $scope.status = {
        isopen: false
    };

    $scope.toggled = function (open) {
        $log.log('Dropdown is now: ', open);
    };

    $scope.toggleDropdown = function ($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.status.isopen = !$scope.status.isopen;
    };

    $scope.isCollapsed = false;
});

app.controller('PostCall', function ($scope, $http) {
    var request = {
        method: 'GET',
        url: '/users/',
        headers: {
            'Accept-Content': 'application/json'
        }
    }
    $http(request).then(function (response) {
        $scope.users = response.data
    })



    var  request2 = {
        method: 'POST',
        url: '/caculate_relevance',
        headers: {
            'Content-Type': 'application/json'
        },
        data: { item1: '3232', item2: 'kkkk' }
    }
    var postdata = { 'item1': '3232', 'item2': 'kkkk' }
    $http(request2).then(function (response) {
        $scope.items = response.data

    })
})