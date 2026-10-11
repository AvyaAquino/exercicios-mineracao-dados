import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"
CATEGORIA_ESCOLHIDA = "Tecnologia"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

noticias = []

for artigo in soup.find_all("article", class_="noticia"):
    noticia = {
        "categoria": artigo.find("span", class_="categoria").text.strip(),
        "titulo": artigo.find("h2", class_="titulo").text.strip(),
        "data": artigo.find("time", class_="data").text.strip(),
        "resumo": artigo.find("p", class_="resumo").text.strip(),
        "autor": artigo.find("p", class_="autor").strong.text.strip(),
    }
    noticias.append(noticia)

    print("+" + "-" * 60)
    print(f"| [{noticia['categoria']}] {noticia['data']}")
    print(f"| {noticia['titulo']}")
    print(f"| {noticia['resumo']}")
    print(f"| Autor: {noticia['autor']}")
print("+" + "-" * 60)

print(f"\nTítulos da categoria '{CATEGORIA_ESCOLHIDA}':")
for n in noticias:
    if n["categoria"] == CATEGORIA_ESCOLHIDA:
        print(f"- {n['titulo']}")
