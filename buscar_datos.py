from bs4 import BeautifulSoup
import requests
import os
# Este script busca productos en Mercado Libre Argentina y guarda los datos en un archivo de texto.

#URL_BASE = "https://listado.mercadolibre.com.ar/harry-potter#D[A:harry%20potter]"

def buscar_datos(nombre_archivo="datos.txt"):
    a_buscar = input("Ingrese a buscar: ").replace(" ", "-")
    URL_BASE = f"https://listado.mercadolibre.com.ar/{a_buscar}"
    datos_obtenido = requests.get(URL_BASE)


    soup = BeautifulSoup(datos_obtenido.text, "html.parser")

    primer_li = soup.find_all("li", class_="ui-search-layout__item")

    with open(f"./{nombre_archivo}", "w", encoding="utf-8") as file:
        for li in primer_li:
            titulo = li.find("a", class_="poly-component__title").text.strip()
            precio = li.find("span", class_="andes-money-amount__fraction").text.strip()
            link = li.find("a", class_="poly-component__title").get("href")
            
            
            file.write(titulo + ";" + link + ";" + precio + "\n")
            
            
def agregar_datos():
    buscar_datos("nuevos.txt")    
    
    with open("./datos.txt", "a", encoding="utf-8") as archivo_datos, open("./nuevos.txt", "r", encoding="utf-8") as archivos_nuevos:
        for linea in archivos_nuevos.readlines():
            archivo_datos.write(linea)
            
    os.remove("nuevos.txt")
        
         
def menu():
    print("1-Buscar datos")
    print("2-Agregar Productos")
    print("3-Salir")
    opc = int(input("Ingresar opcion: "))
    return opc
    
if __name__== "__main__":
    opc = menu()
    
    while True:
        if opc == 1:
            buscar_datos()
        elif opc == 2:
            agregar_datos()
        elif opc == 3:
            break
        else:
            print("Opcion no valida")
        
        opc = menu()

    print("Datos obtenidos y guardados en datos.txt")