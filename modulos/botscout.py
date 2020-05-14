# -------------------------------------------------------------------------------
# Name:         BotScoutWrapper.py
# Purpose:      BotScout module to identify automated web scripts, known as "Bots"
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

from modulos.config import BOTSCOUT_API_KEY

API_KEY = "BOTSCOUT_API_KEY"

def botemail_f(apikey, email):
    
    if '@' in email:

        print(Fore.GREEN+"Email introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Email introducido no es correcto. Lanze de nuevo el Programa e introduzca de nuevo el Email"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()
    
    url_mail = "http://botscout.com/test/?mail=" + str(email) + "&key=" + BOTSCOUT_API_KEY

    response = requests.get(url_mail)

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Email solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.content

    respuesta_2 = respuesta.decode(encoding="utf-8")

    if "Y" in respuesta_2:

        print(Fore.RED+Style.BRIGHT+"[***WARNING***]-------------------------------------------------------------------------[BOT EMAIL]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("El email introducido es un Bot")
        print(Cursor.DOWN(1))

    else:

        print(Fore.GREEN+Style.BRIGHT+"[***EMAIL OK***]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("El email introducido no es un Bot")
        print(Cursor.DOWN(1))
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def botname_f(apikey, name):

    url_name = "http://botscout.com/test/?name=" + str(name) + "&key=" + BOTSCOUT_API_KEY 

    response = requests.get(url_name)

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Nombre de Usuario solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.content
    
    respuesta_2 = respuesta.decode(encoding="utf-8")

    if "Y" in respuesta_2:

        print(Fore.RED+Style.BRIGHT+"[***WARNING***]-------------------------------------------------------------------------[BOT USER]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("El Nombre de Usuario introducido es un Bot")
        print(Cursor.DOWN(1))

    else:

        print(Fore.GREEN+Style.BRIGHT+"[***USER OK***]-----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("El Nombre de Usuario introducido no es un Bot")
        print(Cursor.DOWN(1))
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def botip_f(key, ip):
    
    ipp = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

    if ipp.search(ip):

        print(Fore.GREEN+"IP introducida correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"La IP introducida no es válida. Lanze de nuevo el Programa e introduzca de nuevo la IP"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()
    
    url_ip = "http://botscout.com/test/?ip=" + str(ip) + "&key=" + BOTSCOUT_API_KEY 

    response = requests.get(url_ip)

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la IP solicitada"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.content

    respuesta_2 = respuesta.decode(encoding="utf-8")

    if "Y" in respuesta_2:

        print(Fore.RED+Style.BRIGHT+"[***WARNING***]-------------------------------------------------------------------------[BOT IP]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La IP introducida puede estar relacionada con un Bot")
        print(Cursor.DOWN(1))

    else:

        print(Fore.GREEN+Style.BRIGHT+"[***IP OK***]-------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La IP introducida no se relaciona con un BotNet")
        print(Cursor.DOWN(1))
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))
