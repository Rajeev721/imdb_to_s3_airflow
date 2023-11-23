import requests
import json
import pandas as pd
import os
import boto3

def rapid_api_etl():
	try:
		api_key = os.environ['IMBD_API_KEY']
		api_host = os.environ.get('IMDB_API_HOST')
		headers = {
			"X-RapidAPI-Key": api_key,
			"X-RapidAPI-Host": api_host
		}
		"""****************************************Check if HTTPD is installed in the server if you are unable to connect via public IP****************************************
		yum install httpd
		getenforce
		service httpd start
		"""
		"""****************************************Installing Python and airflow:****************************************
		sudo yum install update
		sudo yum install python3-pip
		pip install "apache-airflow[celery]==2.7.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt"
		airflow standalone
		"""
		"""****************************************This api call is to get reviews****************************************
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

		print(get_all_images_res.status_code)


		review_response = get_all_images_res.json()

		images_dict = {}

		for image in review_response.get('resource')['images']:
			images_dict[image.get('id').split('/')[-1]] = {"caption" : image.get('caption'),
			"created_on" : image.get('createdOn'),
			"url" : image.get('url'),
			"name" : image.get('relatedNames')[0]['name'] if image.get('relatedNames') else ""}
		
		# print(images_dict)
		session = boto3.Session(profile_name='rajeev')
		s3 = session.client('s3')
		res = s3.put_object(Bucket='rajeevlearning', Key = 'landing/images_dict.json', Body = json.dumps(images_dict))
		# print(res)

		# print(review_response.get('@meta')['requestId'])
		# print(json.dumps(images_dict,  indent=4))
		# with open('images_dict.json', 'w') as f:
		# 	json.dump(images_dict,f)
	except Exception as e:
		print(e)

rapid_api_etl()