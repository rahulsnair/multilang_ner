# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:16:10 2022

@author: rahul
"""
import spacy
import os

def ner_multilang(sentence, lang): 
    os.system('python -m spacy download {}_core_web_sm'.format(lang))
    nlp = spacy.load(lang+'_core_web_sm')
    
    doc = nlp(sentence)
    final = []  
    for token in doc:
        result = {'text': token.text,
                      'type': token.ent_type_,
                      'start_pos': token.pos_,
                      'end_pos': token.head.pos_}
        final.append(result)
    return final

ner_multilang('I love universe very much', 'en')