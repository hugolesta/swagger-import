import boto3
import datetime
import types
import json
from dateutil.relativedelta import relativedelta
import botocore
import ast
import os

#IMPLEMENTED AS STATIC METHOD BUT IT CAN BE IMPLEMENTED AS A NORMAL FUNCTION
#SimpleNamespace() USED TO BUILD THOSE TUPLES, WITH IT CAN BE IMPLEMENTED VIA A NORMAL OBJECT
class time:

	@staticmethod
	def daily(date, delta = 1):
		ret = types.SimpleNamespace()
		ret.start = date - datetime.timedelta(days=delta)
		ret.end = date
		return ret

	@staticmethod
	def monthly(date, delta = 1):
		ret = types.SimpleNamespace()
		ret.start = date - relativedelta(months=delta)
		ret.end = date 
		return ret

	@staticmethod
	def yearly(date, delta = 1):
		ret = types.SimpleNamespace()
		ret.start = date - relativedelta(years=delta)
		ret.end = date
		return ret


def read_file_from_bucket(bucketname, filename):
	s3 = boto3.resource('s3')

	obj = s3.Object(bucketname, filename)       

	body = obj.get()['Body'].read().decode('utf-8')

	return body

def delete_object_from_bucket(bucketname, filename):
	s3 = boto3.resource('s3')
	obj = s3.Object(bucketname, filename)
	obj.delete()

	return True

def check_path_status(bucketname, path):
	try:
		s3 = boto3.resource('s3')
		s3.Object(bucketname,path).load
		return True
	except Exception as e:
		if e.response['Error']['Code'] == "404":
			print(e)
			return False

def check_if_S3_object_exist(bucketname, prefix):
	try:
		s3 = boto3.resource('s3')
		s3.Object(bucketname, prefix).download_file()

	except botocore.exceptions.ClientError as e:
			if e.response['Error']['Code'] == "404":
					# The object does not exist.
					return False
			else:
					# Something else has gone wrong.
					raise
	else:
			# The object does exist.
			return True


def put_obj_in_bucket(json_object, bucket, key):
	s3 = boto3.client('s3')
	s3.put_object(
		Body=json.dumps(json_object),
		Bucket=bucket,
		Key=key
	)

def import_swagger(swagger_name, api_gtw_id, parameters,region):
	apiGw = boto3.client('apigateway',region)
	api_res = apiGw.put_rest_api(
		restApiId= api_gtw_id,
		mode='overwrite',
		failOnWarnings=True,
		parameters=ast.literal_eval(parameters),
		body=open('{complete_path}/src/swagger/tasks/swagger_files/{name}.json'.format(complete_path=os.path.abspath(os.getcwd()),name = swagger_name), 'rb').read()
	)
	return api_res