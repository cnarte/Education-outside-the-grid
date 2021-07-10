
from sys import path
from deep_daze import Imagine
from deep_daze.deep_daze import open_folder
from nltk.corpus.reader.chasen import test
import torch
import datetime
torch.cuda.empty_cache()
import requests



class generate_images:
    def __init__(self,path) -> None:
        self.path = path

    def generate_gans(self,text):
        try:
            generator = Imagine(text=text,
                                        open_folder = self.path,
                                        image_width=512,
                                        num_layers=16,
                                        batch_size=1,
                                        # save_every=4,
                                        # save_progress=True,
                                        save_date_time=True,
                                        # save_video=True,
                                        gradient_accumulate_every=16
                                        )
            return "Generated"
        except Exception as e:       
            return str(e)
    
    def generate_deepAi(self,text):
        try:
            response_0 = requests.post(
                    "https://api.deepai.org/api/text2img",
                    data={
                        'text': text,
                    },
                    headers={'api-key': '883c4b05-07e0-4f69-997b-cba002252a30'}
                )
            response_0 = response_0.json()
            name = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
            download = requests.get(response_0['output_url'])
            open(f"{self.path}/{name}.jpg",'wb').write(download.content)

            return "Generated"
        except Exception as e:
             return str(e)   



