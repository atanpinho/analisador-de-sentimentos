from flask import Flask, render_template, request
from pysentimiento import create_analyzer

app = Flask(__name__)

# Inicializando o motor leve de IA em Português (consome pouca RAM)
classificador = create_analyzer(task="sentiment", lang="pt")

@app.route("/", methods=["GET", "POST"])
def home():
    frase_digitada = ""
    resultado_tela = ""
    
    if request.method == "POST":
        frase_digitada = request.form.get("frase")
        
        if frase_digitada:
            # Passando o texto pelo classificador leve
            analise = classificador.predict(frase_digitada)
            rotulo = analise.output
            
            # Pegando a porcentagem exata de certeza
            if rotulo == "POS":
                resultado_tela = f"Análise: Positiva ({analise.probas['POS'] * 100:.2f}%)"
            elif rotulo == "NEG":
                resultado_tela = f"Análise: Negativa ({analise.probas['NEG'] * 100:.2f}%)"
            else:
                resultado_tela = f"Análise: Neutra ({analise.probas['NEU'] * 100:.2f}%)"
                
    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)

if __name__ == "__main__":
    app.run(debug=True)
