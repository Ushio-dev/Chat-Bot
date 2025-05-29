from bs4 import BeautifulSoup
import requests

#URL_BASE = "https://listado.mercadolibre.com.ar/harry-potter#D[A:harry%20potter]"
a_buscar = input("Ingrese a buscar: ").replace(" ", "-")
URL_BASE = f"https://listado.mercadolibre.com.ar/{a_buscar}"
datos_obtenido = requests.get(URL_BASE)


soup = BeautifulSoup(datos_obtenido.text, "html.parser")

primer_li = soup.find_all("li", class_="ui-search-layout__item")

with open("datos.txt", "w", encoding="utf-8") as file:
    for li in primer_li:
        titulo = li.find("a", class_="poly-component__title").text.strip()
        precio = li.find("span", class_="andes-money-amount__fraction").text.strip()
        link = li.find("a", class_="poly-component__title").get("href")
        
        
        file.write(titulo + ";" + link + ";" + precio + "\n")