# launcher.py

import os
import requests
import json
from downloads import ManageDownloads

# Directorios principales
ASSETS_DIR = "assets"
LIBRARIES_DIR = "libraries"
VERSIONS_DIR = "versions"

def load_json_from_url(url):
    """carga el json de una petición url"""
    response = requests.get(url)
    data = response.json()
    return data
    

def get_available_versions():
    """hace una petición para obetener la lista de verison desde la URL correspondiente"""
    # Hacer una petición para obtener la lista de versiones desde la URL correspondiente
    versions_url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    versions_data = load_json_from_url(versions_url)
    versions = versions_data["versions"]
    return versions

def load_version_data(version):
    """carga los datos de la verision seleccionada"""
    # Hacer una petición para obtener los datos de la versión desde la URL correspondiente
    version_url = f"https://example.com/versions/{str(version)}"
    version_data = load_json_from_url(version_url)
    return version_data



def find_version_url(version:str)-> str:
    """busca la version pasado como parámetro en el json de la respuesta de versiones"""
    versions  = get_available_versions()
    
    for singleversion in versions:
        if (singleversion["id"] == version):
            return singleversion["url"]
    return "ERROR: NO SE HA ENCONTRADO LA VERSION"

def load_version_data(version_url:str):
    # Hacer una petición para obtener los datos de la versión desde la URL correspondiente
    
    version_data = load_json_from_url(version_url)
    print(version_url)
    return version_data

def main():
    version  = input("introduzca una version: ")
    versionUrl = find_version_url(str(version))
    version_data = load_version_data(versionUrl)
    ManageDownloads(version_data,version)

main()
