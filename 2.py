import pyttsx3
import os
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)
with open('exemplo.txt','r',encondig='utg-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
engine.say(conteudo)
engine.runAndWait()
