from bs4 import BeautifulSoup
import os
import requests
import json
import random
import string
from Colorama import Fore
rojo = Fore.RED
verde = Fore.GREEN
amarillo = Fore.YELLOW
ID = "".join(random.sample(string.ascii_letters, k=2))
logo = amarillo+"""
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗    ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██████╗██╗     
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║    ████╗  ██║██╔══██╗████╗ ████║██╔════╝    ██╔════╝██║     
███████╗█████╗  ███████║██████╔╝██║     ███████║    ██╔██╗ ██║███████║██╔████╔██║█████╗      ██║     ██║     
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║    ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║     
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║    ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝╚══════╝

                                       By: Kiddo.Kid
"""+Fore.RESET
nombre1 = input("Ingresa un nombre a buscar: ")

url = 'https://rutificador.net/wp-search/nombre.php'

payload = {'nombre': nombre1}

headers = {
    'Host': 'rutificador.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://rutificador.net/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://rutificador.net',
    'Dnt': '1',
    'Connection': 'close'
}

response = requests.post(url, headers=headers, data=payload)

with open("archivo.html", "a") as l:
    pass

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tabla = soup.find('table', {'id': 'tabla-resultados'})
    datos = []
    for fila in tabla.find_all('tr')[1:]:
        celdas = fila.find_all('td')
        if celdas:
            rut = celdas[0].text.strip()
            nombre = celdas[1].text.strip()
            edad = celdas[2].text.strip()
            sexo = celdas[3].text.strip()
            domicilio = celdas[4].text.strip()
            ciudad = celdas[5].text.strip()
            datos.append({
                'RUT': rut,
                'Nombre': nombre,
                'Edad Aprox.': edad,
                'Sexo': sexo,
                'Domicilio': domicilio,
                'Ciudad': ciudad
            })
    for persona in datos:
        print(verde+f"RUT: {persona['RUT']}, Nombre: {persona['Nombre']}, Edad: {persona['Edad Aprox.']}, Sexo: {persona['Sexo']}, Domicilio: {persona['Domicilio']}, Ciudad: {persona['Ciudad']}")
    with open(f"resultado_{ID}.json", "w", encoding='utf-8') as json_file:
        json.dump(datos, json_file, ensure_ascii=False, indent=4)
    os.remove("archivo.html")

else:
    print(rojo+f"Error al realizar la solicitud. Codigo de estado: {response.status_code}")
