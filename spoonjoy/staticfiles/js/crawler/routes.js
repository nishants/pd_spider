
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
      }).state('edit-page', {
        url: "/:id/edit",
        views: {
          default: {
            templateUrl: "../public/pages/_edit_page_form.html",
            controller: "EditFormController"
          }
        }
      })
    }
  ]);

}).call(this);
