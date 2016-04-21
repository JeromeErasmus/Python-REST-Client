app.controller("RequestSettingsController", function($scope, RequestSettings, Request) {
  $scope.parameters = [];
  $scope.body = [];
  $scope.headers = [];
  $scope.authentication = {};
  $scope.proxy = {};
  $scope.methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'];
  $scope.method = "GET";
  $scope.url = "";

  $scope.response = {};

  
  
  RequestSettings.query(function(data) {
    $scope.parameters = data.parameters;

    // create data watcher
   // $scope.$watch('parameters', function() { 
     

      // save data
      $scope.requestSettings = new RequestSettings();
      $scope.requestSettings.parameters = $scope.parameters;

      RequestSettings.save($scope.requestSettings, function() {
        console.log($scope.requestSettings.parameters);
      });
  //  }, true);

  });


  $scope.sendRequest = function()
  {
  /*  RequestSettings.save($scope.requestSettings, function() {
        console.log($scope.requestSettings.parameters);
      });*/
   
    $scope.request = new Request();
    $scope.request.parameters = $scope.parameters;
    $scope.request.body = $scope.body;
    $scope.request.headers = $scope.headers;
    $scope.request.authentication = $scope.authentication;
    $scope.request.proxy = $scope.proxy;
    $scope.request.method = $scope.method;
    $scope.request.url = $scope.url;
    
    $scope.response = Request.save($scope.request, function() {
        
    });
    console.log($scope.response);
  }  
  
  $scope.parameterChange = function(parameters)
  {
    $scope.url = setUrlVars($scope.url, $scope.parameters);
  }
/*
  $scope.$watch('parameters', function() { 
    var str = $.param( $scope.parameters );
    var shallowDecoded = decodeURIComponent( str );
    console.log(shallowDecoded);
   // $scope.url = setUrlVars($scope.url, shallowDecoded);
  }, true);*/

  $scope.addParameterField = function()
  {
    $scope.parameters.push({"name":"", "value":""});
  }

  $scope.removeParameterField = function(field, index)
  {
    $scope.parameters.splice(index, 1);
    $scope.url = setUrlVars($scope.url, $scope.parameters);
  }

  $scope.addBodyField = function()
  {
    $scope.body.push({"name":"", "value":""});
  }

  $scope.removeBodyField = function(field, index)
  {
    $scope.body.splice(index, 1);
  }

  $scope.addHeaderField = function()
  {
    $scope.headers.push({"name":"", "value":""});
  }

  $scope.removeHeaderField = function(field, index)
  {
    $scope.headers.splice(index, 1);
  }

  $scope.dropboxitemselected = function (value, index) {
    $scope.method = value;
  }

  $scope.urlOnChange = function() {
    // chaeck if string contains query parameters
    console.log(getUrlVars($scope.url));
    var vars = getUrlVars($scope.url);
    $scope.parameters = getUrlVars($scope.url);

  }
});


function getUrlVars(url) {
  if(url.indexOf('?') == -1){
    return false;
  }
  var vars = [], hash;
  var hashes = url.slice(url.indexOf('?') + 1).split('&');
  for(var i = 0; i < hashes.length; i++)
  {
      hash = hashes[i].split('=');
      if(hash[0] != "")
      {
        vars.push({"name":hash[0], "value":hash[1]});
      }
        
  }
  return vars;
}

function setUrlVars(url, params) {
  
  var str = $.param( params );
  var shallowDecoded = decodeURIComponent( str );
  
  if(url.indexOf('?') == -1)
  {
    var newurl = url+shallowDecoded;
  }
  else
  {
    var  newUrl = url.slice(0, url.indexOf('?')+1);
    newUrl = newUrl+shallowDecoded;
  }

  return newUrl;
}

/*
app.controller('MainController', function($scope, $http) { 

  $scope.parameters = {};

  $scope.update = function(parameters)
  {
    $scope.parameters = angular.copy(parameters);
  }

  $scope.loadData = function()
  {

    $http.get("/loaddata/").success(function (data) {
      $scope.parameters = data.parameters;
    
    }).error(function () {
      console.log("error loading data");
    });
  }
});*/


