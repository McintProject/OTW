# -------------------------------------------------------------------------------
# Name:         RiskIQWrapper.py
# Purpose:      RiskIQ module to retrieve information related about 
#                      a Domain, an IP, or a Certificate 
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
from colorama import *
import os
import re
from modulos.config import username, key

def risk_dme(apikei, dominio):
    
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
    
    auth =(username, key)
    
    data = {'query': dominio}
    
    url = 'https://api.passivetotal.org/v2/enrichment'
    
    response = requests.get(url, auth=auth, json=data)
    
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
    
    dict_riske = {}
    
    try:

        if "queryType" != None:
    
            array_enrichment = []

            dict_riskee = {"primaryDomain": respuesta.get("primaryDomain", ''),
    
                           "tld": respuesta.get("tld", ''),
    
                           "sinkhole": respuesta.get("sinkhole", ''),
    
                           "everCompromised": respuesta.get("everCompromised", ''),
    
                           "classification": respuesta.get("classification", ''),
    
                           "dynamicDns": respuesta.get("dynamicDns", '')}
    
        array_enrichment.append(dict_riskee)
 
        dict_riske.update({"Enrichment": array_enrichment})
    
    except (KeyError, UnboundLocalError, TypeError):
    
        pass
    
    try:

        if (array_enrichment) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[ENRICHMENT]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_enrichment)
    
            print(Cursor.DOWN(1))   
    
    except (KeyError, UnboundLocalError):
    
        pass
    
def risk_dmm(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/enrichment/malware'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskm = {}

    try:
        
        for results in respuesta["results"][:4]:
        
            if "results" != None:

                array_results = []

                dict_results = {"Malware": respuesta["results"][:4]}

            array_results.append(dict_results)

        dict_riskm.update({"Malware": array_results})

    except (KeyError, UnboundLocalError):

        pass
   
    try:
        
        if (array_results) != []:

            print(Fore.GREEN+Style.BRIGHT+"[MALWARE]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_results)
            print(Cursor.DOWN(1)) 

    except (KeyError, UnboundLocalError):

        pass

def risk_dmo(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/enrichment/osint'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()
    
    respuesta = response.json()

    dict_osint = {}

    try:
            
        for results in respuesta["results"][:4]:
            
            if "results" != None:

                array_osint = []

                dict_res = {"Osint": respuesta["results"][:4]}

            array_osint.append(dict_res)

        dict_osint.update({"Osint": array_osint})

    except (KeyError, UnboundLocalError):

        pass
    
    try:
        
        if (array_osint) != []:

            print(Fore.GREEN+Style.BRIGHT+"[OSINT]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_osint)
            print(Cursor.DOWN(1))  

    except (KeyError, UnboundLocalError):

        pass

def risk_dms(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/enrichment/subdomains'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    try:
        
        for subdomains in respuesta["subdomains"]:
        
            if "subdomains" != None:

                array_subdomains = []

                dict_risks = {"Subdomains": respuesta["subdomains"]}

            array_subdomains.append(dict_risks)

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_subdomains) != []:

            print(Fore.GREEN+Style.BRIGHT+"[SUBDOMAINS]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_subdomains)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_dmdns(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/dns/passive'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskdmdns = {}

    array_riskdmdns = []

    if "queryType" != None:

        dict_riskdmdns1 = {"DNSqueryType": respuesta.get("queryType", ''),
                           "DNSfirstSeen": respuesta.get("firstSeen", ''),
                           "DNSlastSeen": respuesta.get("lastSeen", '')}
        
        array_riskdmdns.append(dict_riskdmdns1)

        dict_riskdmdns.update({"Type": array_riskdmdns})

    try:
        
        for results in respuesta["results"]:

            if (results["resolveType"] != None):

                dict_risk_rtdns = {}

                dict_risk_rtdns.update({"resolveType": respuesta["results"][0]["resolveType"]})

            if (results["value"] != None):

                dict_risk_rtdns.update({"value": respuesta["results"][0]["value"]})

            if (results["resolve"] != None):

                dict_risk_rtdns.update({"resolve": respuesta["results"][0]["resolve"]})

            if (results["recordHash"] != None):

                dict_risk_rtdns.update({"recordHash": respuesta["results"][0]["recordHash"]})

            if (results["source"] != None):

                dict_risk_rtdns.update({"source": respuesta["results"][0]["source"][0]})
  
        array_riskdmdns.append(dict_risk_rtdns)
 
        dict_riskdmdns.update({"DNS": array_riskdmdns})
 
    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskdmdns) != []:

            print(Fore.GREEN+Style.BRIGHT+"[DNS]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskdmdns)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_dmuni(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/dns/passive/unique'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskdmuni = {}

    array_riskdmuni = []

    try:

        if "queryValue" != None:

            dict_riskuni = {}

            dict_riskuni.update({"queryValue": respuesta["queryValue"]}) 

    except (KeyError, UnboundLocalError):

        pass

    try:
        if "total" != None:

            dict_riskuni.update({"total": respuesta["total"]}) 

    except (KeyError, UnboundLocalError):

        pass

    array_riskdmuni.append(dict_riskuni) 

    dict_riskdmuni.update({"UniDNS": array_riskdmuni})

    try:
        
        for results in respuesta["results"]:
        
            if "results" != None:

                array_riskdmuni1 = []

                dict_riskdmuni1 = {"results": respuesta["results"][:9]}

                array_riskdmuni1.append(dict_riskdmuni1) 

        dict_riskdmuni.update({"UniDNS1": array_riskdmuni1})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskdmuni1) != []:

            print(Fore.GREEN+Style.BRIGHT+"[UNIQUE DNS]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskdmuni1)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_dmwhois(apikei, dominio):
    
    auth =(username, key)

    data = {'query': dominio}

    url = 'https://api.passivetotal.org/v2/whois'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskdmwhois = {}

    try:

        if 'domain' != None:

            array_riskdmwhois = []

            dict_dmwhois = {"domain": respuesta.get("domain", ''),
                            "organization": respuesta.get("organization", ''),
                            "registered": respuesta.get("registered", ''),
                            "expiresAt": respuesta.get("expiresAt", ''),
                            "registryUpdatedAt": respuesta.get("registryUpdatedAt", ''),
                            "contactEmail": respuesta.get("contactEmail", ''),
                            "registrar": respuesta.get("registrar", '')}

            array_riskdmwhois.append(dict_dmwhois)

        dict_riskdmwhois.update({"WHOIS": array_riskdmwhois})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for nameServers in respuesta["nameServers"]:

            if 'nameServers' != None:

                array_servers = []

                dict_servers = {"Name Servers": respuesta["nameServers"]}

            array_servers.append(dict_servers)

        dict_riskdmwhois.update({"Servers": array_servers})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskdmwhois) != []:

            print(Fore.GREEN+Style.BRIGHT+"[WHOIS]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskdmwhois)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_servers) != []:

            print(Fore.GREEN+Style.BRIGHT+"[SERVERS]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_servers)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def risk_ipe(apikei, ip):
    
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
    
    auth=(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/enrichment'

    response = requests.get(url, auth=auth, json=data)

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
 
    dict_riskeip = {}

    try:
        
        for queryType in respuesta:
            
            if "queryType" != None:

                array_enrichment = []

                dict_enrichment ={"queryType": respuesta.get("queryType", ''),
                                  "queryValue": respuesta.get("queryValue", ''),
                                  "sinkhole": respuesta.get("sinkhole", ''),
                                  "everCompromised": respuesta.get("everCompromised", ''),
                                  "autonomousSystemNumber": respuesta.get("autonomousSystemNumber", ''),
                                  "autonomousSystemName": respuesta.get("autonomousSystemName", ''),
                                  "network": respuesta.get("network", ''),
                                  "country": respuesta.get("country", ''),
                                  "latitude": respuesta.get("latitude", ''),
                                  "longitude": respuesta.get("longitude", ''),
                                  "dynamic": respuesta.get("dynamic", ''),
                                  "system_tags": respuesta["system_tags"]}

            array_enrichment.append(dict_enrichment)

        dict_riskeip.update({"Enrichment": array_enrichment})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_enrichment) != []:

            print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_enrichment)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_ipm(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/enrichment/malware'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskmip = {}

    try:
        
        for results in respuesta["results"][:4]:
        
            if "results" != None:

                array_results = []

                dict_results = {"Malware": respuesta["results"][:4]}

            array_results.append(dict_results)

        dict_riskmip.update({"Malware":array_results})

    except (KeyError, UnboundLocalError):

        pass
    
    try:
        
        if (array_results) != []:

            print(Fore.GREEN+Style.BRIGHT+"[MALWARE]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_results)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_ipo(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/enrichment/osint'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_osintip = {}

    try:
            
        for results in respuesta["results"][:4]:
            
            if "results" != None:

                array_osintip = []

                dict_res = {"Osint": respuesta["results"][:4]}

            array_osintip.append(dict_res)

        dict_osintip.update({"Osint": array_osintip})

    except (KeyError, UnboundLocalError):

        pass
    
    try:
        
        if (array_osintip) != []:

            print(Fore.GREEN+Style.BRIGHT+"[OSINT]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_osintip)
            print(Cursor.DOWN(1))  

    except (KeyError, UnboundLocalError):

        pass

def risk_ipdns(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/dns/passive'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskipdns = {}

    if "queryType" != None:

        array_riskipdns = []

        dict_riskipdns1 = {"DNSqueryType": respuesta.get("queryType", ''),
                           "DNSfirstSeen": respuesta.get("firstSeen", ''),
                           "DNSlastSeen": respuesta.get("lastSeen", '')}
      
        array_riskipdns.append(dict_riskipdns1)

        dict_riskipdns.update({"Type": array_riskipdns})

    try:
    
        for results in respuesta["results"]:

            dict_risk_rtdns = {}
            if (results["resolveType"] != None):
                dict_risk_rtdns.update({"resolveType": respuesta["results"][0]["resolveType"]})
            if (results["resolve"] != None):
                dict_risk_rtdns.update({"resolve": respuesta["results"][0]["resolve"]})
            if (results["recordHash"] != None):
                dict_risk_rtdns.update({"recordHash": respuesta["results"][0]["recordHash"]})
            if (results["source"] != None):
                dict_risk_rtdns.update({"source": respuesta["results"][0]["source"][0]})
            if (results["recordType"] != None):
                dict_risk_rtdns.update({"recordType": respuesta["results"][0]["recordType"]})
            if (results["collected"] != None):
                dict_risk_rtdns.update({"collected": respuesta["results"][0]["collected"]})

        array_riskipdns.append(dict_risk_rtdns)

        dict_riskipdns.update({"DNS": array_riskipdns})

    except UnboundLocalError:

        pass

    try:
        
        if (array_riskipdns) != []:

            print(Fore.GREEN+Style.BRIGHT+"[DNS]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskipdns)
            print(Cursor.DOWN(1))  

    except (KeyError, UnboundLocalError):

        pass

def risk_ipuni(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/dns/passive/unique'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskipuni = {}

    if "queryValue" != None:

        array_riskipuni = []

        dict_riskuni = {}

        dict_riskuni.update({"queryValue": respuesta["queryValue"]}) 

    if "total" != None:

        dict_riskuni.update({"total": respuesta["total"]}) 

    array_riskipuni.append(dict_riskuni) 

    dict_riskipuni.update({"UniDNS": array_riskipuni})

    try:
        
        for results in respuesta["results"]:
        
            if "results" != None:

                array_riskipuni1 = []

                dict_riskipuni1 = {"results": respuesta["results"][:9]}

                array_riskipuni1.append(dict_riskipuni1) 

        dict_riskipuni.update({"UniDNS1": array_riskipuni1})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskipuni1) != []:

            print(Fore.GREEN+Style.BRIGHT+"[UNIQUE DNS]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskipuni1)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_ipcert(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/ssl-certificate/history'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_ipcert = {}

    try:
    
        for results in respuesta["results"]:
        
            if "results" != None:
                array_riskipcert = []

                dict_riskipres = {"Certificates": respuesta["results"][:5]}

                array_riskipcert.append(dict_riskipres) 

        dict_ipcert.update({"Certificates": array_riskipcert})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskipcert) != []:

            print(Fore.GREEN+Style.BRIGHT+"[CERTIFICATES]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskipcert)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

def risk_ipwhois(apikei, ip):
    
    auth =(username, key)

    data = {'query': ip}

    url = 'https://api.passivetotal.org/v2/whois'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_riskipwhois = {}

    try:

        if 'domain' != None:

            array_riskipwhois = []

            dict_ipwhois = {"domain": respuesta.get("domain", ''),
                            "organization": respuesta.get("organization", ''),
                            "registered": respuesta.get("registered", ''),
                            "expiresAt": respuesta.get("expiresAt", ''),
                            "registryUpdatedAt": respuesta.get("registryUpdatedAt", ''),
                            "contactEmail": respuesta.get("contactEmail", ''),
                            "registrar": respuesta.get("registrar", ''),
                            "whoisServer": respuesta.get("whoisServer", '')}

            array_riskipwhois.append(dict_ipwhois)

        dict_riskipwhois.update({"WHOIS": array_riskipwhois})

    except (KeyError, UnboundLocalError):

        pass

    try:

         for resgistrant in respuesta["registrant"]:

            if 'organization' != None:

                array_registrant = []

                dict_registrant = {"organization": respuesta["registrant"].get("organization", ''),
                                "city": respuesta["registrant"].get("city", ''),
                                "street": respuesta["registrant"].get("street", ''),
                                "postalCode": respuesta["registrant"].get("postalCode", ''),
                                "state": respuesta["registrant"].get("state", ''),
                                "country": respuesta["registrant"].get("country", '')}

                array_registrant.append(dict_registrant)

            dict_riskipwhois.update({"Registrant": array_registrant})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for nameServers in respuesta["nameServers"]:

            if 'nameServers' != None:

                array_ipservers = []

                dict_ipservers = {"Name Servers": respuesta["nameServers"]}

            array_ipservers.append(dict_ipservers)

        dict_riskipwhois.update({"Servers": array_ipservers})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskipwhois) != []:

            print(Fore.GREEN+Style.BRIGHT+"[WHOIS]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskipwhois)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_registrant) != []:

            print(Fore.GREEN+Style.BRIGHT+"[REGISTRANT]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_registrant)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_ipservers) != []:

            print(Fore.GREEN+Style.BRIGHT+"[SERVERS]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_ipservers)
            print(Cursor.DOWN(1)) 

    except (KeyError, UnboundLocalError):

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))


def risk_cert(apikei, hash):
    
    hashp = re.compile(r'\b[0-9a-f]{40}\b')

    if hashp.search(hash): 

        print(Fore.GREEN+"Hash introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Hash introducido no es válido. Lanze de nuevo el Programa e introdúzcalo de nuevo"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()

    auth =(username, key)

    data = {'query': hash}

    url = 'https://api.passivetotal.org/v2/ssl-certificate'

    response = requests.get(url, auth=auth, json=data)

    if response.status_code == 401:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)

        print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")

        print(Cursor.DOWN(1))

        exit()

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Certificado solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    respuesta = response.json()

    dict_riskcert = {}

    try:
        
        for results in respuesta["results"]:

            if 'sha1' != None:

                array_riskcert = []
                dict_certs = {}
                dict_certs.update({"sha1": respuesta["results"][0]["sha1"]})
            if results["expirationDate"] != None:
                dict_certs.update({"expirationDate": respuesta["results"][0]["expirationDate"]})
            if results["fingerprint"] != None:
                dict_certs.update({"fingerprint": respuesta["results"][0]["fingerprint"]})
            if results["firstSeen"] != None:
                dict_certs.update({"firstSeen": respuesta["results"][0]["firstSeen"]})
            if results["issueDate"] != None:
                dict_certs.update({"issueDate": respuesta["results"][0]["issueDate"]})
            if results["issuerCommonName"] != None:
                dict_certs.update({"ExpeditorName": respuesta["results"][0]["issuerCommonName"]})
            if results["issuerCountry"] != None:
                dict_certs.update({"ExpeditorCountry": respuesta["results"][0]["issuerCountry"]})
            if results["issuerOrganizationUnitName"] != None:
                dict_certs.update({"ExpeditorOrganization": respuesta["results"][0]["issuerOrganizationUnitName"]})
            if results["issuerOrganizationUnitName"] != None:
                dict_certs.update({"ExpeditorOrganizationUnitName": respuesta["results"][0]["issuerOrganizationUnitName"]})
            if results["subjectCommonName"] != None:
                dict_certs.update({"CompanyCommonName": respuesta["results"][0]["subjectCommonName"]})
            if results["subjectOrganizationName"] != None:
                dict_certs.update({"CompanyName": respuesta["results"][0]["subjectOrganizationName"]})
            if results["subjectCountry"] != None:
                dict_certs.update({"CompanyCountry": respuesta["results"][0]["subjectCountry"]})
            if results["subjectLocalityName"] != None:
                dict_certs.update({"CompanyLocalityName": respuesta["results"][0]["subjectLocalityName"]})
            try:
                if results["subjectAlternativeNames"] != None:
                    dict_certs.update({"CompanyAlternativeNames": respuesta["results"][0]["subjectAlternativeNames"][0]})
            except IndexError:
                pass
            if results["serialNumber"] != None:
                dict_certs.update({"serialNumber": respuesta["results"][0]["serialNumber"]})

            array_riskcert.append(dict_certs)

        dict_riskcert.update({"Certificado": array_riskcert})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        if (array_riskcert) != []:

            print(Fore.GREEN+Style.BRIGHT+"[CERTIFICATES]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_riskcert)
            print(Cursor.DOWN(1))   

    except (KeyError, UnboundLocalError):

        pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))
