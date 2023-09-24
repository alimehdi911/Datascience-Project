from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
from translate import Translator

app = Flask(__name__)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech_to_text():
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said"
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service"
    pass

def text_to_text_translation(text, source_language, target_language):
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(text)
    return translation
    pass

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()
    pass



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    spoken_text = data['spokenText']
    source_language = data['sourceLanguage']
    target_language = data['targetLanguage']
 
    translated_text = text_to_text_translation(spoken_text, source_language, target_language)
 
    return jsonify({'translatedText': translated_text})

if __name__ == '__main__':
    app.run(debug=True)

