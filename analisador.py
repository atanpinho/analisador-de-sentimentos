from transformers import pipeline

classificador = pipeline('sentiment-analysis', model='pysentimiento/bertweet-pt-sentiment')

resultado = classificador('Estou adorando construir este projeto do zero com total controle!')

print(resultado)