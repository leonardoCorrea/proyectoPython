class NeuralNetwork:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        import tensorflow as tf
        from tensorflow.keras import layers, models

        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))  # Assuming 10 classes for classification

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, train_data, train_labels, epochs=10):
        self.model.fit(train_data, train_labels, epochs=epochs)

    def predict(self, images):
        return self.model.predict(images)