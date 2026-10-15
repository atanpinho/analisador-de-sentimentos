from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classificador = pipeline('sentiment-analysis', model='pysentimiento/bertweet-pt-sentiment')

@app.route("/", methods=["GET", "POST"])
