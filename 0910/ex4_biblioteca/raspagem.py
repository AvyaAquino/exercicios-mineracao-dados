import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")


def campo(livro, classe):
    return livro.find("p", class_=classe).span.text.strip()


livros = []

for div in soup.find_all("div", class_="livro"):
    palavras = [li.text.strip() for li in div.find("ul", class_="palavras-chave").find_all("li")]

    livros.append({
        "titulo": div.find("h2", class_="titulo").text.strip(),
        "autor": campo(div, "autor"),
        "ano": campo(div, "ano"),
        "genero": campo(div, "genero"),
        "situacao": campo(div, "situacao"),
        "palavras": palavras,
    })

print("ACERVO COMPLETO")
for l in livros:
    print("-" * 50)
    print(f"Título:   {l['titulo']}")
    print(f"Autor:    {l['autor']}")
    print(f"Ano:      {l['ano']}")
    print(f"Gênero:   {l['genero']}")
    print(f"Situação: {l['situacao']}")
    print(f"Palavras-chave: {', '.join(l['palavras'])}")
print("-" * 50)

print("\nLIVROS DISPONÍVEIS")
for l in livros:
    if l["situacao"] == "Disponível":
        print(f"- {l['titulo']} ({l['autor']}, {l['ano']})")
