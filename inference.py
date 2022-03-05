import matplotlib.pyplot as plt
# import IPython.display as ipd
import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
import commons
import utils
from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models1 import SynthesizerTrn
from text.symbols import symbols
from text.text import label_to_fusion_sequence, _speaker_to_id
import librosa
from scipy.io.wavfile import write

def get_text(text):
    # text_norm = text_to_sequence(text, hps.data.text_cleaners)
    text_norm = label_to_fusion_sequence(text)
    # if hps.data.add_blank:
        # text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm
hps = utils.get_hparams_from_file("./configs/my_base.json")
# net_g = SynthesizerTrn(
#     len(symbols),
#     hps.data.filter_length // 2 + 1,
#     hps.train.segment_size // hps.data.hop_length,
#     **hps.model).cuda()
net_g = SynthesizerTrn(
    hps,
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    **hps.model).cuda()
_ = net_g.eval()
modelpath="logs/ljs_base/G_510000.pth"
model_prefix=modelpath.split('/')[-1].split('.')[0]
if not os.path.exists(model_prefix):
        os.mkdir(model_prefix)
_ = utils.load_checkpoint(modelpath, net_g, None)

# outdir = 'output/'
test_dirs = '/home/research/data/tts_raw_data/miaomiao/labels'
files = os.listdir(test_dirs)

with torch.no_grad():
     for file in files[:10]:
        filename = test_dirs + "/" + file
        stn_tst = get_text(filename)
        x_tst = stn_tst.cuda().unsqueeze(0)
        x_tst_lengths = torch.LongTensor([x_tst.size(2)]).cuda()
        print(stn_tst.shape, x_tst.shape, x_tst_lengths)
        audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
        print('wav shape: ', audio.shape)
        basename = os.path.basename(filename).split(".")[0]

        output_name = model_prefix + "/" + basename + ".wav"
        librosa.output.write_wav(output_name, audio, hps.data.sampling_rate)
# ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))
