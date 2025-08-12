import os
import sys
import email
import argparse
import re
import tldextract
import pandas as pd
import joblib
from utils import check_urls, check_attachments

def parse_email(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)
    headers = dict(msg.items())
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            if ctype == 'text/plain':
                body += part.get_payload(decode=True).decode(errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')
    return headers, body, msg

def heuristic_checks(headers, body, msg):
    score = 0
    reasons = []

    # Check SPF and DKIM pass/fail
    spf = headers.get('Received-SPF', '').lower()
    if 'fail' in spf:
        score += 2
        reasons.append('SPF fail')

    dkim = headers.get('Authentication-Results', '').lower()
    if 'dkim=fail' in dkim:
        score += 2
        reasons.append('DKIM fail')

    # Check sender domain suspicious
    from_addr = headers.get('From', '')
    domain = tldextract.extract(from_addr).registered_domain
    if domain.endswith('.xyz') or domain.endswith('.top'):
        score += 1
        reasons.append('Suspicious sender domain')

    # Check URLs in body
    url_score, url_reasons = check_urls(body)
    score += url_score
    reasons.extend(url_reasons)

    # Check attachments
    attach_score, attach_reasons = check_attachments(msg)
    score += attach_score
    reasons.extend(attach_reasons)

    return score, reasons

def ml_predict(features):
    model = joblib.load('models/phishing_model.pkl')
    pred = model.predict(features)
    return pred[0]

def extract_features(headers, body, msg):
    # Extract features like number of URLs, suspicious attachments count, length of email, etc.
    num_urls = len(re.findall(r'https?://', body))
    attach_count = sum(1 for _ in msg.iter_attachments())
    # Add other features as needed
    features = pd.DataFrame({'num_urls':[num_urls], 'attach_count':[attach_count]})
    return features

def main():
    parser = argparse.ArgumentParser(description="Phishing Detection Tool")
    parser.add_argument('--email-file', required=True, help='Path to email file (.eml)')
    args = parser.parse_args()

    headers, body, msg = parse_email(args.email_file)
    score, reasons = heuristic_checks(headers, body, msg)
    features = extract_features(headers, body, msg)
    prediction = ml_predict(features)

    print("Heuristic phishing score:", score)
    print("Reasons:", reasons)
    print("ML Model prediction:", "Phishing" if prediction==1 else "Benign")

if __name__ == '__main__':
    main()
