import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")


def campo(produto, classe):
    """Retorna o texto do <span> dentro do <p> com a classe informada."""
    return produto.find("p", class_=classe).span.text.strip()


produtos = []
for div in soup.find_all("div", class_="produto"):
    produtos.append({
        "nome": div.find("h2", class_="nome").text.strip(),
        "fabricante": campo(div, "fabricante"),
        "categoria": campo(div, "categoria"),
        "preco": campo(div, "preco"),
        "estoque": campo(div, "estoque"),
    })

print("TODOS OS PRODUTOS")
print(f"{'Nome':<22}{'Fabricante':<12}{'Categoria':<16}{'Preço':<14}{'Estoque'}")
print("-" * 80)
for p in produtos:
    print(f"{p['nome']:<22}{p['fabricante']:<12}{p['categoria']:<16}{p['preco']:<14}{p['estoque']}")

print("\nPRODUTOS DISPONÍVEIS")
print("-" * 80)
for p in produtos:
    if p["estoque"] == "Disponível":
        print(f"- {p['nome']} ({p['fabricante']}) - {p['preco']}")
