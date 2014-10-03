(function() {
	'use strict';

	crawler.app.controller('SubmitUrlFormController', function($scope, crawlerService) {
		$scope.linkToSubmit	= null;
	    $scope.submitUrl = function() {
	        crawlerService.submitUrl($scope.linkToSubmit)
	    };
	});

}).call(this);
