from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class MetricsEvaluator:
    def __init__(self):
        pass

    def calculate_metrics(self, y_true, y_pred):
        try:
            metrics = {
                'accuracy': accuracy_score(y_true, y_pred),
                'precision': precision_score(y_true, y_pred),
                'recall': recall_score(y_true, y_pred),
                'f1_score': f1_score(y_true, y_pred)
            }
            return metrics
        except Exception as e:
            raise RuntimeError(f"Failed to calculate evaluation metrics: {e}")
