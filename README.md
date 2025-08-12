# Phishing Detection Tool

This project implements a simple phishing detection tool using basic machine learning. It analyzes email text files to identify phishing attempts based on URLs, suspicious keywords, and email length.

---

## Features

- Parses email files (`.eml`) for analysis.
- Checks URLs and attachments for suspicious patterns.
- Uses a trained ML model to classify emails as phishing or legitimate.
- Provides confidence scores for predictions.

---

## Requirements

- Python 3.7 or higher
- Packages listed in `requirements.txt`

---

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Veronikaktsv/Phishing-Detection-Tool.git
    cd Phishing-Detection-Tool
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Prepare your dataset:
   - Place phishing and legitimate email samples in `data/phishing_samples.csv`.
   - Place emails to analyze in `data/test_emails/` as `.eml` files.

4. Train the model:

    ```bash
    python train_phishing_model.py
    ```

5. Run phishing detection on test emails:

    ```bash
    python detect_phishing.py --email_file data/test_emails/sample_email_1.eml
    ```

---

## Usage Examples

### Testing the Phishing Detection Tool

You can test the tool using sample email files stored in the `data/test_emails/` folder.

- Example command to run the detection on a test email:

    ```bash
    python detect_phishing.py --email_file data/test_emails/sample_email_1.eml
    ```

### Sample Test Emails and Expected Outputs

| Test Email Filename  | Description                          | Expected Output                             |
| -------------------- | ---------------------------------- | ------------------------------------------ |
| `sample_email_1.eml` | Legitimate email from trusted source | `Prediction: Legitimate (Confidence: 0.95)` |
| `sample_email_2.eml` | Phishing email with suspicious URL   | `Prediction: Phishing (Confidence: 0.89)`   |
| `sample_email_3.eml` | Email with suspicious attachment     | `Prediction: Phishing (Confidence: 0.92)`   |
| `sample_email_4.eml` | Legitimate newsletter email          | `Prediction: Legitimate (Confidence: 0.88)` |

---

## License

This project is licensed under the [MIT License](LICENSE).
