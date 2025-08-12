import os
import pickle
import re

MODEL_PATH = 'models/phishing_model.pkl'
TEST_EMAILS_DIR = 'data/test_emails/'

def extract_features_from_text(text):
    url_pattern = r'http[s]?://\S+'
    urls = re.findall(url_pattern, text.lower())
    suspicious_keywords = ['urgent', 'password', 'verify', 'update', 'click', 'login']
    keyword_count = sum(text.lower().count(word) for word in suspicious_keywords)
    return [len(urls), keyword_count, len(text)]

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

def analyze_email(filepath, model):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    features = extract_features_from_text(text)
    prediction = model.predict([features])[0]
    label = 'Phishing' if prediction == 1 else 'Legitimate'
    print(f"{os.path.basename(filepath)}: {label}")

def main():
    model = load_model()
    print("Starting phishing detection on test emails...\n")
    for filename in os.listdir(TEST_EMAILS_DIR):
        if filename.endswith('.txt'):
            analyze_email(os.path.join(TEST_EMAILS_DIR, filename), model)

if __name__ == '__main__':
    main()
