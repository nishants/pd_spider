(function() {
	'use strict';

	crawler.app.service('crawlerService', ['Restangular', function(Restangular) {	 	    
		 var pages = Restangular.all('crawler/pages');

	    return {
	    	submitUrl: function(link){	   
	    		var req = {link: link} ;
	    		return pages.post(req);
	    	},
	    	getPage: function(pageId){
	    		return Restangular.one('crawler/pages', pageId).get(pageId);
	    	},	    	
	    	updatePage: function(params){
	    		return Restangular.one('crawler/pages', params.id).customPUT(params);
	    	},
	    	getPages: function(){
	    		return Restangular.all('crawler/pages').getList();
	    	}

	    };
	}]);

}).call(this);
