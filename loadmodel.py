import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
def get_prediction_string(path):  
    model = keras.models.load_model('potholenew.h5')
    img_path = path 
    img = image.load_img(img_path,
    . target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)

    predicted_index = np.argmax(predictions)
    print(predictions)
    print(predicted_index)
    print(f"Predicted Index: {predicted_index}")
    if predicted_index == predictions[0]:
        return 'Pathole'
    else:
        return 'Road'
# get_prediction_string(path)
