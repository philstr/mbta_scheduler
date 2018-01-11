import mbta
import constants

for pred in mbta.getArrivalTimePredictions(constants.LOWELL_LINE_ROUTE_ID, constants.WINCHESTER_CENTER_STOP_ID, constants.INBOUND_DIRECTION_ID):
	print pred