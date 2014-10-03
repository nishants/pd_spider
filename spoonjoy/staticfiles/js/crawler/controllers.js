(function() {
	'use strict';

	crawler.app.controller('SubmitUrlFormController', function($scope, crawlerService) {
		$scope.linkToSubmit	= null;
		var onSuccess = function(data){
			alert("PageId : "+ data.id);
		}
		var onFailure = function(data){
			alert("Failed to submit link : " + $scope.linkToSubmit)
		}

	    $scope.submitUrl = function() {
	        crawlerService.submitUrl($scope.linkToSubmit).then(onSuccess, onFailure)
	    };
	});

}).call(this);
