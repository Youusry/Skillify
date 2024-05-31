from flask import Flask, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def speech():
    rec = sr.Recognizer()
    with sr.Microphone() as src:
        print("Say your answer...")
        audio = rec.listen(src)
        try:
            text = rec.recognize_google(audio)
            print(text)
            return jsonify({"result": text})
        except sr.UnknownValueError:
            return jsonify({"result": "Could not understand audio"})
        except sr.RequestError as e:
            return jsonify({"result": "Could not request results; {0}".format(e)})

if __name__ == '__main__':
    app.run(debug=True)
