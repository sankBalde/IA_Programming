import tensorflow as tf
import numpy as np


# First Example
x = np.array([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])

y = np.array([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

# Transform array to tensors
X = tf.cast(tf.constant(x), dtype=tf.float32)
Y = tf.cast(tf.constant(y), dtype=tf.float32)

# Our first model to predict the relationship between X and Y with Adam optimizer
# We know that Y = X + 10 but we let him learn it
def model_1():
    tf.random.set_seed(42)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(50, activation=None),

        tf.keras.layers.Dense(1)
        ])

    model.compile(loss="mae",
              optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.01),
              metrics=["mae"])

    model.fit(tf.expand_dims(X, axis=-1), y, epochs=100, verbose=0)
    model.save("model_1")
    return model


# Second Example
A = tf.range(-100,100,4)
B = A + 10

A_train = A[:40]
B_train = B[:40]


A_test = A[40:]
B_test = B[40:]

def model_2():
    tf.random.set_seed(42)

    model = tf.keras.Sequential([

    tf.keras.layers.Dense(10, input_shape=[1], name="input_layer"),
    tf.keras.layers.Dense(1, name="ouput_layer")
        ], name="model_1")

    model.compile(loss="mae",
              optimizer=tf.keras.optimizers.legacy.SGD(),
              metrics=["mae"])

    model.fit(A_train, B_train, epochs=100, verbose=0)
    model.save("model_2")
    return model

# Build the 2 models
model_1()
model_2()
