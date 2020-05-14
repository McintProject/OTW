# -------------------------------------------------------------------------------
# Name:         ShodanWrapper.py
# Purpose:      Shodan module to obtain information related about an IP:
#               (ASN, ISP, Ports & Services, CVE's...)
#
# Author:      Jorge Iturria 
#
# Created:     30/04/2020
# Copyright:   (c) Jorge iturria 2020
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests
import json
from colorama import *
import os
import re

from modulos.config import SHODAN_API_KEY

def ip_f(apikey, ip):

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

    response = requests.get("https://api.shodan.io/shodan/host/" + str(ip) + "?key=" + SHODAN_API_KEY)

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
    
    
    servicios = response.json()

    dict_shodan = {}

    array_general_info = []

    if 'ip_str' in servicios:

        dict_general_info = {"IP": servicios.get("ip_str", ''),
                             "last_update": servicios.get("last_update", ''),
                             "country_name": servicios.get("country_name", ''),
                             "country_code": servicios.get("country_code", ''),
                             "city": servicios.get("city", ''),
                             "latitude": servicios.get("latitude", ''),
                             "longitude": servicios.get("longitude", ''),
                             "org": servicios.get("org", ''),
                             "asn": servicios.get("asn", ''),
                             "os":servicios.get("os", '')}

    array_general_info.append(dict_general_info)

    if len(array_general_info) !=0:

        dict_shodan.update({"Información general":array_general_info})

    array_ports = []

    if 'domains' in servicios:

        try: 
            
            for domains in servicios["domains"]:

                if 'domains' != []:

                    array_domains = []

                    dict_domains = {"domains": servicios["domains"]}

                array_domains.append(dict_domains)

                dict_shodan.update({"Domains": array_domains})

        except (KeyError, UnboundLocalError):

            pass

    if 'hostnames' in servicios:

        try: 
            
            for hostnames in servicios["domains"]:

                if 'hostnames' != []:

                    array_hostnames = []

                    dict_hostnames = {"hostnames": servicios["hostnames"]}

                array_hostnames.append(dict_hostnames)

                dict_shodan.update({"Hostnames": array_hostnames})

        except (KeyError, UnboundLocalError):

            pass
        
    try:
    
        for ports in servicios["ports"]:
            
            if "ports" != []:

                dict_ports = {"OpenPorts": servicios["ports"]}

        array_ports.append(dict_ports)

        dict_shodan.update({"Puertos":array_ports})

    except (KeyError, UnboundLocalError):

        pass

    try:

        array_data = []

        for data in servicios["data"]:

            dict_data = {}
                
            if  "data" != None:

                dict_data.update({"port": servicios["data"][0]["port"]})    
                
            if  "data" != None:

                dict_data.update({"product": servicios["data"][0]["product"]})

            try:
            
                if  "data" != None:

                    dict_data.update({"version": servicios["data"][0]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data.update({"CERTIFICATES": servicios["data"][0]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][0]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][0]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][0]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][0]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][0]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][0]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][0]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data.append(dict_data)

        dict_shodan.update({"data":array_data})

    except (KeyError, UnboundLocalError):

        pass

    try:

        array_data1 = []

        for data in servicios["data"]:

   
            if  "data" != None:

                dict_data1 = {}

                dict_data1.update({"port": servicios["data"][1]["port"]})

            
            if  "data" != None:

                dict_data1.update({"product": servicios["data"][1]["product"]})

            try:
                
                if  "data" != None:

                    dict_data1.update({"version": servicios["data"][1]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data1.update({"CERTIFICATES": servicios["data"][1]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][1]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][1]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][1]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][1]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][1]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][1]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][1]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data1.append(dict_data1)

        dict_shodan.update({"data1":array_data1})

    except (KeyError, UnboundLocalError):

        pass

    try:

        array_data2 = []

        for data in servicios["data"]:

            dict_data2 = {}
                
            if  "data" != None:

                dict_data2.update({"port": servicios["data"][2]["port"]})
                
            if  "data" != None:

                dict_data2.update({"product": servicios["data"][2]["product"]})

            try:
                
                if  "data" != None:

                    dict_data2.update({"version": servicios["data"][2]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data2.update({"CERTIFICATES": servicios["data"][2]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][2]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][2]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][2]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][2]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][2]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][2]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][2]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data2.append(dict_data2)

        dict_shodan.update({"data2":array_data2})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data3 = []

        for data in servicios["data"]:

            dict_data3 = {}
                
            if  "data" != None:

                dict_data3.update({"port": servicios["data"][3]["port"]})
                
            if  "data" != None:

                dict_data3.update({"product": servicios["data"][3]["product"]})

            try:
                
                if  "data" != None:

                    dict_data3.update({"version": servicios["data"][3]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data3.update({"CERTIFICATES": servicios["data"][3]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][3]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][3]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][3]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][3]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][3]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][3]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][3]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data3.append(dict_data3)

        dict_shodan.update({"data3":array_data3})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data4 = []

        for data in servicios["data"]:

            dict_data4 = {}
                
            if  "data" != None:

                dict_data4.update({"port": servicios["data"][4]["port"]})

            if  "data" != None:

                dict_data4.update({"product": servicios["data"][4]["product"]})

            try:

                if  "data" != None:

                    dict_data4.update({"version": servicios["data"][4]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data4.update({"CERTIFICATES": servicios["data"][4]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][4]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][4]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][4]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][4]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][4]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][4]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][4]["ssl"]["cipher"]["name"]})
                                       

            except KeyError:

                pass

        array_data4.append(dict_data4)

        dict_shodan.update({"data4":array_data4})

    except (KeyError , IndexError, UnboundLocalError):

        pass

    try:

        array_data5 = []

        for data in servicios["data"]:

            #Creamos diccionario 

            dict_data5 = {}

            if  "data" != None:

                dict_data5.update({"port": servicios["data"][5]["port"]})

            if  "data" != None:

                dict_data5.update({"product": servicios["data"][5]["product"]})

            try:
                
                if  "data" != None:

                    dict_data5.update({"version": servicios["data"][5]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data5.update({"CERTIFICATES": servicios["data"][5]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][5]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][5]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][5]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][5]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][5]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][5]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][5]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data5.append(dict_data5)

        dict_shodan.update({"data5":array_data5})

    except  (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data6 = []

        for data in servicios["data"]:

            dict_data6 = {}

            if  "data" != None:

                dict_data6.update({"port": servicios["data"][6]["port"]})

            if  "data" != None:

                dict_data6.update({"product": servicios["data"][6]["product"]})

            try:
                
                if  "data" != None:

                    dict_data6.update({"version": servicios["data"][6]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data6.update({"CERTIFICATES": servicios["data"][6]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][6]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][6]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][6]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][6]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][6]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][6]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][6]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data6.append(dict_data6)

        dict_shodan.update({"data6":array_data6})

    except  (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data7 = []

        for data in servicios["data"]:

            dict_data7 = {}


            if  "data" != None:

                dict_data7.update({"port": servicios["data"][7]["port"]})

            if  "data" != None:

                dict_data7.update({"product": servicios["data"][7]["product"]})

            try:
                
                if  "data" != None:

                    dict_data7.update({"version": servicios["data"][7]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data7.update({"CERTIFICATES": servicios["data"][7]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][7]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][7]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][7]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][7]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][7]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][7]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][7]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        array_data7.append(dict_data7)

        dict_shodan.update({"data7":array_data7})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data8 = []

        for data in servicios["data"]:

            #Creamos diccionario 

            dict_data8 = {}


            if  "data" != None:

                dict_data8.update({"port": servicios["data"][8]["port"]})

            if  "data" != None:

                dict_data8.update({"product": servicios["data"][8]["product"]})

            try:
                
                if  "data" != None:

                    dict_data8.update({"version": servicios["data"][8]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data8.update({"CERTIFICATES": servicios["data"][8]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][8]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][8]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][8]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][8]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][8]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][8]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][8]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        # Añadimos el diccionario a la lista

        array_data8.append(dict_data8)

        # Añadimos la lista al diccionario principal

        dict_shodan.update({"data8":array_data8})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:

        array_data9 = []

        for data in servicios["data"]:

            #Creamos diccionario 

            dict_data9 = {}


            if  "data" != None:

                dict_data9.update({"port": servicios["data"][9]["port"]})

            if  "data" != None:

                dict_data9.update({"product": servicios["data"][9]["product"]})

            try:
                
                if  "data" != None:

                    dict_data9.update({"version": servicios["data"][9]["version"]})

            except KeyError:

                pass

            try:

                if "data" != None:

                    dict_data9.update({"CERTIFICATES": servicios["data"][9]["ssl"]["versions"],
                                       "sig_alg": servicios["data"][9]["ssl"]["cert"]["sig_alg"],
                                       "sha256": servicios["data"][9]["ssl"]["cert"]["fingerprint"]["sha256"],
                                       "sha1": servicios["data"][9]["ssl"]["cert"]["fingerprint"]["sha1"],
                                       "bits": servicios["data"][9]["ssl"]["cert"]["pubkey"]["bits"],
                                       "type": servicios["data"][9]["ssl"]["cert"]["pubkey"]["type"],
                                       "CN": servicios["data"][9]["ssl"]["cert"]["subject"]["CN"],
                                       "name": servicios["data"][9]["ssl"]["cipher"]["name"]})

            except KeyError:

                pass

        # Añadimos el diccionario a la lista

        array_data9.append(dict_data9)

        # Añadimos la lista al diccionario principal

        dict_shodan.update({"data9":array_data9})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:
    
        array_vuln = []

        for vulns in servicios["vulns"]:

            if 'vulns' != []:

                dict_vuln = {"Vulns": servicios["vulns"]}

        array_vuln.append(dict_vuln)

        dict_shodan.update({"Vulnerabilities":array_vuln})

    except (KeyError, IndexError, UnboundLocalError):

        pass

    if (array_general_info) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_general_info)
        print(Cursor.DOWN(1))  

    try:
        
        if (array_domains) != []:
            print(Fore.GREEN+Style.BRIGHT+"[DOMAINS]----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_domains)
            print(Cursor.DOWN(1))

    except (KeyError, IndexError, UnboundLocalError):

        pass

    try:
        
        if (array_hostnames) != []:
            print(Fore.GREEN+Style.BRIGHT+"[HOSTNAMES]--------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_hostnames)
            print(Cursor.DOWN(1)) 

    except (KeyError, IndexError, UnboundLocalError):

        pass

    if (array_ports) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORTS]-----------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ports)
        print(Cursor.DOWN(1))  

    if (array_data) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data)
        print(Cursor.DOWN(1))

    if (array_data1) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data1)
        print(Cursor.DOWN(1)) 

    if (array_data2) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data2)
        print(Cursor.DOWN(1)) 

    if (array_data3) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data3)
        print(Cursor.DOWN(1)) 

    if (array_data4) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data4)
        print(Cursor.DOWN(1))

    if (array_data5) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data5)
        print(Cursor.DOWN(1))

    if (array_data6) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data6)
        print(Cursor.DOWN(1))

    if (array_data7) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data7)
        print(Cursor.DOWN(1))

    if (array_data8) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data8)
        print(Cursor.DOWN(1))

    if (array_data9) != []:
        
        print(Fore.GREEN+Style.BRIGHT+"[PORT DATA]-------------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_data9)
        print(Cursor.DOWN(1))

    if (array_vuln) != []:

        print(Fore.GREEN+Style.BRIGHT+"[VULNERABILITIES]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_vuln)
        print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))



