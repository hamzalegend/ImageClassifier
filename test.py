import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained model
model = load_model('model.keras')

test_folder = os.path.join(os.getcwd(), "test")


test_images = [os.path.join(test_folder, img) for img in os.listdir(
    test_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]


def predict_image(image_path, model):
    img = load_img(image_path, target_size=(500, 500))
    img_array = img_to_array(img) / 255.0  # Normalize pixel values

    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    return predicted_class, confidence


class_labels = ["Boat", "car", "bike", "motorccycle", "scoter"]

# Plot the test images with their predictions
plt.figure(figsize=(12, 8))

for i, img_path in enumerate(test_images):
    # Predict the class of each image
    predicted_class, confidence = predict_image(img_path, model)
    class_name = class_labels[predicted_class]

    # Plot the image and the prediction
    plt.subplot(5, 1, i + 1)  # Adjust subplot grid as needed
    plt.imshow(load_img(img_path))
    plt.title(f"Predicted: {class_name} ({confidence:.2f})")
    plt.axis('off')

plt.tight_layout()
plt.show()
