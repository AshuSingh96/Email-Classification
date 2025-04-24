import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

from utils import clean_text

def train_and_save_model(data_path="data/combined_emails.csv", model_path="model_pipeline.pkl"):
    # Load dataset
    df = pd.read_csv(data_path)

    # Drop nulls and clean
    df.dropna(subset=["email", "label"], inplace=True)
    df["cleaned_email"] = df["email"].apply(clean_text)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        df["cleaned_email"], df["label"], test_size=0.2, random_state=42
    )

    # Pipeline
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Train
    pipe.fit(X_train, y_train)

    # Evaluate
    y_pred = pipe.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Report:\n", classification_report(y_test, y_pred))

    # Save model
    joblib.dump(pipe, model_path)
    print(f"Model saved to {model_path}")

def load_model(model_path="model_pipeline.pkl"):
    return joblib.load(model_path)
