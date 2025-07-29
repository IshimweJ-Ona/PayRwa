import requests
import pytesseract
from PIL import Image
import io

def generate_qr(data):
    url = f"https://api.qrserver.com/v1/create-qr-code/?data={data}&size=150x150"
    return url

def read_qr(file):
    try:
        image = Image.open(file)
        result = pytesseract.image_to_string(image)
        return {'data': result}
    except Exception as e:
        return {'error': str(e)}
    