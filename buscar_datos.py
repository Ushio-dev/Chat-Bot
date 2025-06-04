from bs4 import BeautifulSoup
import requests
import os
import json
from producto import Producto
# Este script busca productos en Mercado Libre Argentina y guarda los datos en un archivo de texto.

#URL_BASE = "https://listado.mercadolibre.com.ar/harry-potter#D[A:harry%20potter]"

datos_empresa = {
  "nombre": "TechNova Components",
  "horarios_atencion": {
    "lunes_viernes": "09:00 - 18:00",
    "sabado": "10:00 - 14:00",
    "domingo": "Cerrado"
  },
  "telefono": "+54 11 3456-7890",
  "correo": "contacto@technova.com",
  "productos": [],
  "empleados": [
    {
      "nombre": "Lucía Fernández",
      "telefono": "+54 11 6543-2100",
      "horario": "09:00 - 15:00",
      "dias_trabajo": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    },
    {
      "nombre": "Carlos Gómez",
      "telefono": "+54 11 6789-1234",
      "horario": "12:00 - 18:00",
      "dias_trabajo": ["Lunes", "Miércoles", "Viernes", "Sábado"]
    },
    {
      "nombre": "Mariana Torres",
      "telefono": "+54 11 6123-4567",
      "horario": "10:00 - 16:00",
      "dias_trabajo": ["Martes", "Jueves", "Viernes", "Sábado"]
    },
    {
      "nombre": "Diego Ramírez",
      "telefono": "+54 11 6345-7891",
      "horario": "13:00 - 18:00",
      "dias_trabajo": ["Lunes", "Martes", "Miércoles", "Jueves"]
    }
  ]
}


   
    
def crear_archivo():
    with open("datos.json", "w", encoding="utf-8") as file:
        json.dump(datos_empresa, file)
    print("Archivo JSON creado con éxito.")     
        
    """    
    with open(f"./{nombre_archivo}", "w", encoding="utf-8") as file:
        for li in li_productos:
            titulo = li.find("a", class_="poly-component__title").text.strip()
            precio = li.find("span", class_="andes-money-amount__fraction").text.strip()
            link = li.find("a", class_="poly-component__title").get("href")
            
            
            file.write(titulo + ";" + link + ";" + precio + "\n")
       """     
  
def nuevos_productos():
    a_buscar = input("Ingrese a buscar: ").replace(" ", "-")
    URL_BASE = f"https://listado.mercadolibre.com.ar/{a_buscar}"
    datos_obtenido = requests.get(URL_BASE)


    soup = BeautifulSoup(datos_obtenido.text, "html.parser")

    li_productos = soup.find_all("li", class_="ui-search-layout__item") # li es la etiqueta que contiene los productos
        
    productos = []
        
    for li in li_productos:
        titulo = li.find("a", class_="poly-component__title").text.strip()
        precio = li.find("span", class_="andes-money-amount__fraction").text.strip()
        link = li.find("a", class_="poly-component__title").get("href")
        
        productos.append(Producto(titulo, link, precio).__dict__)
    
    with open("datos.json", "r+",  encoding="utf-8") as file:
        datos = json.load(file)
        
        for producto in productos:
            datos["productos"].append(producto)
        
        file.seek(0)  # Mover el cursor al inicio del archivo
        json.dump(datos, file)   
         
def agregar_datos():
    if os.path.exists("./datos.json"): 
        nuevos_productos()
        
        """
        with open("./datos.txt", "a", encoding="utf-8") as archivo_datos, open("./nuevos.txt", "r", encoding="utf-8") as archivos_nuevos:
            for linea in archivos_nuevos.readlines():
                archivo_datos.write(linea)
                
        os.remove("nuevos.txt")
        """
        
    else:
        crear_archivo()
        nuevos_productos()
        
         
def menu():
    print("1-Agregar Productos")
    print("0-Salir")
    opc = int(input("Ingresar opcion: "))
    return opc
    
if __name__== "__main__":
    opc = menu()
    
    while True:
        if opc == 1:
            agregar_datos()
        elif opc == 0:
            break
        else:
            print("Opcion no valida")
        
        opc = menu()
