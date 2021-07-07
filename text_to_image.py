# from big_sleep import Imagine
# CUDA_LAUNCH_BLOCKING=1
# dream = Imagine(
#     text = "fire in the sky",
#     lr = 5e-2,
#     save_every = 25,
#     save_progress = True
# )

# dream()

from sys import path
from deep_daze import Imagine
from deep_daze.deep_daze import open_folder
import torch
torch.cuda.empty_cache()

# imagine = Imagine(
#     text = 'cosmic love and attention',
#     image_width=256,
#     num_layers=16,
#     batch_size=1,
#     gradient_accumulate_every=16
# )
# imagine()

class generate_images:
    def __init__(self,path) -> None:
        self.path = path

    def generate(self,text):
        image = Imagine(text=text,
                                    open_folder = path,
                                    image_width=256,
                                    num_layers=16,
                                    batch_size=1,
                                    save_every=4,
                                    save_progress=True,
                                    save_date_time=True,
                                    save_video=True,
                                    gradient_accumulate_every=16
                                    )
        
        return "Generated"

