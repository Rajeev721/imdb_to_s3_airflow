import requests
import json
import pandas as pd
import os
import boto3
# import pprint
api_key = os.environ['IMBD_API_KEY']
api_host = os.environ.get('IMDB_API_HOST')
headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": api_host
}
"""# #This api call is to get reviews
# rev_url = "https://imdb8.p.rapidapi.com/title/get-reviews"
# rev_querystring = {"tconst":"tt0944947","currentCountry":"US","purchaseCountry":"US"}
# #This api call is to get user reviews
# url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"
# querystring = {"tconst":"tt0944947"}
# rev_response = requests.get(rev_url, headers=headers, params= rev_querystring)
# user_rev_response = requests.get(url, headers=headers, params= querystring)
"""

get_all_images_url = "https://imdb8.p.rapidapi.com/title/get-all-images"
querystring = {"tconst":"tt0944947"}
get_all_images_res = requests.get(get_all_images_url, headers=headers, params= querystring)


review_response = get_all_images_res.json()

images_dict = {}

for image in review_response.get('resource')['images']:
	images_dict[image.get('id')] = {"caption" : image.get('caption'),
	"created_on" : image.get('createdOn'),
	"url" : image.get('url'),
	"name" : image.get('relatedNames')[0]['name']}
	break
# print(review_response.get('@meta')['requestId'])
print(json.dumps(images_dict,  indent=4))
# pprint.PrettyPrinter(indent = 4).pprint(images_dict)