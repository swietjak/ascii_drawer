from flask import Flask, render_template, request
from ascii_art import ReturnImage
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=["POST"])
def upload_image():
    print("hello")
    print(request.files)
    if request.files:
        img = request.files["image"]    
        filename = secure_filename(img.filename)
        print(img)
        img.save(filename)
        image = Image.open(filename).convert("L")
        a = ReturnImage(image)
        os.remove(filename)
        return render_template("upload_image.html", a=a)
    else:
        return render_template('index.html')