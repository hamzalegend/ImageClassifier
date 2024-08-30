import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

import os

imageTrainSize = 500
Epochs = 10

# Set up the paths
# Replace with your main folder path
base_dir = os.path.join(os.getcwd(), "raw_data")

# Data preprocessing
datagen = ImageDataGenerator(
    rescale=1.0/255,        # Rescale pixel values
    validation_split=0.2    # Split 20% for validation
)

# Load training data
train_data = datagen.flow_from_directory(
    base_dir,
    # Resize images to 150x150
    target_size=(imageTrainSize, imageTrainSize),
    batch_size=32,              # Number of images per batch
    class_mode='categorical',   # Multiclass classification
    subset='training'
)

# Load validation data
val_data = datagen.flow_from_directory(
    base_dir,
    target_size=(imageTrainSize, imageTrainSize),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(
        imageTrainSize, imageTrainSize, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    # Output layer for classification
    Dense(train_data.num_classes, activation='softmax')
])

# Compile the model
model.compile(
    optimizer=Adam(),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=Epochs  # Increase this for better results
)

# Save the model to disk
model.save('model.keras')
print("Model saved as 'model.keras'")
