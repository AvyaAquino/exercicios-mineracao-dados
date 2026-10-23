import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")


def campo(evento, classe):
    return evento.find("p", class_=classe).span.text.strip()


multiplos = []

for evento in soup.find_all("div", class_="evento"):
    nome = evento.find("h2", class_="nome").text.strip()

    palestrantes = [p.text.strip() for p in evento.find_all("span", class_="palestrante")]

    link = evento.find("a", class_="inscricao")
    link_texto = link.text.strip()
    link_href = link["href"]

    print("-" * 55)
    print(f"Evento:   {nome}")
    print(f"Data:     {campo(evento, 'data')}  às {campo(evento, 'horario')}")
    print(f"Local:    {campo(evento, 'local')}")
    print(f"Palestrante(s): {', '.join(palestrantes)}")
    print(f"Inscrição: \"{link_texto}\" -> {link_href}")

    if len(palestrantes) > 1:
        print(f"*** Este evento possui {len(palestrantes)} palestrantes ***")
        multiplos.append(nome)
print("-" * 55)

print("\nEventos com mais de um palestrante:")
for nome in multiplos:
    print(f"- {nome}")
