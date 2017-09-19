var app = angular.module('main', ['ngRoute', 'simplePagination']);
app.config(($routeProvider, $httpProvider) => {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$routeProvider
	.when('/', {
		template: '<home></home>'
	})
});