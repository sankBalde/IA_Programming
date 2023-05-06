import tensorflow as tf
import sys
from utils import pred_and_print

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py image_filename")
        exit(1)
    Enter = sys.argv[1]

model = tf.keras.models.load_model("best_model.h5")
class_names = ['pizza', 'steak']

pred_and_print(model, Enter, class_names)
