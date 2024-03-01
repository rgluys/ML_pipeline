import tensorflow as tf
from prometheus_client import Counter

class ModelProcessor:
    def __init__(self, gpu=False):
        self.gpu = gpu
        self.model_trained_counter = Counter('model_trained_counter', 'Number of times model is trained')

    def train_model(self, X, y):
        try:
            # Train model...
            self.model_trained_counter.inc()
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to train model: {e}")

    def evaluate_model(self, model, X, y):
        try:
            # Evaluate model...
            return accuracy
        except Exception as e:
            raise RuntimeError(f"Failed to evaluate model: {e}")
