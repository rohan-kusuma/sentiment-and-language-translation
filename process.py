import pickle
import streamlit as st
import numpy as np
from textblob import TextBlob
from langdetect import detect



loaded_model = pickle.load(open('C:/Users/pc/PycharmProjects/Sentiment_Analysis/trained_model.sav','rb'))

def model(text):
    prediction = loaded_model.predict([text])

    if prediction[0] == 1:
        return "Text is Positive"
    else:
        return "Text is Negative"

def language_translator(text,lang):
    detect_lang = detect(text)
    blob = TextBlob(text)
    trans_sent = blob.translate(to=lang)

    return detect_lang, trans_sent




