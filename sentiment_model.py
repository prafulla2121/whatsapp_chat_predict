import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import joblib

# Load the dataset
df = pd.read_csv("Twitter_Data.csv")

# Rename columns for consistency
df = df.rename(columns={'clean_text': 'message', 'category': 'sentiment'})

# Check for any missing values and drop them (optional cleanup)
df = df.dropna(subset=['message', 'sentiment'])

# Features and labels
X = df['message']
y = df['sentiment']

# Text vectorization using TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
X_vec = vectorizer.fit_transform(X)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on test data
y_pred = rf_model.predict(X_test)

# Print classification report
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
joblib.dump(rf_model, "/mnt/data/rf_sentiment_model.pkl")
joblib.dump(vectorizer, "/mnt/data/tfidf_vectorizer.pkl")
