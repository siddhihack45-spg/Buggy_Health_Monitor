
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


class BuggyDetector:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=42
        )
        self.is_trained = False

    def train(self):
        # Generate demonstration data.
        # This is NOT real buggy sensor data.
        X, y = make_classification(
            n_samples=300,
            n_features=3,
            n_informative=3,
            n_redundant=0,
            n_classes=2,
            random_state=42
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        self.model.fit(X_train, y_train)
        self.is_trained = True

        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        print("\n--- MODEL TRAINING ---")
        print("Training completed!")
        print("Demo accuracy:", round(accuracy, 3))
        print("Number of trees:", len(self.model.estimators_))

    def predict(self, readings):
        if not self.is_trained:
            raise RuntimeError("Train or load the model first")

        prediction = self.model.predict([readings])[0]
        probabilities = self.model.predict_proba([readings])[0]
        confidence = max(probabilities) * 100

        if prediction == 0:
            condition = "NORMAL"
        else:
            condition = "WARNING"

        return condition, round(confidence, 2)

    def save(self):
        if not self.is_trained:
            raise RuntimeError("Train the model first")

        joblib.dump(self.model, "random_forest.pkl")
        print("Model saved as random_forest.pkl")

    def load(self):
        self.model = joblib.load("random_forest.pkl")
        self.is_trained = True
        print("Model loaded successfully")