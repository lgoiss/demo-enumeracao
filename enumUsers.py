import requests
import json


with open("users.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
    
        nome_usuario  = linha.strip()
        payload  = {'login': nome_usuario, 'senha': ''}
        r = requests.post('http://localhost:8080/usuario/login', json=payload)
        mensagem = r.text
        if (mensagem == "Senha Incorreta!"):
            with open("usuarios_validos.txt", "a") as resultado:
                resultado.write("\nUsuário " + nome_usuario + " é válido")