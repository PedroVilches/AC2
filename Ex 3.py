import streamlit as st
import speech_recognition as sr

def principal():
    st.title("Transcrição de Áudio")
    uploaded_file = st.file_uploader("Faça upload do arquivo de áudio(formato suportado:WAV)",type=["wav"])
    if uploaded_file(arquivo_audio) as source:
        transcrever_audio(uploaded_file)

def transcrever_audio(arquivo_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(arquivo_audio) as source:
        st.wrtie("Processando audio...")
        audio = recognizer.record(source)
        texto_transcrito = recognizer.recognize_google(audio, language="pt-BR")
        st.write("Texto teanscrito:", texto_transcrito)
def código
principal()
