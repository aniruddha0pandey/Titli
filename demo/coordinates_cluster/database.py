import config
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(config.KEY_PATH)

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': config.DATABASE_URL
})

ref = db.reference(config.WORKING_BRANCH)
snapshot = ref.child('104958581419633735554/').get()
all_keys = []
for i in snapshot.keys():
	all_keys.append(i)

coordinates = []

for i in all_keys:
	a = []
	a.append(float(snapshot[i]['latitude']))
	a.append(float(snapshot[i]['longitude']))
	coordinates.append(a)

