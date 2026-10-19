from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    frase_digitada = ""
    resultado_tela = ""

    if request.method == "POST":
        frase_digitada = request.form.get("frase")
        
        if frase_digitada:
            # Configuração original do e-book puxando o pipeline do transformers
            classificador = pipeline("sentiment-analysis")
            resposta_ia = classificador(frase_digitada)
            
            # Puxando as chaves diretas do dicionário dentro da lista [0]
            rotulo = resposta_ia[0]['label']
            certeza = resposta_ia[0]['score'] * 100
            
            # Formatação exata do resultado original do livro
            resultado_tela = f"Análise: {rotulo} ({certeza:.2f}%) de certeza"

    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)

if __name__ == "__main__":
    app.run(debug=True)
