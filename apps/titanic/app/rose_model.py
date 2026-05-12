class RoseModel:
    def __init__(self) -> None:
        self.model = None
        self.import_error = None
        try:
            from sklearn.tree import DecisionTreeClassifier
            self.model = DecisionTreeClassifier()
        except ModuleNotFoundError as exc:
            self.import_error = str(exc)

    def get_model_name(self):
        if self.model is None:
            return None
        return type(self.model).__name__

    def get_status(self):
        return {
            "available": self.model is not None,
            "error": self.import_error,
        }

   