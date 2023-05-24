
import os, requests

GAMEDIR = os.path.join(".", ".minecraft")
print(GAMEDIR)

def getClient(version_data,version):
    clientURL = version_data["downloads"]["client"]["url"]
    response = requests.get(clientURL)
    with open(f"{GAMEDIR}/{version}/{version}.json" , "wb") as archivo:
        archivo.write(response.content)
    print("Archivo descargado y guardado en:"+f"{GAMEDIR}/{version}/{version}.json" )

def ManageDownloads(version_data,version):
    getClient(version_data,version)
