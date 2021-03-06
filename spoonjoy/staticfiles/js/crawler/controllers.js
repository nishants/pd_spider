(function() {
	'use strict';

	crawler.app.controller('IndexedPagesController', function($scope, crawlerService, $location) {
		$scope.pages  = [];
		
		var onSuccess = function(response){
			$scope.pages = response;	
		}

		var onFailure = function(response){
			console.error("Failed to fetch pages : ")
		}

	    var loadPages = function() {
	        crawlerService.getPages().then(onSuccess, onFailure)
	    };

	    loadPages();
	    $scope.redirectToListPages = function(){
	    	$location.url("/indexedPages")
	    }
	});

	crawler.app.controller('SubmitUrlFormController', function($scope, crawlerService, $location) {
		$scope.linkToSubmit	= null;
		var handleError = function(error){
			alert("Could not porcess url.\nReason : "+error)
		}
		var onSuccess = function(response){
			if(response.error){
				handleError(response.error);
			}
			var link = response.data.id+"/edit"
        	$location.url(link)
		}

	    $scope.submitUrl = function() {
	        crawlerService.submitUrl($scope.linkToSubmit).then(onSuccess)
	    };
	});

	crawler.app.controller('EditFormController', function($scope, crawlerService, $stateParams, $location) {
		
		var getPage =  function(){
			var onGetPage = function(response){
				$scope.page = response.data;
			}

			var pageNotFound = function(response){
				console.error("No page found with id : " + $stateParams.id);
			}

			crawlerService.getPage($stateParams.id).then(onGetPage, pageNotFound)
		}

		var onSuccess = function(response){
			$location.url('/indexedPages');
		}
		var onFailure = function(response){
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
