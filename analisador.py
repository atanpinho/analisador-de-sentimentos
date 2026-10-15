from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classificador = pipeline('sentiment-analysis', model='pysentimiento/bertweet-pt-sentiment')

@app.route("/", methods=["GET", "POST"])

def home():
    frase_digitada = ""
    resultado_tela = ""

    if request.method == "POST":
        frase_digitada = request.form.get("frase")
        resposta_ia = classificador(frase_digitada)
        rotulo = resposta_ia[0]['label']
        certeza = resposta_ia[0]['score'] * 100
        resultado_tela = f"Análise: {rotulo} ({certeza:.2f}% de certeza)"        
    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)
    
if __name__ == "__main__":
    app.run(debug=True)
