import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

for secao in soup.find_all("section", class_="secao"):
    categoria = secao.find("h2").text.strip()
    print("=" * 50)
    print(categoria.upper())
    print("=" * 50)

    for item in secao.find_all("div", class_="item"):
        nome = item.find("h3", class_="nome").text.strip()
        descricao = item.find("p", class_="descricao").text.strip()
        preco = item.find("p", class_="preco").text.strip()
        print(f"  {nome:<25} {preco:>10}")
        print(f"     {descricao}")
    print()
