from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# O SEGREDO: Carrega o cérebro da IA no TOPO do arquivo (Roda uma única vez no boot)
# Usando o modelo otimizado e leve em português para não estourar os 512MB de RAM
classificador = pipeline(
    "sentiment-analysis", 
    model="pysentimiento/bertweet-pt-sentiment",
    low_cpu_mem_usage=True  # Instrução para o Python economizar memória RAM na nuvem
)

@app.route("/", methods=["GET", "POST"])
def home():
    frase_digitada = ""
    resultado_tela = ""

    if request.method == "POST":
        # Captura o texto que veio da caixinha "frase" do HTML
        frase_digitada = request.form.get("frase")
        
        if frase_digitada:
            # Passando o texto pelo cérebro da Inteligência Artificial
            resposta_ia = classificador(frase_digitada)
            
            # Extraindo os dados brutos da memória RAM
            rotulo = resposta_ia[0]['label']
            certeza = resposta_ia[0]['score'] * 100
            
            # Montando a f-string cirúrgica que será exibida na tela
            resultado_tela = f"Análise: {rotulo} ({certeza:.2f}%) de certeza"

    # Injetando as variáveis vivas diretamente para dentro do HTML
    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)

if __name__ == "__main__":
    # Garante o funcionamento local na porta 5000 padrão
    app.run(debug=True)

