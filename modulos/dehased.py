# -------------------------------------------------------------------------------
# Name:         DehasedWrapper.py
# Purpose:      Dehased module to retrieve Info about Data Leaks based on Emails,
#               Passwords, Usernames, Hashes or Phone Numbers
#              
# Author:      Jorge Iturria 
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------
import requests
import json
from colorama import *
import os
import re

from modulos.config import DEHASHED_USER_API, DEHASHED_API_KEY

def dehas_f(apikei, target):

    headers = {"Accept": "application/json"}

    response = requests.get('https://api.dehashed.com/search?query=\'"'+target+'"\'', auth=requests.auth.HTTPBasicAuth(DEHASHED_USER_API, DEHASHED_API_KEY), headers={'Accept':'application/json'})

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()
        
    respuesta = response.json()

    if (respuesta["total"] == 0):

        print(Fore.GREEN+Style.BRIGHT+"[GREAT!!!]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print("No se han encontrado Leaks para el Target introducido")
        print(Cursor.DOWN(1))

        print (Fore.CYAN+Style.BRIGHT+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    dict_dehased = {}

    array_total = []

    if (respuesta["total"] != None):

        dict_total = {"Leaks en los que el Target ha sido encontrado": respuesta["total"]}

    array_total.append(dict_total)

    dict_dehased.update({"status": array_total})

    array_entries = []

    for entries in respuesta["entries"]:

        dict_entries = {}

        if (entries["email"] != None) and (entries["email"] != ""):

            dict_entries.update({"email": entries["email"]})

        if (entries["username"] != None) and (entries["username"] != ""):

            dict_entries.update({"username": entries["username"]})

        if (entries["password"] != None) and (entries["password"] != ""):

            dict_entries.update({"password": entries["password"]})

        if (entries["hashed_password"] != None) and (entries["hashed_password"] != ""):

            dict_entries.update({"hashed_password": entries["hashed_password"]})

        if (entries["name"] != None) and (entries["name"] != ""):

            dict_entries.update({"name": entries["name"]})

        if (entries["address"] != None) and (entries["address"] != ""):

            dict_entries.update({"address": entries["address"]})

        if (entries["ip_address"] != None) and (entries["ip_address"] != ""):

            dict_entries.update({"ip_address": entries["ip_address"]})

        if (entries["phone"] != None) and (entries["phone"] != ""):

            dict_entries.update({"phone": entries["phone"]})

        if (entries["obtained_from"] != None) and (entries["obtained_from"] != ""):

            dict_entries.update({"obtained_from": entries["obtained_from"]})

        # Añadimos el Diccionario a la Lista

        array_entries.append(dict_entries)

        # Añadimos la Lista al Diccionario Principal

        dict_dehased.update({"Leaks": array_entries})

    if (array_total) != []:

        print(Fore.RED+Style.BRIGHT+"[WARNING]------------------------------------------------------------------------------------[TARGET COMPROMISED]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_total)
        print(Cursor.DOWN(1))

    try:
        
        if (array_entries[0]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº1]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[0])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[1]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº2]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[1])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[2]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº3]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[2])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:

        if (array_entries[3]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº4]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[3])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[4]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº5]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[4])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[5]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº6]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[5])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[6]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº7]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[6])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        
        if (array_entries[7]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº8]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[7])
            print(Cursor.DOWN(1))

    except IndexError:

        pass
    try:
        if (array_entries[8]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº9]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[8])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    try:
        if (array_entries[9]) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LEAK Nº10]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_entries[9])
            print(Cursor.DOWN(1))

    except IndexError:

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))
