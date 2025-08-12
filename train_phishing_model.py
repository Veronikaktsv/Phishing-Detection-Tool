import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import re

def extract_features_from_text(text):
    url_pattern = r'http[s]?://\S+'
    urls = re.findall(url_pattern, text.lower())
    suspicious_keywords = ['urgent', 'password', 'verify', 'update', 'click', 'login']
    keyword_count = sum(text.lower().count(word) for word in suspicious_keywords)
    return [len(urls), keyword_count, len(text)]

def main():
    df = pd.read_csv('data/phishing_samples.csv')
    df['features'] = df['email_text'].apply(extract_features_from_text)
    df[['url_count', 'keyword_count', 'email_length']] = pd.DataFrame(df['features'].tolist(), index=df.index)

    X = df[['url_count', 'keyword_count', 'email_length']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)
    print(f'Model accuracy: {acc:.2f}')

    with open('models/phishing_model.pkl', 'wb') as f:
        pickle.dump(clf, f)

if __name__ == '__main__':
    main()
