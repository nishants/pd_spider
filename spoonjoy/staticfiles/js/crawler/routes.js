
(function() {
  "use strict";
  crawler.app.config([
    '$stateProvider', function($stateProvider) {
      return $stateProvider.state('submit-url', {
        url: "/submitUrl",
        views: {
          default: {
            templateUrl: "../public/pages/_submit_link_form.html",
            controller: "SubmitUrlFormController"
          }
        }
      })
    }
  ]);

}).call(this);
