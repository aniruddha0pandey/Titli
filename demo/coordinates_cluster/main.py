import config
from database import *
import cluster
import calendar, time

def compute():
	a=cluster.fetch_coordinates(coordinates)
	latitude, longitude = [], []
	for i in range(len(a)):
		for j in range(1):
			latitude.append(a[i][0])
			longitude.append(a[i][1])
	return latitude, longitude

def commit(latitude, longitude):
	cluster_ref = db.reference(config.WORKING_BRANCH)
	timestamp = str(calendar.timegm(time.gmtime()))
	for i in range(len(latitude)):
		cluster_ref.child('clusters_' + timestamp).push().set({
			'latitude': latitude[i],
			'longitude': longitude[i]
		})

if __name__ == '__main__':
	latitude, longitude = compute()
	commit(latitude, longitude)
