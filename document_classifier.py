import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def train_classifier():
    # Load dataset
    df = pd.read_csv('large_dummy_legal_dataset.csv')

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

    # Vectorization with proper handling of unseen words
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Logistic Regression Model
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_tfidf, y_train)

    # Predictions
    y_pred = clf.predict(X_test_tfidf)

    # Evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the model and vectorizer
    joblib.dump(clf, 'legal_document_classifier.joblib')
    joblib.dump(vectorizer, 'legal_document_vectorizer.joblib')

def classify_document(text):
    if not os.path.exists('legal_document_classifier.joblib') or not os.path.exists('legal_document_vectorizer.joblib'):
        raise FileNotFoundError("Classifier or vectorizer not found. Please train the model first.")
    
    clf = joblib.load('legal_document_classifier.joblib')
    vectorizer = joblib.load('legal_document_vectorizer.joblib')

    text_tfidf = vectorizer.transform([text])
    document_type = clf.predict(text_tfidf)[0]

    return document_type

if __name__ == "__main__":
    train_classifier()
    
    # Test the classifier
    test_text = "This is a Special Leave Petition filed under Article 136 challenging the High Court's order."
    print(f"Test classification: {classify_document(test_text)}")
