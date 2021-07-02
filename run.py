from os import abort
import os
import extract_ppt
import text_to_image
import vedio_generation
import text_processing

from flask import Flask, render_template, request
from werkzeug import secure_filename
from gevent.pywsgi import WSGIServer
from flask import send_from_directory
app = Flask(__name__)

path = ""
PORT = int(os.environ.get("PORT", 3000))
img_folder = "images"
vid_folder = "video"

@app.route('/upload_file', methods = ['POST','GET'])
def get_file():
    if request.method == 'POST':
        f = request.files['file']
        path = secure_filename(f.filename)
        f.save(path)
        
        ppt_ex = extract_ppt.data_extracter()
        pre_pro = text_processing.process_text()

        pro_df , pro_data = ppt_ex.extract(path)
        data , pro_data = pre_pro.process(pro_data)

        img_gen = text_to_image.generate_images(img_folder)
        vid_gen  = vedio_generation.img_2_vid()

        res = False
        for sentence in pro_data:
            if(len(sentence.split())>2):
                res = img_gen.generate(sentence)
                
        if(res ==True):
            vid_gen.generate_video(img_folder,vid_folder)

        try:
            return send_from_directory(vid_folder,"generated.avi")
        except FileNotFoundError:
            abort(404)


if __name__=='__main__':
    app.run(debug=True)
    http_server = WSGIServer(("", PORT), app)
    http_server.serve_forever()






