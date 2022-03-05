#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import numpy as np
from .input_encoding import phone_set, tone_set, \
    wordcateg_set, prosody_set, speaker_set

# Mappings from symbol to numeric ID and vice versa:
_phone_to_id = {p: i for i, p in enumerate(phone_set)}#len=149
_id_to_phone = {i: p for i, p in enumerate(phone_set)}
_tone_to_id = {t: i for i, t in enumerate(tone_set)}#len=13
_id_to_tone = {i: t for i, t in enumerate(tone_set)}
_categ_to_id = {c: i for i, c in enumerate(wordcateg_set)}#len=6
_id_to_categ = {i: c for i, c in enumerate(wordcateg_set)}
_prsd_to_id = {p: i for i, p in enumerate(prosody_set)}#len=7
_id_to_prsd = {i: p for i, p in enumerate(prosody_set)}
_speaker_to_id= {p: i for i, p in enumerate(speaker_set)}
_id_to_speaker= {i: p for i, p in enumerate(speaker_set)}

# Regular expression matching text enclosed in curly braces:
_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')

def load_dict_from_json(json_file):
    if os.path.isfile(json_file):
        assert os.path.getsize(
            json_file) > 0, 'the json file %s is empty.' % json_file
        with open(json_file, 'r') as fid:
            speaker_index_dict = json.load(fid)
    else:
        raise IOError("%s is empty." % json_file)
    return speaker_index_dict


def phone_to_sequence(phones):
    phones.append("~")
    return [_phone_to_id[p] for p in phones]


def tone_to_sequence(tones):
    tones.append("~")
    return [_tone_to_id[t] for t in tones]


def categ_to_sequence(categories):
    categories.append("~")
    return [_categ_to_id[t] for t in categories]


def prosody_to_sequence(prosody):
    prosody.append("~")
    return [_prsd_to_id[t] for t in prosody]

def speaker_to_sequence(speakers):
    
    return [_speaker_to_id[t] for t in speakers]

def label_to_fusion_sequence(label):
    phones = []
    tones = []
    word_categ = []
    prosody = []

    with open(label, 'r') as lab_reader:
        lines = lab_reader.readlines()
        for line in lines:
            meta = line.strip().split('\t')
            phones.append(meta[0])
            tones.append(meta[1])
            word_categ.append(meta[3])
            prosody.append(meta[4])
    phones.append("~")
    tones.append("~")
    word_categ.append("~")
    prosody.append("~")

    return [_phone_to_id[t] for t in phones], \
        [_tone_to_id[t] for t in tones], \
        [_categ_to_id[t] for t in word_categ], \
        [_prsd_to_id[t] for t in prosody]
