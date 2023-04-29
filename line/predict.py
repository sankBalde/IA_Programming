import tensorflow as tf
from line import model_1, model_2

# Load model_1
model_1 = tf.keras.models.load_model("model_1.h5")

# Load model_2
model_2 = tf.keras.models.load_model("model_2.h5")

# Trying to predict X = 17
print("Model 1 predict X = 17 :",model_1.predict([17.0])[0][0])
# Our model seems good with an mae if 0.2204

#Model 2 with SGD optimizer
print("Model 2 predict X = 17 :",model_2.predict([17.0])[0][0])

"""
Model 1 predict X = 17 : 27.21035
Model 2 predict X = 17 : 27.138983

Conclusion : Model 2 is better than Model 1
"""