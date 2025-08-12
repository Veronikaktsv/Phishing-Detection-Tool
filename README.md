# Phishing Detection Tool

A Python tool to analyze emails for phishing attempts by inspecting headers, URLs, and attachments. Combines heuristic rules with a simple ML model for classification.

## Features
- Email header analysis: SPF, DKIM, sender reputation hints
- URL checks: domain reputation, suspicious patterns
- Attachment checks: file type and extension heuristics
- ML-based classification with logistic regression
- CLI to scan raw email files or text input

## Setup
1. Clone repo and create virtual environment
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    
4. Train model on provided dataset or use pretrained `models/phishing_model.pkl`

## Usage

`python phishing_detector.py --email-file data/test_emails/sample1.eml`

## Data
- `data/phishing_samples.csv` contains labeled phishing and benign emails for training/testing

## License
MIT License
