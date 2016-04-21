
var app = angular.module("myApp", ['ngResource']);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');

}]);

app.factory("RequestSettings", function($resource) {
  return $resource("/requestsettings", {}, {
    query: { isArray: false }
  })
});

app.factory("Request", function($resource) {
  return $resource("/sendrequest", {}, {
    query: { isArray: false }
  })
});


