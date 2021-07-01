# from big_sleep import Imagine
# CUDA_LAUNCH_BLOCKING=1
# dream = Imagine(
#     text = "fire in the sky",
#     lr = 5e-2,
#     save_every = 25,
#     save_progress = True
# )

# dream()

from deep_daze import Imagine
import torch
torch.cuda.empty_cache()

imagine = Imagine(
    text = 'cosmic love and attention',
    image_width=256,
    num_layers=16,
    batch_size=1,
    gradient_accumulate_every=16
)
imagine()

class generate_images:
    def __init__(self) -> None:
        self.generator = Imagine(
                                    image_width=256,
                                    num_layers=16,
                                    batch_size=1,
                                    gradient_accumulate_every=16
                                    )

    def generate(self,text):

        self.generator(text)
        return self.generator

