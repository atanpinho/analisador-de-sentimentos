# 🧠 EU E IA - ANALISANDO E CONSTRUINDO PROJETOS
> *"Repetição não é regressão, é a consolidação do domínio técnico."*

Este repositório contém o código-fonte completo do **Analisador de Sentimentos Inteligente**, o primeiro projeto prático desenvolvido e documentado no e-book "EU E IA". A aplicação utiliza Inteligência Artificial de ponta para decodificar as emoções por trás de textos em tempo real através de uma interface web moderna.

🚀 **Acesse a aplicação em produção:** [Clique aqui para testar o Analisador de Sentimentos](https://onrender.com)

---

## 🛠️ Tecnologias & Engenharia do Projeto

O ecossistema foi projetado para ser elástico, performático e visualmente minimalista, unindo o poder do Python no ecossistema de IA com a agilidade da web.

### 🖥️ Back-End & Inteligência Artificial
* **Python 3 & Flask:** Arquitetura limpa com rotas estruturadas em requisições `POST` e gerenciamento de estados.
* **pysentimiento (`bertweet-pt-sentiment`):** Integração com o modelo de IA da Hugging Face, alcançando alta precisão na análise de textos e sentimentos em Português do Brasil.
* **Gunicorn:** Servidor HTTP WSGI de nível de produção, configurado para garantir a estabilidade e segurança da aplicação na nuvem.

### 🎨 Front-End Elástico & Visual
* **HTML5 Semântico:** Estrutura otimizada focada em acessibilidade e injeção dinâmica de resultados via Jinja2 (`{% if resultado %}`).
* **Custom CSS3 (Dark Mode):** Interface moderna com fundo escuro, caixa arredondada em tom grafite e botão de ação com efeito azul-neon vibrante.

---

## 📁 Estrutura de Pastas do Projeto

```text
├── analisador.py       # Core do Back-End, fiação das rotas e lógica da IA
├── requirements.txt    # Gerenciador de dependências de produção
├── render.yaml         # Arquivo de infraestrutura como código (IaC) para o deploy
├── venv/               # Ambiente virtual isolado do projeto
├── templates/
│   └── index.html      # Interface visual e tomada de resultados
└── static/
    └── style.css       # Maquiagem, design escuro e efeitos neon
```

---

## ⚙️ Como Executar Localmente

Se você deseja clonar este projeto do e-book e rodar na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   ```

2. **Ative o ambiente virtual (venv):**
   ```bash
   # No Windows:
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o analisador:**
   ```bash
   python analisador.py
   ```
   Acesse no seu navegador: `http://localhost:10000`

---

## 📖 Sobre o E-book
Este projeto faz parte do ecossistema de aprendizado do livro **"EU E IA - ANALISANDO E CONSTRUINDO PROJETOS"**. O objetivo desta obra é guiar desenvolvedores na criação de soluções reais, provando que dominar a IA através da prática repetitiva e consciente gera a verdadeira consolidação técnica.
