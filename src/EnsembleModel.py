from sklearn.ensemble import RandomForestClassifier

class EnsembleModel:
    def __init__(self):
        pass

    def build_ensemble_model(self):
        try:
            model = RandomForestClassifier(n_estimators=100)
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to build ensemble model: {e}")
