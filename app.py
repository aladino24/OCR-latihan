from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import joblib
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

app = Flask(__name__)

# Load the pytesseract configuration and state from the saved model
loaded_pytesseract_state = joblib.load('pytesseract_model.pkl')
pytesseract.pytesseract.tesseract_cmd = loaded_pytesseract_state['tesseract_cmd']

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_information = ""

    if request.method == 'POST':
        # Handle file upload
        if 'file' in request.files:
            file = request.files['file']
            if file:
                # Save the uploaded image temporarily
                image_path = "temp_image.png"
                file.save(image_path)

                # Perform OCR on the uploaded image
                extracted_information = pytesseract.image_to_string(Image.open(image_path))

    return render_template('index.html', extracted_information=extracted_information)

if __name__ == '__main__':
    app.run(debug=True)
