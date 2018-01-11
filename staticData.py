import csv

# Figure out how to better organize this file..

STOPS_FILE_RELATIVE_PATH = './static_data/stops.txt'
ROUTES_FILE_RELATIVE_PATH = './static_data/routes.txt'

def createSetFromCSV(filePath, idIndex):
	setToReturn = set()
	with open(filePath, 'rb') as csvFile:
		reader = csv.reader(csvFile)
		reader.next()	# Skip first line (assuming here all txt files used have a field-name first line)
		# Add better exception handling in below loop
		for row in reader:
			setToReturn.add(row[idIndex])	
	return setToReturn

stops = createSetFromCSV(STOPS_FILE_RELATIVE_PATH, 0)
routes = createSetFromCSV(ROUTES_FILE_RELATIVE_PATH, 0)

def isValidStopID(stopID):
	return stopID in stops

def isValidRouteID(routeID):
	return routeID in routes

