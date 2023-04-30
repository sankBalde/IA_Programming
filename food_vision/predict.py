import tensorflow as tf
import tensorflow_hub as hub
import sys
from utils import pred_and_print

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py image_filename")
        exit(1)
    Enter = sys.argv[1]

model = tf.keras.models.load_model("efficientnet_model.h5",
                                   custom_objects={'KerasLayer':hub.KerasLayer})

class_names = ['chicken_curry', 'chicken_wings', 'fried_rice', 'grilled_salmon',
               'hamburger', 'ice_cream', 'pizza', 'ramen', 'steak','sushi']

pred_and_print(model, Enter, class_names)