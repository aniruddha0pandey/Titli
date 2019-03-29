from sklearn.cluster import MeanShift, estimate_bandwidth

coordinates = []

def fetch_coordinates(args):
	coordinates = args
	ms = MeanShift()
	ms.fit(coordinates)
	cluster_centers = ms.cluster_centers_
	return cluster_centers
