from sklearn.utils.class_weight import compute_class_weight

class ImbalanceHandler:
    def __init__(self, strategy='class_weights'):
        self.strategy = strategy

    def handle_imbalance(self, X, y):
        try:
            if self.strategy == 'class_weights':
                class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
                return {c: w for c, w in zip(np.unique(y), class_weights)}
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Failed to handle class imbalance: {e}")
