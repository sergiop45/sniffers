import requests
from bs4 import BeautifulSoup
import sys
import urllib.parse

def sniffarLinks(url, base_url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            validlinks = [urllib.parse.urljoin(base_url, link["href"]) for link in links]
            return validlinks
        else:
            print(f'Falha na requisição com código de status {response.status_code}')
            return []
    except Exception as erro:
        print(erro)
        return []

if len(sys.argv) != 2:
    print("Use: python snniferlinks.py <url_alvo>")
else:
    alvo = "https://" + sys.argv[1]
    print("Sniffer de links em {}".format(alvo))
    
    links_encontrados = set()
    
    def salvar_links(links):
        with open("links.txt".format(alvo), "w") as file:
            for url in links:
                file.write(url + "\n")

    def explorar_links(url, base_url):
        novos_links = sniffarLinks(url, base_url)
        for link in novos_links:
            if link.startswith(base_url) and link not in links_encontrados:
                links_encontrados.add(link)
                print("Sniffer de links em {}".format(link))
                explorar_links(link, base_url)

    links_encontrados.add(alvo)
    
    explorar_links(alvo, alvo)
    salvar_links(links_encontrados)
