# Ibis-homework
## Inspiration
This is a homework assignment from a company Ibis Solutions.
## General info
This is a small service which uses the data from click_log_fixed.csv database and exposes it via API. The file has the data for the following fields: id, click_id, timestamp (unix timestamp), type, campaign,
banner, content_unit, network, browser, operating_system, country, state and city.

Project consists of multiple parts:
* SQL server which has the the data from click_log_fixed.csv
* The API
* API extended with a time filter
* tests

The API is recieving information about the campaign and it returns the number of clicks that were made on advertisements that belong to this
campaign. Extended API has additional information: a start date and a end date and it returns the number of clicks that were made between the start date and the end
date. Tests cover the API route.
## Technololgies
* Python
* Django library
* PostgreSQL

This project was written in PyCharm IDE.
## Running this project 
``` 
python3 manage.py runserver 8000
``` 


