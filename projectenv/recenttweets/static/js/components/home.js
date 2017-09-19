angular.module('main')
.controller('homeController', ($scope, $http, Pagination) => {
	$scope.clickHome = () => {
		$http({
			url: '/api/data/',
			method: 'GET',
			headers: {'X-Requested-With': 'XMLHttpRequest'},
			params: {query: '#tapingo'}
		}).then(function success(res) {
			$scope.result = res.data.info;
			$scope.pagination = Pagination.getNew(20);
			$scope.pagination.numPages = Math.ceil($scope.result.length / $scope.pagination.perPage);
		}, function error(res) {
		});
	}
	$scope.clickHome();
	$scope.clickSearch = () => {
		if ($scope.query === '') {
			return;
		} else {
			$http({
				url: '/api/data/',
				method: 'GET',
				headers: {'X-Requested-With': 'XMLHttpRequest'},
				params: {query: $scope.query}
			}).then(function success(res) {
				$scope.result = res.data.info;
				$scope.pagination = Pagination.getNew(20);
				$scope.pagination.numPages = Math.ceil($scope.result.length / $scope.pagination.perPage);
			}, function error(res) {
			});
		}
	}
	$scope.clickX = () => {
		$scope.query = '';
		$scope.result = [];
		$scope.pagination.page = 0;
		$scope.pagination.numPages = 1;
	}
})
.directive('home', () => {
	return {
		restrict: 'E',
		controller: 'homeController',
		templateUrl: 'static/html/home.html'
	};
});