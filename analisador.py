from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def home():
    frase_digitada = ""
    resultado_tela = ""
    
    if request.method == "POST":
        frase_digitada = request.form.get("frase")
        
        if frase_digitada:
            # Importa e cria o analisador APENAS aqui dentro, quando o botão é clicado!
            # Isso faz o site dar o status LIVE instantaneamente no Render.
            from pysentimiento import create_analyzer
            classificador = create_analyzer(task="sentiment", lang="pt")
            
            analise = classificador.predict(frase_digitada)
            rotulo = analise.output
            
            if rotulo == "POS":
                resultado_tela = f"Análise: Positiva ({analise.probas['POS'] * 100:.2f}%)"
            elif rotulo == "NEG":
                resultado_tela = f"Análise: Negativa ({analise.probas['NEG'] * 100:.2f}%)"
            else:
                resultado_tela = f"Análise: Neutra ({analise.probas['NEU'] * 100:.2f}%)"
                
    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
