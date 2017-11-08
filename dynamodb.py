import boto
from boto.dynamodb import connect_to_region
from flask import current_app as app

con = connect_to_region(aws_access_key_id=app.config["AWS_KEY"],
	aws_secret_access_key=app.config["AWS_SECRET"],
	region_name='us-east-1')

table = con.get_table(app.config["DYNAMODB_TABLE"])
for item in table.scan():
	print item


