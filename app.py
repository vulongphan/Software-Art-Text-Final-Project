import os

import openai
from flask import Flask, redirect, render_template, request, url_for

from gtts import gTTS
from playsound import playsound

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def tts(script):
    file = "file.mp3"
    # initialize tts, create mp3 and play
    tts = gTTS(text=script, lang='en', tld = 'com') 
    tts.save(file)
    playsound(file)
    

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        country = request.form["country"]
        age = request.form["age"]
        occupation = request.form["occupation"]
        prompt = """My name is {}. I am from {}. I am {} years old. I am a {}.""".format(
            name, country, age, occupation)
        cnt = 10
        result = [prompt]
        while cnt > 0:
            response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=prompt,
                temperature=0.5,
            )
            prompt = response.choices[0].text
            result.append(prompt)
            cnt -= 1
        result = "".join(result)
        print(result)
        tts(result)
        return redirect(url_for("index"))

    # result = request.args.get("result")
    return render_template("index.html")
