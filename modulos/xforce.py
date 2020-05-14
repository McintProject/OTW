# -------------------------------------------------------------------------------
# Name:         XforceExchangeWrapper.py
# Purpose:      IBM XforceExchange module to retrieve Info & Reputation data for a Domain, 
#               IP, URL or Hash (Malware Data)
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
import base64
from requests.auth import HTTPBasicAuth 
from colorama import *
import os
import re

from modulos.config import api_key, password

def xip_reputacion(apikei, ip):

    ipp = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

    if ipp.search(ip): 

        print(Fore.GREEN+"IP introducida correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"La IP introducida no es válida. Lanze de nuevo el Programa e introduzca de nuevo la IP"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    endpoint = "https://api.xforce.ibmcloud.com/"

    response = requests.get("https://api.xforce.ibmcloud.com/ipr/history/" + ip, auth=HTTPBasicAuth(api_key, password))

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
   
    respuesta = response.json()

    dict_iprep = {}

    try:
       
       if "ip" != None:

           array_iprep = []

           dict_ip = {"IP": respuesta["ip"]}

           array_iprep.append(dict_ip)

           dict_iprep.update({"IP": array_iprep})

    except (KeyError, UnboundLocalError):

       pass

    try:
       
       for history in respuesta["history"]:

           if (history["created"] != {}):

               dict_history = {"created": respuesta["history"][-1].get("created", ''),
                               "reason": respuesta["history"][-1].get("reason", ''),
                               "cats": respuesta["history"][-1].get("cats", ''),
                               "geo": respuesta["history"][-1]["geo"].get("country", ''),
                               "categoryDescriptions": respuesta["history"][-1].get("categoryDescriptions", ''),
                               "reasonDescription": respuesta["history"][-1].get("reasonDescription", ''),
                               "score": respuesta["history"][-1].get("score", '')}

       array_iprep.append(dict_history)

       dict_iprep.update({"History": array_iprep})

    except (KeyError, UnboundLocalError):

        pass

    try:
       
       for subnets in respuesta["subnets"]:

           if (subnets["ip"] != {}):


               array_subnet = []

               dict_subnet = {"ip": respuesta["subnets"][-1].get("ip", ''),
                              "created": respuesta["subnets"][-1].get("created", ''),
                              "asns": respuesta["subnets"][-1].get("asns", ''),
                              "Country": respuesta["subnets"][-1]["geo"].get("country", '')}

       array_subnet.append(dict_subnet)

       dict_iprep.update({"subnets": array_subnet})

    except (KeyError, UnboundLocalError):

       pass

    if (array_iprep) != []:

       print(Fore.GREEN+Style.BRIGHT+"[HISTORY]----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
       print() 
       print(array_iprep)
       print(Cursor.DOWN(1))

    try:

       if (array_subnet) != []:

            print(Fore.GREEN+Style.BRIGHT+"[SUBNETS]----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_subnet)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

       pass

def xip_dns(auth, ip):
    
    response = requests.get("https://api.xforce.ibmcloud.com/resolve/" + ip, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_ipdns = {}

    try:

        if "RDNS" !=None:

            array_rdns = []

            dict_rdns = {"DNS": respuesta["RDNS"]}

            array_rdns.append(dict_rdns)

            dict_ipdns.update({"DNS": array_rdns})

    except KeyError:

        pass

    if (array_rdns) != []:

        print(Fore.GREEN+Style.BRIGHT+"[DNS]---------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_rdns)
        print(Cursor.DOWN(1))

def xip_malware(auth, ip):
    
    response = requests.get("https://api.xforce.ibmcloud.com/ipr/malware/" + ip, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_ipmal = {}

    try:
    
        for malware in respuesta["malware"]:
        
            try:
                if "malware" != None:

                    array_ipmal = []

                    dict_ipmalw = {"firstseen": respuesta["malware"][0].get("irstseen", ''),
                                   "Domain": respuesta["malware"][0].get("domain", ''),
                                   "Family": respuesta["malware"][0]["family"][0],
                                   "origin": respuesta["malware"][0].get("origin", ''),
                                   "type": respuesta["malware"][0].get("type", ''),
                                   "Hash": respuesta["malware"][0].get("md5", ''),                         
                                   "Port": respuesta["malware"][0].get("port", ''),
                                   "filepath": respuesta["malware"][0].get("filepath", '')}

            except KeyError:

                pass

        array_ipmal.append(dict_ipmalw)

        dict_ipmal.update({"Malware": array_ipmal})

    except Exception:

        pass

    try:
    
        if (array_ipmal) != []:

            print(Fore.GREEN+Style.BRIGHT+"[MALWARE]---------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_ipmal)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

def xip_whois(auth, ip):

    response = requests.get("https://api.xforce.ibmcloud.com/whois/" + ip, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_ipwhois = {}
 
    try:
        
        if "createdDate" != None:

            array_ipwhois = []

            dict_whois = {"createdDate": respuesta["createdDate"],
                        "updatedDate": respuesta["updatedDate"],
                        "netRange": respuesta["netRange"],
                        "country": respuesta["contact"][0].get("country", ''),
                        "organization": respuesta["contact"][0].get("organization", ''),
                        "type": respuesta["contact"][0].get("type", ''),
                        "country": respuesta["contact"][0].get("country", ''),
                        "registrarName": respuesta["extended"].get("registrarName", ''),
                        "contactEmail": respuesta["extended"].get("contactEmail", '')}
                        
            array_ipwhois.append(dict_whois)

            dict_ipwhois.update({"Whois": array_ipwhois})

    except (KeyError, UnboundLocalError):

        pass

    try:
    
        if (array_ipwhois) != []:

            print(Fore.GREEN+Style.BRIGHT+"[WHOIS]------------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_ipwhois)
            print(Cursor.DOWN(1))

    except UnboundLocalError:

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def domain_rep(apikey, dominio):

    dom = re.compile(r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6}$')

    if dom.search(dominio): 

        print(Fore.GREEN+"Nombre de Dominio introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))
    
    else:

        print(Fore.RED+"El nombre de Dominio introducido no es válido. Lanze de nuevo el Programa e introdúzcalo de nuevo"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()

    response = requests.get("https://api.xforce.ibmcloud.com/resolve/" + dominio, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Dominio solicitado"+Fore.RESET+Style.RESET_ALL)
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
    
    respuesta = response.json()
    
    dict_domain = {}

    if 'AAAA' in respuesta:
        array_aaaa = []

        dict_aaaa = {"Ipv6": respuesta["AAAA"]}

        array_aaaa.append(dict_aaaa)
 
        dict_domain.update({"AAAA": array_aaaa})

    if 'MX' in respuesta:

        array_mx = []

        dict_mx = {"MX": respuesta["MX"]}

        array_mx.append(dict_mx)

        dict_domain.update({"MX": array_mx})

    if 'TXT' in respuesta:

        array_txt = []

        dict_txt = {"TXT": respuesta["TXT"]}

        array_txt.append(dict_txt)

        dict_domain.update({"TXT": array_txt})

    try:

        for Passive in respuesta["Passive"]:

            if 'query' != None:

                array_query = []

                dict_passive = {"query": respuesta["Passive"].get("query", '')}

        array_query.append(dict_passive)

        dict_domain.update({"Passive": array_query})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain = []

            dict_pass = {"value": respuesta["Passive"]["records"][0]["value"],
                        "type": respuesta["Passive"]["records"][0]["type"],
                        "recordType": respuesta["Passive"]["records"][0]["recordType"],
                        "first": respuesta["Passive"]["records"][0]["first"],
                        "last": respuesta["Passive"]["records"][0]["last"]}

        array_domain.append(dict_pass)

        dict_domain.update({"Passive1": array_domain})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain1 = []

            dict_pass1 = {"value": respuesta["Passive"]["records"][1]["value"],
                        "type": respuesta["Passive"]["records"][1]["type"],
                        "recordType": respuesta["Passive"]["records"][1]["recordType"],
                        "first": respuesta["Passive"]["records"][1]["first"],
                        "last": respuesta["Passive"]["records"][1]["last"]}

        array_domain1.append(dict_pass1)

        dict_domain.update({"Passive2": array_domain1})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain2 = []

            dict_pass2 = {"value": respuesta["Passive"]["records"][2]["value"],
                        "type": respuesta["Passive"]["records"][2]["type"],
                        "recordType": respuesta["Passive"]["records"][2]["recordType"],
                        "first": respuesta["Passive"]["records"][2]["first"],
                        "last": respuesta["Passive"]["records"][2]["last"]}

        array_domain2.append(dict_pass2)

        dict_domain.update({"Passive3": array_domain2})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain3 = []

            dict_pass3 = {"value": respuesta["Passive"]["records"][3]["value"],
                        "type": respuesta["Passive"]["records"][3]["type"],
                        "recordType": respuesta["Passive"]["records"][3]["recordType"],
                        "first": respuesta["Passive"]["records"][3]["first"],
                        "last": respuesta["Passive"]["records"][3]["last"]}

        array_domain3.append(dict_pass3)

        dict_domain.update({"Passive4": array_domain3})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain4 = []

            dict_pass4 = {"value": respuesta["Passive"]["records"][4]["value"],
                        "type": respuesta["Passive"]["records"][4]["type"],
                        "recordType": respuesta["Passive"]["records"][4]["recordType"],
                        "first": respuesta["Passive"]["records"][4]["first"],
                        "last": respuesta["Passive"]["records"][4]["last"]}

        array_domain4.append(dict_pass4)

        dict_domain.update({"Passive5": array_domain4})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_query) != []:

            print(Fore.GREEN+Style.BRIGHT+"[QUERY]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_query)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain1) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE1]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain1)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain2) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE2]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain3) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE3]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain3)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain4) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE4]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain4)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_aaaa) != []:

            print(Fore.GREEN+Style.BRIGHT+"[IPV6]------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_aaaa)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_mx) != []:

            print(Fore.GREEN+Style.BRIGHT+"[MX]--------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_mx)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_txt) != []:

            print(Fore.GREEN+Style.BRIGHT+"[TXT]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_txt)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    if dict_domain == {}:
        
        print(Fore.RED+Style.BRIGHT+"[DNS]-------------------------------------------------------------------------------------[NO RESULTS]"+Fore.RESET+Style.RESET_ALL)

def domain_whois(auth, dominio):

    response = requests.get("https://api.xforce.ibmcloud.com/whois/" + dominio, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    array_dmwhois = respuesta

    dict_dmwhois = {}

    dict_dmwhois = array_dmwhois
    
    if (array_dmwhois) == {'extended': None}:

        print(Fore.RED+Style.BRIGHT+"[WHOIS]-----------------------------------------------------------------------------------[NO RESULTS]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(Cursor.DOWN(1))
        
    else:

        print(Fore.GREEN+Style.BRIGHT+"[WHOIS]---------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_dmwhois)
        print(Cursor.DOWN(1))
    
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def url_rep(apikey, url):
    
    urll = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')

    if urll.search(url): 

        print(Fore.GREEN+"URL introducida correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"La URL introducida no es válida. Lanze de nuevo el Programa e introdúzcala de nuevo"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()
   
    response = requests.get("https://api.xforce.ibmcloud.com/url/" + url, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la URL solicitada"+Fore.RESET+Style.RESET_ALL)
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
    
    respuesta = response.json()

    dict_url = {}

    try:
    
        for result in respuesta["result"]:

            if 'result' != None:

                array_result = []

                dict_result = {"url": respuesta["result"].get("url", ''),
                               "cats": respuesta["result"].get("cats", ''),
                               "score": respuesta["result"].get("score", ''),
                               "categoryDescriptions": respuesta["result"].get("categoryDescriptions", '')}

        array_result.append(dict_result)

        dict_url.update({"Resultados": array_result})

    except (KeyError, UnboundLocalError):

            pass

    try:
 
        for tags in respuesta["tags"]:

            array_tags = []

            if (tags["tag"] != None):

                dict_tags = {"tag": respuesta["tags"][-1].get("tag", ''),
                             "date": respuesta["tags"][-1].get("date", '')}

        array_tags.append(dict_tags)

        dict_url.update({"tags": array_tags})

    except (KeyError, UnboundLocalError):

            pass

    try:
        
        if (array_result) != []:

            print(Fore.GREEN+Style.BRIGHT+"[GENERAL]-----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_result)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_tags) != []:

            print(Fore.GREEN+Style.BRIGHT+"[TYPE]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_tags)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

def url_dns(apikey, url):

    response = requests.get("https://api.xforce.ibmcloud.com/resolve/" + url, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()
   
    dict_domain = {}

    if 'AAAA' in respuesta:
        array_aaaa = []

        dict_aaaa = {"Ipv6": respuesta["AAAA"]}

        if dict_aaaa != {"Ipv6": []}:
        
            array_aaaa.append(dict_aaaa)

        if array_aaaa != []:

            dict_domain.update({"AAAA": array_aaaa})

    if 'MX' in respuesta:

        array_mx = []

        dict_mx = {"MX": respuesta["MX"]}

        if dict_mx != {"MX": []}:
        
            array_mx.append(dict_mx)

        if array_mx != []:

            dict_domain.update({"MX": array_mx})

    if 'TXT' in respuesta:

        array_txt = []

        dict_txt = {"TXT": respuesta["TXT"]}

        if dict_txt != {"TXT": []}:

            array_txt.append(dict_txt)

        if array_txt != []:

            dict_domain.update({"TXT": array_txt})

    try:

        for Passive in respuesta["Passive"]:

            if 'query' != None:

                array_query = []

                dict_passive = {"query": respuesta["Passive"].get("query", '')}

        array_query.append(dict_passive)

        dict_domain.update({"Passive": array_query})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain = []

            dict_pass = {"value": respuesta["Passive"]["records"][0]["value"],
                        "type": respuesta["Passive"]["records"][0]["type"],
                        "recordType": respuesta["Passive"]["records"][0]["recordType"],
                        "first": respuesta["Passive"]["records"][0]["first"],
                        "last": respuesta["Passive"]["records"][0]["last"]}

        array_domain.append(dict_pass)

        dict_domain.update({"Passive1": array_domain})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain1 = []

            dict_pass1 = {"value": respuesta["Passive"]["records"][1]["value"],
                        "type": respuesta["Passive"]["records"][1]["type"],
                        "recordType": respuesta["Passive"]["records"][1]["recordType"],
                        "first": respuesta["Passive"]["records"][1]["first"],
                        "last": respuesta["Passive"]["records"][1]["last"]}

        array_domain1.append(dict_pass1)

        dict_domain.update({"Passive2": array_domain1})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain2 = []

            dict_pass2 = {"value": respuesta["Passive"]["records"][2]["value"],
                        "type": respuesta["Passive"]["records"][2]["type"],
                        "recordType": respuesta["Passive"]["records"][2]["recordType"],
                        "first": respuesta["Passive"]["records"][2]["first"],
                        "last": respuesta["Passive"]["records"][2]["last"]}

        array_domain2.append(dict_pass2)

        dict_domain.update({"Passive3": array_domain2})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain3 = []

            dict_pass3 = {"value": respuesta["Passive"]["records"][3]["value"],
                        "type": respuesta["Passive"]["records"][3]["type"],
                        "recordType": respuesta["Passive"]["records"][3]["recordType"],
                        "first": respuesta["Passive"]["records"][3]["first"],
                        "last": respuesta["Passive"]["records"][3]["last"]}

        array_domain3.append(dict_pass3)

        dict_domain.update({"Passive4": array_domain3})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:

        for Passive in respuesta["Passive"]:

            array_domain4 = []

            dict_pass4 = {"value": respuesta["Passive"]["records"][4]["value"],
                        "type": respuesta["Passive"]["records"][4]["type"],
                        "recordType": respuesta["Passive"]["records"][4]["recordType"],
                        "first": respuesta["Passive"]["records"][4]["first"],
                        "last": respuesta["Passive"]["records"][4]["last"]}

        array_domain4.append(dict_pass4)

        dict_domain.update({"Passive5": array_domain4})

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_query) != []:

            print(Fore.GREEN+Style.BRIGHT+"[QUERY]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_query)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain1) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE1]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain1)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain2) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE2]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain3) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE3]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain3)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_domain4) != []:

            print(Fore.GREEN+Style.BRIGHT+"[PASSIVE4]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domain4)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError, IndexError):

        pass

    try:
        
        if (array_aaaa) != []:

            print(Fore.GREEN+Style.BRIGHT+"[IPV6]------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_aaaa)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_mx) != []: 

            print(Fore.GREEN+Style.BRIGHT+"[MX]--------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_mx)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_txt) != []: 
            print(Fore.GREEN+Style.BRIGHT+"[TXT]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_txt)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    if dict_domain == {}:
        
        print(Fore.RED+Style.BRIGHT+"[DNS]-------------------------------------------------------------------------------------[NO RESULTS]"+Fore.RESET+Style.RESET_ALL)

def url_whois(apikey, url):
    
    response = requests.get("https://api.xforce.ibmcloud.com/whois/" + url, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    array_urlwhois = respuesta

    dict_urlwhois = {}

    dict_urlwhois = array_urlwhois
    
    if (array_urlwhois) == {'extended': None}:

        print(Fore.RED+Style.BRIGHT+"[WHOIS]--------------------------------------------------------------------------- ---[NO RESULTS]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(Cursor.DOWN(1))
        
    else:

        print(Fore.GREEN+Style.BRIGHT+"[WHOIS]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_urlwhois)
        print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def mal_hash(apikey, hash):
    
    response = requests.get("https://api.xforce.ibmcloud.com/malware/" + hash, auth=HTTPBasicAuth(api_key, password))

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    if response.status_code == 404:

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Hash solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()
    
    respuesta = response.json()

    dict_hash = {}

    try:
        
        for malware in respuesta["malware"]:

            if 'type' != None:

                array_general = []

                dict_general = {"created": respuesta["malware"].get("created", ''),
                                "risk": respuesta["malware"].get("risk", ''),       
                                "type": respuesta["malware"].get("type", ''),
                                "Hash": respuesta["malware"].get("md5", '')}

        array_general.append(dict_general)

        dict_hash.update({"General": array_general})

    except (KeyError, UnboundLocalError, TypeError):

        pass

    try:
        
        for malware in respuesta["malware"]:

            try:
                
                if 'type' != None:

                    array_malw = []

                    dict_malw = {}

                    dict_malw.update({"type": respuesta["malware"]["origins"]["CnCServers"]["rows"][-1]["type"]})

            except (KeyError, TypeError):

                pass

            try:

                if 'md5' != None:
                
                    dict_malw.update({"Hash": respuesta["malware"]["origins"]["CnCServers"]["rows"][-1]["md5"]})

            except (KeyError, TypeError):

                pass

            try:

                if 'domain' != None:

                    dict_malw.update({"IP": respuesta["malware"]["origins"]["CnCServers"]["rows"][-1]["domain"]})

            except (KeyError, TypeError):

                pass

            try:
                if 'port' != None:
            
                    dict_malw.update({"port": respuesta["malware"]["origins"]["CnCServers"]["rows"][-1]["port"]})

            except (KeyError, TypeError):

                pass

            try:

                if 'source' != None:
            
                    dict_malw.update({"Fuente": respuesta["malware"]["origins"]["external"]["source"]})

            except (KeyError, TypeError):

                pass

            try:

                if 'malwareType' != None:

                    dict_malw.update({"Tipo": respuesta["malware"]["origins"]["external"]["malwareType"]})

            except (KeyError, TypeError):

                pass

            try: 
                
                if 'family' != None:

                    dict_malw.update({"Family": respuesta["malware"]["origins"]["external"]["family"][-1]})

            except (KeyError, TypeError):

                pass

            try:

                if 'platform' != None:

                    dict_malw.update({"Platform": respuesta["malware"]["origins"]["external"]["platform"]})

            except (KeyError, TypeError):

                pass

            try:

                if 'risk' != None:

                    dict_malw.update({"Risk": respuesta["malware"]["origins"]["external"]["risk"]})

            except (KeyError, TypeError):

                pass
            
            try:

                if 'filepath' != None:

                    dict_malw.update({"filepath": respuesta["malware"]["origins"]["CnCServers"]["rows"][-1]["filepath"]})

            except (KeyError, TypeError):

                pass

        array_malw.append(dict_malw)

        dict_hash.update({"malware": array_malw})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_general) != []:

            print(Fore.GREEN+Style.BRIGHT+"[GENERAL]-----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_general)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_malw) != []:

            print(Fore.GREEN+Style.BRIGHT+"[MALWARE]-----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_malw)
            print(Cursor.DOWN(1))

    except (KeyError, UnboundLocalError):

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))
        

