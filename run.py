from os import abort
import os
import requests

from werkzeug.wrappers import response
import extract_ppt
import text_to_image
import vedio_generation
import text_processing
import base64
from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask import send_from_directory
app = Flask(__name__)

path = ""
PORT = int(os.environ.get("PORT", 8000))
img_folder = "images"
vid_folder = "video"

@app.route('/upload_file', methods = ['POST'])
def get_file():
    if request.method == 'POST':
        f = request.files['file']
        path = ("ppt")
        f.save(path)
        
        ppt_ex = extract_ppt.data_extracter()
        # pre_pro = text_processing.process_text()

        pro_df , pro_data = ppt_ex.extract(path)
        img_gen = text_to_image.generate_images(img_folder)
        vid_gen  = vedio_generation.img_2_vid()

        res = False
        for sentence in pro_data:
            if(len(sentence.split())>2):
                res = img_gen.generate(sentence)
                
        if(res ==True):
            vid_gen.generate_video(img_folder,vid_folder)

        try:
            return "Generated"
        except Exception as e:
            return e

@app.route('/send_text', methods = ['POST','GET'])
def generate_by_text():
    text = request.get_json()["text"]
    pre_pro = text_processing.process_text()
    data , pro_data = pre_pro.process(text)

    img_gen = text_to_image.generate_images(img_folder)
    vid_gen  = vedio_generation.img_2_vid()

    res = False
    for sentence in pro_data:
        if(1):
            res = img_gen.generate_deepAi(sentence)
            
    if(res =="Generated"):

        vid_gen.generate_video(img_folder,vid_folder)

        for f in os.listdir(img_folder):
            os.remove(os.path.join(img_folder,f))
        return "Generated"
    else:
        return res


@app.route('/get_video', methods = ['GET'])
def send_video():
    
    with open(f"{vid_folder}/generated.avi", "rb") as video:
        encode = base64.b64decode(video.read())
        #for decoding
        # fh = open("video.mp4", "wb")
        # fh.write(base64.b64decode(str))
        # fh.close()
    response = {
        "video_base64" : str(encode),
        # "video_direct" : send_from_directory(vid_folder,"generated.avi")
    }
    try:
        return response #send_from_directory(vid_folder,"generated.avi")
    except Exception as e:
        return str(e)

if __name__=='__main__':
    app.run(port= 5000, debug=False )
    # http_server = WSGIServer(("", PORT), app)
    # http_server.serve_forever()







