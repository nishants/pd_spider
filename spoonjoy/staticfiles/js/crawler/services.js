(function() {
	'use strict';

	crawler.app.service('crawlerService', ['Restangular', function(Restangular) {	 	    
		 var pages = Restangular.all('crawler/pages')

	    return {
	    	submitUrl: function(link){	   
	    		var req = {link: link} 		
	    		pages.post(req);
	    	}

	    };
	}]);

}).call(this);