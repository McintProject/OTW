# -------------------------------------------------------------------------------
# Name:         FraudGuardWrapper.py
# Purpose:      Fraudguard module to retrieve IP reputation data for a specific IP 
#
# Author:      Jorge I
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------
import requests
import json
from requests.auth import HTTPBasicAuth
from colorama import *
import os
import re

from modulos.config import USER_API_KEY, PASSWORD_API_KEY

def ip_fraud(apikey, target):

    ip = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

    if ip.search(target): 

        print(Fore.GREEN+"IP introducida correctamente"+Fore.RESET)
        print()

    else:

        print(Fore.RED+"La IP introducida no es válida. Lanze de nuevo el Programa e introduzca de nuevo la IP"+Fore.RESET)
        print()

        exit()

    url = "https://api.fraudguard.io/v2/ip/"

    response = requests.get('https://api.fraudguard.io/v2/ip/' + target, verify=True, auth=HTTPBasicAuth(USER_API_KEY, PASSWORD_API_KEY))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()
    
    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la IP solicitada"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_fraud = {}

    try:
        
        for threat in respuesta:

            if (respuesta["risk_level"] != "unknown"):

                array_threat = []

                dict_threat = {"Risk_Level": respuesta["risk_level"]}
                
            if (respuesta["threat"] != None) and (respuesta["threat"] != "unknown"):

                dict_threat.update({"Threat": respuesta["threat"]})

            if (respuesta["discover_date"] != "unknown"):

                dict_threat.update({"Discover_Date": respuesta["discover_date"]})

        array_threat.append(dict_threat)

        dict_fraud.update({"Threat": array_threat})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for threat in respuesta:
                
            if (respuesta["latitude"] != "unknown"):

                array_geo = []

                dict_geo = {}

                dict_geo.update({"Latitude": respuesta["latitude"]})

            if (respuesta["longitude"] != "unknown"):

                dict_geo.update({"Longitude": respuesta["longitude"]})

            if (respuesta["city"] != "unknown"):

                dict_geo.update({"City": respuesta["city"]})

            if (respuesta["postal_code"] != "unknown"):

                dict_geo.update({"Postal_Code": respuesta["postal_code"]})

            if (respuesta["country"] != "unknown"):

                dict_geo.update({"Country": respuesta["country"]})

            if (respuesta["isocode"] != "unknown"):

                dict_geo.update({"Isocode": respuesta["isocode"]})

            if (respuesta["state"] != "unknown"):

                dict_geo.update({"State": respuesta["state"]})
                
            if (respuesta["state_code"] != "unknown"):

                dict_geo.update({"State_Code": respuesta["state_code"]})

            if (respuesta["timezone"] != "unknown"):

                dict_geo.update({"Timezone": respuesta["timezone"]})

        array_geo.append(dict_geo)

        dict_fraud.update({"Geo": array_geo})

    except (NameError, KeyError, UnboundLocalError):

        pass

    try:
        
        for threat in respuesta:

            if (respuesta["asn"] != "unknown"):

                array_tech = []

                dict_tech = {}

                dict_tech.update({"ASN": respuesta["asn"]})

                if (respuesta["asn_organization"] != "unknown"):

                    dict_tech.update({"ASN_Organization": respuesta["asn_organization"]})

                if (respuesta["isp"] != "unknown"):

                    dict_tech.update({"Isp": respuesta["isp"]})

                if (respuesta["organization"] != "unknown"):

                    dict_tech.update({"Organization": respuesta["organization"]})

                if (respuesta["connection_type"] != "unknown"):

                    dict_tech.update({"Connection_Type": respuesta["connection_type"]})

        array_tech.append(dict_tech)

        dict_fraud.update({"Tech": array_tech})

    except (KeyError, UnboundLocalError):

        pass

    if (respuesta["risk_level"] == '1'):

        print(Fore.GREEN+Style.BRIGHT+"[RISK LEVEL 1/5]--------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La Ip introducida no está asociada a ningún riesgo")
        print(Cursor.DOWN(1))

    elif (respuesta["risk_level"] == '2'):

        print(Fore.GREEN+Style.BRIGHT+"[RISK LEVEL 2/5]-----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La Ip introducida está asociada con Prácticas de Spam o Recursos Automatizados")
        print(Cursor.DOWN(1))

    elif (respuesta["risk_level"] == '3'):

        print(Fore.GREEN+Style.BRIGHT+"[RISK LEVEL 3/5]-----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La Ip introducida puede estar detrás de un Proxy Público")
        print(Cursor.DOWN(1))

    elif (respuesta["risk_level"] == '4'):

        print(Fore.GREEN+Style.BRIGHT+"[RISK LEVEL 4/5]-----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La Ip introducida se corresponde con un Nodo de Salida de la Red Tor")
        print(Cursor.DOWN(1))

    elif (respuesta["risk_level"] == '5'):

        print(Fore.GREEN+Style.BRIGHT+"[RISK LEVEL 5/5]-----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print("La Ip introducida esta relacionada con Botnets, Malware, o Ataques DDOS")
        print(Cursor.DOWN(1))

    if (array_threat) != []:
        print(Fore.GREEN+Style.BRIGHT+"[GENERAL THREAT INFO]----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_threat)
        print(Cursor.DOWN(1))

    try:
        
        if (array_geo) != []:
            print(Fore.GREEN+Style.BRIGHT+"[GEO THREAT INFO]--------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_geo)
            print(Cursor.DOWN(1))

    except NameError:

        pass

    if (array_tech) != []:

        print(Fore.GREEN+Style.BRIGHT+"[TECH THREAT INFO]----------------------------------------------------------------------------- -[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_tech)
        print(Cursor.DOWN(0.5))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))


    
    







