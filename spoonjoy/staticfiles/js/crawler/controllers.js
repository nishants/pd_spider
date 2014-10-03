(function() {
	'use strict';

	crawler.app.controller('SubmitUrlFormController', function($scope, crawlerService, $location) {
		$scope.linkToSubmit	= null;
		var onSuccess = function(data){
			var link = data.id+"/edit"
        	$location.url(link)
		}

		var onFailure = function(data){
			console.error("Failed to submit link : " + $scope.linkToSubmit)
		}

	    $scope.submitUrl = function() {
	        crawlerService.submitUrl($scope.linkToSubmit).then(onSuccess, onFailure)
	    };
	});

	crawler.app.controller('EditFormController', function($scope, crawlerService, $stateParams) {
		
		var getPage =  function(){
			var onGetPage = function(data){
				$scope.page = data;
			}

			var pageNotFound = function(data){
				console.error("No page found with id : " + $stateParams.id);
			}

			crawlerService.getPage($stateParams.id).then(onGetPage, pageNotFound)
		}

		var onSuccess = function(data){
			console.log("updated page : "+ data.id);
		}
		var onFailure = function(data){
			console.error("Failed to update page : ")
		}

	    $scope.updatePage = function() {
	        crawlerService.updatePage($scope.page).then(onSuccess, onFailure)
	    };
	    getPage();

	});

	crawler.app.controller.fetchPageMetaData = {

	}
}).call(this);
