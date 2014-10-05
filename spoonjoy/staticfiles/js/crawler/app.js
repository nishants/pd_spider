(function() {
  	'use strict';
  	window.crawler = {};
  	crawler.app = angular.module("crawler-app", ['ui.router', 'restangular']);

  	crawler.app.config(
  		function (RestangularProvider) {
    		RestangularProvider.setRequestSuffix('/');
		}
	);

}).call(this);
