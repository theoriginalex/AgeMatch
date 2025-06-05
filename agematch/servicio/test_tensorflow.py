import tensorflow as tf

print("TensorFlow version:", tf.__version__)
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])
model.summary()
