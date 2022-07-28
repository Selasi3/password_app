from flask import Flask, render_template,url_for, request, redirect

import string
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods= ["POST"])
def generate():
    if request.method =="POST":
        no_lowercase_strings = int(request.form["lower"])
        no_uppercase_strings = int(request.form["upper"])
        no_numeric = int(request.form["numeric"])
        no_symbols = int(request.form["symbols"])

        lowercase_alphabet = list(string.ascii_lowercase)
        uppercase_alphabet = list(string.ascii_uppercase)
        all_digits = list(string.digits)
        all_symbols = list(string.punctuation)

        password_characters = []
        lowercase_alphabet = generate_characters(no_lowercase_strings, lowercase_alphabet)
        uppercase_alphabet = generate_characters(no_uppercase_strings, uppercase_alphabet)
        digit_characters = generate_characters(no_numeric, all_digits)
        symbol_characters = generate_characters(no_symbols, all_symbols)

        password_characters.extend(lowercase_alphabet)
        password_characters.extend(uppercase_alphabet)
        password_characters.extend(digit_characters)
        password_characters.extend(symbol_characters)

        random.shuffle(password_characters)
        string_password = ""

        for character in password_characters:
            string_password+=character
        
        return render_template("index.html", generated_password = string_password)
    

def generate_characters(number, character_type):
    characters =  []
    for i in range(number):
        characters.append(random.choice(character_type))
    return characters



    