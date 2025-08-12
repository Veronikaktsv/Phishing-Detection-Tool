import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Sample training data (you can expand this)
data = [
    {"text": "Click this link http://bad-domain.xyz now", "label": 1},
    {"text": "Verify your account immediately", "label": 1},
    {"text": "Meeting schedule for next week", "label": 0},
    {"text": "Please find attached report", "label": 0},
    {"text": "Urgent: Update your password at http://phishingsite.com", "label": 1},
    {"text": "Let's have lunch tomorrow", "label": 0},
]

df = pd.DataFrame(data)

X = df['text']
y = df['label']

# Create a simple pipeline: CountVectorizer + LogisticRegression
pipeline = Pipeline([
    ('vect', CountVectorizer(ngram_range=(1,2))),
    ('clf', LogisticRegression(solver='liblinear'))
])

# Train model
pipeline.fit(X, y)

# Make sure models directory exists
os.makedirs('models', exist_ok=True)

# Save model
joblib.dump(pipeline, 'models/phishing_model.pkl')

print("Model trained and saved to models/phishing_model.pkl")
