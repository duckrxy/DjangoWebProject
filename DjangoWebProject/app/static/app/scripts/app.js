var app = angular.module('ui.bootstrap.demo', ['ui.bootstrap', 'ngAnimate', 'ngTouch'])

app.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_value }}';
})

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


    $scope.postrequest = function () {
        var postdata = { item1: '3232', item2: 'kkkk' }


        $http({
            method: 'POST',
            url: '/test_api/',
            data: postdata,
            headers: { 'Content-Type': 'application/json; charset=utf8' }
        }).then(function (response) {
            $scope.item = response.data
        })
        $http.post('/test_api/', postdata).then(function (response) {
            $scope.item = response.data
        })

    }

    $scope.getrequest = function () {

        var postdata = { item1: '3232', item2: 'kkkk' }
        $http({
            method: 'GET',
            url: '/test_api?item1=sss&item2=sss',
            data: postdata,
            headers: { 'Content-Type': 'application/json; charset=utf8' }
        }).then(function (response) {
            $scope.item = response.data
        })

    }



})