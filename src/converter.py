from keras.models import load_model
import tensorflowjs as tfjs

model = load_model('./output/trained_model/model.h5')
print("Model Loaded...\n")
tfjs.converters.save_keras_model(model, './coverted_model_tfjs')
print("Model Converted...\n")