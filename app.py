import streamlit as st
import pickle
import numpy as np
from googletrans import Translator
from process import model,language_translator
import googletrans
language = googletrans.LANGUAGES

loaded_model = pickle.load(open('C:/Users/pc/PycharmProjects/Sentiment_Analysis/trained_model.sav','rb'))



st.title('Text Sentiment Analysis and Language Translator')

choice = st.sidebar.selectbox('Select an option',('Sentiment Analysis','Language Translator'))



if choice == 'Sentiment Analysis':
    st.title('Sentiment Analysis')
    text_input = st.text_input("Please enter your text")
    if st.button('Show Sentiment'):
        st.success(model(text_input))
else:
    st.title('Language Translator')
    text_input = st.text_input("Please enter your text")
    dest_lang = st.selectbox('Please select language for translation',language.values())

    for key,value in language.items():
        if dest_lang == value:
            lang_key = key

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Translate'):
            st.success(language_translator(text_input, lang=lang_key)[1])
    with col2:
        if st.button('Detect Language'):
            lang_detected = language_translator(text_input, lang=lang_key)[0]
            st.success(language[lang_detected])


