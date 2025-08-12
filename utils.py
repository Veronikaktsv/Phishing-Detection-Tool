import re
import magic

def check_urls(text):
    score = 0
    reasons = []
    urls = re.findall(r'https?://[^\s]+', text)
    for url in urls:
        # Heuristic checks for suspicious URLs
        if len(url) > 75:
            score += 1
            reasons.append(f'Long URL: {url}')
        if re.search(r'\d+\.\d+\.\d+\.\d+', url):
            score += 2
            reasons.append(f'URL uses IP address: {url}')
        # Add more URL heuristics (e.g. check domain age with external API)
    return score, reasons

def check_attachments(msg):
    score = 0
    reasons = []
    for part in msg.iter_attachments():
        filename = part.get_filename() or ""
        # Suspicious extension check
        if filename.endswith(('.exe', '.scr', '.js', '.vbs')):
            score += 3
            reasons.append(f'Suspicious attachment extension: {filename}')
        # Check mime type using python-magic
        try:
            filetype = magic.from_buffer(part.get_payload(decode=True), mime=True)
            if filetype in ['application/x-msdownload', 'application/x-sh']:
                score += 3
                reasons.append(f'Suspicious attachment type: {filetype}')
        except Exception:
            pass
    return score, reasons
