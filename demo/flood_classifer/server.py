import os
from flask import Flask, request, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
import predict
# import uuid
import time

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = './images'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload/<uid>', methods=['GET', 'POST'])
def upload(uid):
	if request.method == 'POST' and 'photo' in request.files:
		filename = photos.save(request.files['photo']) # + "___" + str(uuid.uuid4()) + "___" + str(uid)
		file_url = photos.url(filename)
		img_label = predict.main('./images/' + filename)
		return jsonify({
			uid: {
				"img_url": file_url,
				"img_label": img_label
			}
		}), 201
	return html

if __name__ == '__main__':
	# app.run(host='127.0.0.1', port=000, debug=True, threaded=True)
  app.run(debug=False)
