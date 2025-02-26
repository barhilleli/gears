"""
Install ----------------------------------------------------------------------------------------------------------------
conda create -n temp python=3.11
conda activate temp
pip install flask
pip install flask flask-cors

For https connection ---------------------------------------------------------------------------------------------------
Did this in terminal:
openssl genpkey -algorithm RSA -out privkey.pem
openssl req -new -key privkey.pem -out cert.csr
openssl x509 -req -in cert.csr -signkey privkey.pem -out cert.pem

Where to put things ----------------------------------------------------------------------------------------------------
A single folder:
img1.jpeg
img2.jpeg
app.py
cert.pem
privkey.pem
cert.csr

Run --------------------------------------------------------------------------------------------------------------------
from inside the folder, do:
python app.py

Usage ------------------------------------------------------------------------------------------------------------------
In my web-browser do
    https://localhost:8000/images/20241010_175114.jpg

In https://gears.aposteriori.com.sg/builder.html do:
    Insert in the imageURL box:
    imageURL = https://192.168.1.5:8000/images/20241010_175114.jpg
"""
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for the specific domain
CORS(app, origins="https://gears.aposteriori.com.sg")

@app.route('/images/<filename>')
def serve_image(filename):
    # Adjust this to the directory where your image files are located
    image_directory = 'images/'
    return send_from_directory(image_directory, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, ssl_context=('cert.pem', 'privkey.pem'))
