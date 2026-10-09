from transformers import pipeline

classificador = pipeline('sentiment-analysis', model='pysentimiento/bertweet-pt-sentiment')

resultado = classificador('Estou adorando construir este projeto do zero com total controle!')

print(resultado)

while True:
    frase_usuario = input('Digite uma frase para analisar (ou Ctrl+C para sair): ')

    if frase_usuario =="sair":
        print('Tchau! Até a próxima.')
        break

    resultado_usuario = classificador(frase_usuario)
    print(resultado_usuario)
    



