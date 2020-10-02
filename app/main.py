from flask import Flask, render_template, request, flash, redirect, url_for
#from ascii_art import ReturnImage
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import os
import secrets


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
os.makedirs(UPLOAD_FOLDER,  exist_ok=True)

secret = secrets.token_urlsafe(32)
app.secret_key = secret

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def getAverage(image):
    im = np.array(image)
    s = im.shape
    w = s[0]
    h = s[1]
    return np.average(im.reshape(w*h))

def ReturnImage(image, cols=200, scale=0.43, inverted="off", gsc=1):
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gscale2 = "@%#*+=-:. "

    gscale = gscale1 if gsc == 1 else gscale2
    #cols = 200
    #scale = 0.43
    #image = Image.open("static/img/header_img.png").convert("L")
    W, H = image.size[0], image.size[1]
    cols = W if cols > W else cols
    scale = W if scale > W else scale
    w = W/cols
    h = w/scale
    rows = int(H/h)

    aimg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        if j == rows - 1:
            y2 = H

        aimg.append("")

        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)

            if i == cols-1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))
            avg = 0

            if(inverted == None):
                avg = int(getAverage(img))    
            else:
                avg = 255 - int(getAverage(img))

            gsval = gscale[int((avg*(len(gscale) - 1))/255)]                
            aimg[j] += gsval
    return aimg

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=["GET", "POST"])
def upload_image():
    if 'image_disc' not in request.files or "image_web" not in request.files:
            return redirect(url_for('index'))
    if request.files:
        img = request.files["image_disc"]    
        if img.filename == '':
            err = "No file attached"
            flash(err)
            return redirect(url_for('index', err=err))
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            path_to_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(filename)
            img.save(path_to_file)
            image = Image.open(path_to_file).convert("L")
            
            cols = int(request.form.get("cols"))
            scale = float(request.form.get("scale"))
            invert = request.form.get("invert")
            print(invert)
            gsc = int(request.form.get("gscaler"))
           
            a = ReturnImage(image, cols, scale, invert, gsc)
            os.remove(path_to_file)
            return render_template("upload_image.html", a=a, filename=filename)
        else:
            err = "Wrong file name"
            return redirect('/')
    else:
        return render_template('index.html')