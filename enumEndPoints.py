import requests
import json


with open("wordlist/endpoints.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
    
        endopoint  = linha.strip()
        r = requests.get('http://localhost:8080/'+endopoint)
        retorno = r.status_code
        codigo_retorno   = str(retorno)
        if (retorno != 200):
            with open("endpoints_validos.txt", "a") as resultado:
                resultado.write("\nCódigo: "+codigo_retorno+"\nEndpoint Encontrado: http://localhost:8080/"+endopoint)