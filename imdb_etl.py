import requests
import json
import pandas as pd
import os
import boto3

api_key = os.environ['IMBD_API_KEY']
api_host = os.environ.get('IMDB_API_HOST')
headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": api_host
}

#This api call is to get reviews
rev_url = "https://imdb8.p.rapidapi.com/title/get-reviews"

rev_querystring = {"tconst":"tt0944947","currentCountry":"US","purchaseCountry":"US"}

#This api call is to get user reviews
url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"

querystring = {"tconst":"tt0944947"}

rev_response = requests.get(rev_url, headers=headers, params= rev_querystring)
user_rev_response = requests.get(url, headers=headers, params= querystring)

reviews = {}
rev_response_json = json.loads(rev_response.text)['imdbrating']
print(rev_response_json)