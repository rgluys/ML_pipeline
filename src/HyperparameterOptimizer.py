from sklearn.model_selection import RandomizedSearchCV

class HyperparameterOptimizer:
    def __init__(self, model, param_space):
        self.model = model
        self.param_space = param_space

    def optimize(self, X, y):
        try:
            optimizer = RandomizedSearchCV(estimator=self.model, param_distributions=self.param_space, n_iter=10, random_state=42)
            optimizer.fit(X, y)
            return optimizer.best_params_
        except Exception as e:
            raise RuntimeError(f"Failed to optimize hyperparameters: {e}")
