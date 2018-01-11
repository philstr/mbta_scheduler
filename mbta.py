import requests
import json
import staticData

API_URL_BASE = 'https://api-v3.mbta.com'

class InvalidArgumentException(Exception):
	pass

def getPredictions(routeID, stopID, directionID=None):
	validateRouteID(routeID)
	validateStopID(stopID)
	validateDirectionID(directionID)
	url = '{}/predictions?filter[route]={}&filter[stop]={}&filter[direction_id]={}'.format(API_URL_BASE, routeID, stopID, directionID)
	predictions = []
	try:
		rawResponse = requests.get(url)
		predictions = rawResponse.json()['data']
	except:
		print "Error!" # Do something better here
	return predictions

def getArrivalTimePredictions(routeID, stopID, directionID=None):
	predictions = getPredictions(routeID, stopID, directionID)
	return [p['attributes']['arrival_time'] for p in predictions]

def validateRouteID(routeID):
	assert staticData.isValidRouteID(routeID), "Invalid route ID"

def validateStopID(stopID):
	assert staticData.isValidStopID(stopID), "Invalid stop ID"

def validateDirectionID(directionID):
	if directionID == None:
		return
	assert directionID is '0' or directionID is '1', "provided direction ID must be \"0\" or \"1\""

