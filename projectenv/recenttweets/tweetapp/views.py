from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import tweepy
import json

def get_data(request):
	if request.method == 'GET' and request.is_ajax():
		query = request.GET['query']
		auth = tweepy.OAuthHandler('', '')
		auth.set_access_token('', '')
		api = tweepy.API(auth)
		result = api.search(query, count=100)
		months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
		tweets = []
		for i in result:
			string = str(i.created_at)
			arr = string.split(' ')
			arr = arr[0].split('-')
			date = months[int(arr[1]) - 1] + ' ' + arr[2]
			tweets.append([i.text, date, i.user.name, '@' + i.user.screen_name, i.user.profile_image_url])
		return HttpResponse(json.dumps({'info': tweets}), content_type="application/json", status=200)
	else:
		return HttpResponse('Request not GET or not AJAX', status=400)
