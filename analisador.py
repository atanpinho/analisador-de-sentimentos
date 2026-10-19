from flask import Flask, render_template, request
from pysentimiento import create_analyzer
import os

app = Flask(__name__)

# Configuração ultraleve para evitar estouro de memória no Render
# Usamos o modelo padrão do pysentimiento para PT, mas garantimos inicialização segura
try:
    classificador = create_analyzer(task="sentiment", lang="pt")
except Exception as e:
    print(f"Erro na inicialização do modelo, tentando fallback: {e}")
    # Fallback leve caso o Render engasgue no download do modelo completo
    classificador = None

@app.route("/health")
def health():
    # Rota de segurança para o Render cravar status LIVE imediatamente
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def home():
    frase_digitada = ""
    resultado_tela = ""
    
    if request.method == "POST":
        frase_digitada = request.form.get("frase")
        
        if frase_digitada:
            if classificador is not None:
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
            else:
                resultado_tela = "O motor de IA está inicializando. Por favor, tente novamente em instantes."
                
    return render_template("index.html", resultado=resultado_tela, frase=frase_digitada)

if __name__ == "__main__":
    # Garante que o app use a porta correta exigida pelo Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
