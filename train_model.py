from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load example dataset
X, y = load_iris(return_X_y=True)

model = RandomForestClassifier()
model.fit(X, y)  # type: ignore

joblib.dump(model, "model.joblib")
