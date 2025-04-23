from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load the trained model
model = load_model('handwriting_model.h5')  # Ensure the model is saved in Handwriting.py

def preprocess_image(image_path):
    """
    Preprocess the input image to match the model's input requirements.
    """
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((32, 32))  # Resize to 32x32
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.stack((img,)*3, axis=-1)  # Convert to 3 channels
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def predict_handwriting(image_path):
    """
    Predict the handwritten digit from the input image.
    """
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)
    predicted_digit = np.argmax(prediction)
    return predicted_digit

# Example usage
if __name__ == "__main__":
    image_path = "C:\Users\kimvi\Downloads\pp0259_1-66266.png"  # Replace with the path to your image
    result = predict_handwriting(image_path)
    print(f"Predicted digit: {result}")
