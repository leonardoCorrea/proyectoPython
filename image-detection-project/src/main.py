# FILE: /image-detection-project/image-detection-project/src/main.py
import tensorflow as tf
from model import NeuralNetwork
from data.dataset import Dataset
from utils import preprocess_image, visualize_results

def main():
    # Initialize the neural network model
    model = NeuralNetwork()
    model.build_model()

    # Load the dataset
    dataset = Dataset()
    train_data, test_data = dataset.load_data()

    # Preprocess the images
    train_data = preprocess_image(train_data)
    test_data = preprocess_image(test_data)

    # Train the model
    model.train(train_data)

    # Make predictions
    predictions = model.predict(test_data)

    # Visualize results
    visualize_results(predictions)

if __name__ == "__main__":
    main()