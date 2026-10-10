import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

cursos = soup.find_all("div", class_="curso")
print(f"Total de cursos encontrados: {len(cursos)}\n")

for curso in cursos:
    nome = curso.find("h2", class_="nome").text.strip()
    area = curso.find("p", class_="area").span.text.strip()
    carga = curso.find("p", class_="carga").span.text.strip()

    print("=" * 40)
    print(f"Curso: {nome}")
    print(f"Área: {area}")
    print(f"Carga horária: {carga}")
    print("Assuntos estudados:")

    for i, assunto in enumerate(curso.find("ul", class_="assuntos").find_all("li"), start=1):
        print(f"   {i}. {assunto.text.strip()}")
print("=" * 40)
