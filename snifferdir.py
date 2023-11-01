import requests
import sys
import os

if len(sys.argv) < 2:
    print("Uso: python script.py <URL_alvo>")
    sys.exit(1)

alvo = "https://" + sys.argv[1]
dir_finds = []

with open("wordlist-dir.txt", "r") as file:
    wordlist = file.readlines()

for word in wordlist:
    url = alvo + "/" + word
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Diretório: " + word + " encontrado")
            dir_finds.append(url)
        else:
            print("Diretório " + word + " não encontrado!")
    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao fazer a solicitação:", e)

with open("dir_encontrados.txt", "w") as file:
    for dir in dir_finds:
        file.write(dir+"\n")
    
