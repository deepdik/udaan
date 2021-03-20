#!/bin/bash

while [ true ]; do
	# do what you need to here
	cd /home/ubuntu/spark_18/spark_18/
	source env/bin/activate
	python manage.py delete_token
	sleep 1
done


