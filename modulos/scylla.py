# -------------------------------------------------------------------------------
# Name:         ScyllaWrapper.py
# Purpose:      Scylla module to retrieve Info about Data leaks based on IP's & Passwords 
#              
# Author:      Jorge Iturria 
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------
import requests
import simplejson as json
from json import JSONDecodeError
from io import open
import webbrowser
from requests.auth import HTTPBasicAuth
from colorama import *
import os
import re

from modulos.config import User, Password

def jprint(obj):

	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

def scylla_mail(apikey, email):

    if '@' in email:

        print(Fore.GREEN+"Email introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Email introducido no es correcto. Lanze de nuevo el Programa e introduzca de nuevo el Email"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    url = "https://scylla.sh/search"

    headers = {"Accept": "application/json"}

    print(Fore.CYAN+"El Email a buscar es " + email+Fore.RESET)

    _source="q=Email:"+str(email)

    try:
        
        response = requests.get(url, headers=headers, params=_source, verify=False, auth=HTTPBasicAuth(User, Password))

        response_json = (response.json()[0]["_source"])

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

    try:
    
        password = response_json["Password"]

        ip = response_json["IP"]

        dominio = response_json["Domain"]

        print(Fore.RED+Style.BRIGHT+"[WARNING]-------------------------------------------------------------------------------[EMAIL COMPROMISED]"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print("Email comprometido!!! Password asociada:  " + password + " --- IP relacionada: " + ip + " --- Dominio relacionado: " + dominio)
        print(Cursor.DOWN(1)) 

    except KeyError:

        print(Fore.GREEN+Style.BRIGHT+"[IT'S OK]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print("El Email no se encuentra en la BBDD")
        print(Cursor.DOWN(1)) 


    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))



def scylla_pass(apikei, contraseña):

        
    url = "https://scylla.sh/search"

    headers = {"Accept": "application/json"}

    print(Fore.CYAN+"La contraseña a buscar es " + contraseña+Fore.RESET)

    _source="q=Password:"+str(contraseña)

    
        
    try:
        
        response=requests.get(url, headers=headers, params=_source, verify=False, auth=HTTPBasicAuth(User, Password))

        response_json = (response.json()[0]["_source"])

    except IndexError:

        pass

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

    try: 
        
        response_json = (response.json()[0]["_source"])
        
        Email = response_json["Email"]

        ip = response_json["IP"]

        dominio = response_json["Domain"]

        print(Fore.RED+Style.BRIGHT+"[WARNING]-------------------------------------------------------------------------------[PASSWORD COMPROMISED]"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print("Password comprometida!!! Password asociada con el Email: " + Email + " --- IP relacionada: " + ip + " --- Dominio relacionado: " + dominio)
        print(Cursor.DOWN(1)) 

    except IndexError:

        print(Fore.GREEN+Style.BRIGHT+"[IT'S OK]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print("El Password no se encuentra en la BBDD")
        print(Cursor.DOWN(1)) 

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

