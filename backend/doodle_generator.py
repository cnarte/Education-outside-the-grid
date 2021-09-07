import spacy_universal_sentence_encoder
from quickdraw import QuickDrawData
nlp = spacy_universal_sentence_encoder.load_model('en_use_lg')
qd = QuickDrawData()
from quickdraw import QuickDrawDataGroup
import datetime
def doodle(text):
    doc_1 = nlp(text)
    score = {}
    for a in list(qd.drawing_names):
        doc_2 = nlp(a)
        score[a] = doc_1.similarity(doc_2)
    cat = sorted(score)
    doodle_cat = "bird"
    ants = QuickDrawDataGroup(doodle_cat)
    ant = ants.get_drawing()
    name = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    ant.image.save(f"frontend/src/assets/doodle/{name}.jpg")

import os
import cv2
from PIL import Image

class doodle_2_vid():
    def __init__(self) -> None:
        pass
    def find_mean_shape(self, path):
        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(path))

        for file in os.listdir(path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
                im = Image.open(os.path.join(path, file))
                width, height = im.size
                mean_width += width
                mean_height += height

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)
        return mean_height, mean_width


    def resize(self, path):
        mean_height, mean_width = self.find_mean_shape(path)

        for file in os.listdir(path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):

                im = Image.open(os.path.join(path, file))
                os.remove(os.path.join(path, file))

                width, height = im.size
                print(width, height)

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(path, file), "JPEG", quality=100)

                print(im.filename.split("\\")[-1], " is resized")


    def generate_video(self, in_path, out_path):
        image_folder = in_path
        video_name = os.path.join(out_path, "doodle.avi")

        self.resize(image_folder)
        images = [
            img
            for img in os.listdir(image_folder)
            if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")
        ]

        print(images)

        frame = cv2.imread(os.path.join(image_folder, images[0]))

        height, width, layers = frame.shape
        # fourcc = cv2.VideoWriter_fourcc(*'FMP4')
        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        output = "generated"
        os.popen("ffmpeg -y -i 'frontend/src/assets/video/doodle.avi' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'frontend/src/assets/video/doodle.mp4'")

# generate_video("images", "video")


# doodle("dog running ground")