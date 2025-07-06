import tensorflow as tf
from tensorflow.keras.applications import ResNet50, resnet50
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the ResNet50 model with pretrained weights
model = ResNet50(weights='imagenet')

# Function to classify a given image
def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = resnet50.preprocess_input(x)

    preds = model.predict(x)
    decoded = resnet50.decode_predictions(preds, top=3)[0]
    return [(label, prob) for (_, label, prob) in decoded]
