# Phishing Detection Tool

This project implements a simple phishing detection tool using basic machine learning. It analyzes email text files to identify phishing attempts based on URLs, suspicious keywords, and email length.

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt

2. Prepare your dataset:
- Place phishing and legitimate email samples in data/phishing_samples.csv.
- Place emails to analyze in data/test_emails/ as .txt files.

3. Train the model:
   
     ```bash
    python train_phishing_model.py

4. Run phishing detection on test emails:

     ```bash
     python phishing_detection.py

## License

This project is licensed under the [MIT License](LICENSE).
