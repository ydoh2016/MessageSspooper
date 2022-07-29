from flask import Flask, render_template, request

from werkzeug.utils import secure_filename

import datetime
import os

SAVEPATH = ['0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000']

app = Flask(__name__)

@app.route('/send_images', methods = ['POST'])
def send_images():
    if request.method == 'POST':
        f = request.files["img"]
        savepath = os.path.join('static', 'images', datetime.datetime.now().strftime("%m%d%H%M%S%f") + '.png')
        f.save(savepath)
        SAVEPATH.append(savepath)
        if len(SAVEPATH) > 8:
            if os.path.exists(SAVEPATH[0]):
                os.remove(SAVEPATH[0])
            del SAVEPATH[0]
        return 'image saved.'

@app.route('/show_images', methods = ['GET'])
def show_images():
    print(SAVEPATH)
    return render_template('show_images.html', value = SAVEPATH)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)