import os
from PIL import Image
from flask import url_for, current_app

def add_image(pic_upload):
    filename_WS = pic_upload.filename
    filename = filename_WS.replace(" ","-")
    filepath = os.path.join(current_app.root_path,'static/images',filename)

    pic = Image.open(pic_upload)
    pic.save(filepath)

    return filename