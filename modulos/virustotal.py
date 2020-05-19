# -------------------------------------------------------------------------------
# Name:         VirusTotalWrapper.py
# Purpose:      Virus Total module to obtain information related about an IP, a Domain, an URL or a Hash
#
# Author:      Jorge I
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests
import simplejson as json
from json import JSONDecodeError
import re
from colorama import *
import os

from modulos.config import VIRUS_TOTAL_API_KEY

def vipm_f(apikey, ip):

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

    params = {'apikey':VIRUS_TOTAL_API_KEY, 'ip':ip}

    url = "https://virustotal.com/vtapi/v2/ip-address/report"

    try:
        
        response = requests.get(url, params=params)

        if response.status_code == 404: 

            print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la IP solicitada"+Fore.RESET+Style.RESET_ALL)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
            print(Cursor.DOWN(1))
            exit()

        ips = response.json()

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()
    
    dict_ips = {}

    array_resources = []

    resource = ips

    if'verbose_msg' in resource:
        
        dict_resources = {"IN" : resource.get("verbose_msg", ''),
                          "country" : resource.get("country", ''),
                          "as_owner" : resource.get("as_owner", ''),
                          "continent" : resource.get("continent", ''),
                          "asn" : resource.get("asn", ''),
                          "network" : resource.get("network", ''),
                          "whois" : resource.get("whois", '')}
    
    array_resources.append(dict_resources)
    
    dict_ips.update({"Resources":array_resources})
    
    array_certif = []

    try:
    
        if 'last_https_certificate' in ips:
        
            for last_https_certificate in ips["last_https_certificate"]:

                if (last_https_certificate[0]) != None:

                    dict_certif = {"signature_algorithm": ips["last_https_certificate"].get("signature_algorithm", ''),
                                "thumbprint_sha256": ips["last_https_certificate"].get("thumbprint_sha256", ''),
                                "version": ips["last_https_certificate"].get("version", ''),
                                "OU": ips["last_https_certificate"]["subject"].get("OU", ''),
                                "CN": ips["last_https_certificate"]["subject"].get("CN", ''),
                                "validity": ips["last_https_certificate"]["validity"].get("not_after", '')}

            array_certif.append(dict_certif)

            dict_ips.update({"HTTPS_Certificates": array_certif})

    except UnboundLocalError:

        pass

    array_resol = []

    try:
    
        for resolutions in ips["resolutions"][:10]:

            if 'resolutions' != None:

                dict_resol = {"hostname": resolutions.get("hostname", ''),  
                            "last_resolved": resolutions.get("last_resolved", '')} 

            array_resol.append(dict_resol)    

        dict_ips.update({"Resolutions": array_resol})

    except UnboundLocalError:

        pass

    array_urls = []

    try:
    
        if 'detected_urls' in ips:
            
            for detected_urls in ips["detected_urls"][:10]:

                if 'detected_urls' != None:

                    dict_url = {"url" : detected_urls.get("url", ''),
                                "positives" : detected_urls.get("positives", ''),
                                "scan_date" : detected_urls.get("scan_date", '')}

                array_urls.append(dict_url)
 
            dict_ips.update({"detected_urls":array_urls})

    except UnboundLocalError:

        pass
    
    array_downloaded = []

    try:
        
        if 'detected_downloaded_samples' in ips:
        
            for detected_downloaded_samples in ips["detected_downloaded_samples"][:10]:

                if 'detected_downloaded_samples' != None:

                    dict_downloaded = {"sha256": detected_downloaded_samples.get("sha256", ''),
                                    "positives": detected_downloaded_samples.get("positives", ''),
                                    "date": detected_downloaded_samples.get("date", '')}

                array_downloaded.append(dict_downloaded)

            dict_ips.update({"Downloaded Samples": array_downloaded})

    except UnboundLocalError:

        pass

    array_comunic = []

    try:
    
        if 'detected_communicating_samples' in ips:
            
            for detected_communicating_samples in ips["detected_communicating_samples"][:10]:

                if 'detected_communicating_samples' != None:

                    dict_comunic = {"sha256": detected_communicating_samples.get("sha256", ''),
                                    "positives": detected_communicating_samples.get("positives", ''),
                                    "date": detected_communicating_samples.get("date", '')}
 
                array_comunic.append(dict_comunic)

            dict_ips.update({"Communicating_Samples": array_comunic})

    except UnboundLocalError:

        pass
    
    if (array_resources) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RESOURCES]-------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_resources)
        print(Cursor.DOWN(1))

    if (array_certif) != []:

        print(Fore.GREEN+Style.BRIGHT+"[CERTIFICATES]----------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_certif)
        print(Cursor.DOWN(1))

    if (array_resol) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RESOLUTIONS]-----------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_resol)
        print(Cursor.DOWN(1))

    if (array_urls) != []:

        print(Fore.GREEN+Style.BRIGHT+"[DETECTED URL's]--------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_urls)
        print(Cursor.DOWN(1))   

    if (array_downloaded) != []:

        print(Fore.GREEN+Style.BRIGHT+"[DETECTED DOWNLOADED SAMPLES]-------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_downloaded)
        print(Cursor.DOWN(1))

    if (array_comunic) != []:

        print(Fore.GREEN+Style.BRIGHT+"[COMMUNICATING SAMPLES]-------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_comunic)
        print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def vdm_f(apikey, dominio):

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

    params = {'apikey':VIRUS_TOTAL_API_KEY, 'domain':dominio}

    url = "https://www.virustotal.com/vtapi/v2/domain/report"

    try:
        
        response = requests.get(url, params=params)
    
        if response.status_code == 404: 

            print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Dominio solicitado"+Fore.RESET+Style.RESET_ALL)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
            print(Cursor.DOWN(1))
            exit()
        
        dominios = response.json()

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()
    
    dict_dm = {}

    array_general = []
        
    if "verbose_msg" != None:

        dict_general = {}

        dict_general.update({"Domain": dominios["verbose_msg"]})

    try: 

        if "popularity_ranks" != None:
            dict_general.update({"AlexaRank": dominios["popularity_ranks"]["Alexa"]["rank"]})
            dict_general.update({"MajesticRank": dominios["popularity_ranks"]["Majestic"]["rank"]})
            dict_general.update({"StatvooRank": dominios["popularity_ranks"]["Statvoo"]["rank"]})
            dict_general.update({"CiscoUmbrella": dominios["popularity_ranks"]["Cisco Umbrella"]["rank"]})
            dict_general.update({"Quantcast": dominios["popularity_ranks"]["Quantcast"]["rank"]})

    except KeyError:

        pass

    try:
    
        if "Webutation domain info" != None:

            dict_general.update({"Webutation": dominios["Webutation domain info"]["Verdict"]})
            dict_general.update({"Webutation": dominios["Webutation domain info"]["Safety score"]})

    except KeyError:

        pass

    try:
    
        if "BitDefender domain info" != None:

            dict_general.update({"Bitdefender": dominios["BitDefender domain info"]})

    except KeyError:

        pass

    try:
    
        if "Alexa domain info" != None:
            dict_general.update({"Alexa": dominios["Alexa domain info"]})

    except KeyError:

        pass

    try:
    
        if "whois" != None:

            dict_general.update({"Whois": dominios["whois"]})

    except KeyError:

        pass

    array_general.append(dict_general)

    dict_dm.update({"General": array_general})

    array_resolutions = []
                
    try:
        
        if 'resolutions' in dominios:
    
            for resolutions in dominios["resolutions"]: 

                if 'resolutions' != None:

                    dict_resolutions = {"last_resolved": resolutions.get("last_resolved", ''),
                                        "ip_address": resolutions.get("ip_address", '')}

                array_resolutions.append(dict_resolutions)

        if len(array_resolutions) != 0:
            
            dict_dm.update({"resolutions":array_resolutions})

    except UnboundLocalError:

        pass

    array_dns_records = []

    try:
        
        if 'dns_records' in dominios:

            for dns_records in dominios["dns_records"]:
                
                if 'dns_records' != None:

                    dict_dns_records = {"type": dns_records.get("type", ''),
                                        "value": dns_records.get("value", '')}

                array_dns_records.append(dict_dns_records)

        if len(array_dns_records) != 0:

            dict_dm.update({"DNS":array_dns_records})

    except UnboundLocalError:

        pass

    array_certif = []

    try:
        
        if 'last_https_certificate' in dominios:
        
            for last_https_certificate in dominios["last_https_certificate"]:

                if 'last_https_certificate' != None:

                    dict_certif = {"signature_algorithm": dominios["last_https_certificate"].get("signature_algorithm", ''),
                                "thumbprint_sha256": dominios["last_https_certificate"].get("thumbprint_sha256", ''),
                                "version": dominios["last_https_certificate"].get("version", ''),
                                "CN": dominios["last_https_certificate"]["subject"].get("CN", ''),
                                "validity": dominios["last_https_certificate"]["validity"].get("not_after", '')}

            array_certif.append(dict_certif)

            dict_dm.update({"HTTPS_Certificates": array_certif})

    except UnboundLocalError:

        pass

    array_detected_urls = []
             
    try:
        
        if 'detected_urls' in dominios:

            for  detected_urls in dominios["detected_urls"]:

                if 'detected_urls'!= None:

                    dict_detected_urls = {"scan_date": detected_urls.get("scan_date", ''),
                                        "url": detected_urls.get("url", ''),
                                        "positives": detected_urls.get("positives", '')}

                array_detected_urls.append(dict_detected_urls)

            if len(array_detected_urls) != 0:

                dict_dm.update({"detected_urls":array_detected_urls})

    except UnboundLocalError:

        pass

    array_detected_downloaded_samples = []

    try:
        
        if 'detected_downloaded_samples' in dominios:

            for detected_downloaded_samples in dominios["detected_downloaded_samples"][:10]:

                if 'detected_downloaded_samples' != None:

                    dict_detected_downloaded_samples = {"sha256": detected_downloaded_samples.get("sha256", ''),
                                                            "positives": detected_downloaded_samples.get("positives", ''),
                                                            "date": detected_downloaded_samples.get("date", '')}

                array_detected_downloaded_samples.append(dict_detected_downloaded_samples)
        
            if len(detected_downloaded_samples) != 0:

                dict_dm.update({"detected_downloaded_samples":array_detected_downloaded_samples})

    except UnboundLocalError:

        pass

    array_detected_communicating_samples = []

    try:
        
        if 'detected_communicating_samples' in dominios:

            for detected_communicating_samples in dominios["detected_communicating_samples"][:10]:

                if 'detected_communicating_samples' != None:

                    dict_detected_communicating_samples = {"date": detected_communicating_samples.get("date", ''),
                                                            "positives": detected_communicating_samples.get("positives", ''),
                                                            "sha256": detected_communicating_samples.get("sha256", '')}

            array_detected_communicating_samples.append(dict_detected_communicating_samples)

            dict_dm.update({"detected_communicating_samples":array_detected_communicating_samples})

    except UnboundLocalError:

        pass
        
    array_subdomains = []

    subdomains = dominios

    try:
        
        if 'subdomains' in dominios:
    
            dict_subdomains = {"subdomains": subdomains.get("subdomains", '')}

            array_subdomains.append(dict_subdomains)

        if len(array_subdomains) != 0:

            dict_dm.update({"Subdominios":array_subdomains})

    except UnboundLocalError:

        pass

    if (array_general) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GENERAL]--------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_general)
        print(Cursor.DOWN(1))

    if (array_resolutions) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RESOLUTIONS]----------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_resolutions)
        print(Cursor.DOWN(1))

    if (array_dns_records) != []:

        print(Fore.GREEN+Style.BRIGHT+"[DNS RECORDS]----------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_dns_records)
        print(Cursor.DOWN(1))

    if (array_certif) != []:

        print(Fore.GREEN+Style.BRIGHT+"[CERTIFICATES]---------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_certif)
        print(Cursor.DOWN(1))  

    try:

        if (array_detected_urls) != []:

            print(Fore.GREEN+Style.BRIGHT+"[DETECTED URL's]---------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_detected_urls)
            print(Cursor.DOWN(1)) 

    except UnboundLocalError:

        pass

    try:

        if (detected_downloaded_samples) != []:

            print(Fore.GREEN+Style.BRIGHT+"[DETECTED DOWNLOADED SAMPLES]--------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_detected_downloaded_samples)
            print(Cursor.DOWN(1))   

    except UnboundLocalError:

        pass

    try:

        if (detected_communicating_samples) != []:

            print(Fore.GREEN+Style.BRIGHT+"[DETECTED COMUNICATING SAMPLES]-----------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_detected_communicating_samples)
            print(Cursor.DOWN(1))

    except UnboundLocalError:

            pass

    if (array_subdomains) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SUBDOMAINS]----------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print()
        print(array_subdomains)
        print(Cursor.DOWN(1))
    
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def url_f(apikey, resource):

        params = {'apikey':VIRUS_TOTAL_API_KEY, 'resource':resource}

        url = "https://virustotal.com/vtapi/v2/url/report"

        try:
            
            response = requests.get(url, params=params)

            if response.status_code == 404: 

                print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la URL solicitada"+Fore.RESET+Style.RESET_ALL)
                print(Cursor.DOWN(1))
                print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
                print(Cursor.DOWN(1))
                exit()  

            urls = response.json()

        except json.decoder.JSONDecodeError:

            print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado")
            print(Cursor.DOWN(1))

            exit()

        dict_url = {}

        array_url = []

        try:
        
            if 'scan_id' in urls:

                dict_urlres = {"Scan_id": urls.get("scan_id", ''),
                            "Resource": urls.get("resource", ''),
                            "Scan_date": urls.get("scan_date", ''),
                            "Positives": urls.get("positives", ''),
                            "Total Av Analized": urls.get("total", '')}

            array_url.append(dict_urlres)

            dict_url.update({"RESOURCES": array_url})

            print(Fore.GREEN+Style.BRIGHT+"[URL RESOURCES]--------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_url)
            print(Cursor.DOWN(1))

        except UnboundLocalError:

            print(Fore.RED+Style.BRIGHT+"[NO INFO FOR THIS URL]--------------------------------------------[URL RESOURCES]"+Fore.RESET+Style.RESET_ALL)

        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

def hash_f(apikey, hash):

        params = {'apikey':VIRUS_TOTAL_API_KEY, 'resource':hash}

        url = "https://virustotal.com/vtapi/v2/file/report"

        try:
            
            response = requests.get(url, params=params)

            if response.status_code == 404: 

                print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Hash solicitado"+Fore.RESET+Style.RESET_ALL)
                print(Cursor.DOWN(1))
                print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
                print(Cursor.DOWN(1))
                exit()
            
            hashes = response.json()

        except json.decoder.JSONDecodeError:

            print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado")
            print(Cursor.DOWN(1))

            exit()
        
        dict_hash = {}
       
        array_hash = []
     
        try:

            if "scan_id" in hashes:

                dict_hashres = {"Scan_id": hashes.get("scan_id", ''),
                                "Hash Analizado": hashes.get("resource", ''),
                                "Scan_date": hashes.get("scan_date", ''),
                                "Estado": hashes.get("verbose_msg", ''),
                                "Positives": hashes.get("positives", ''),
                                "Total Av Analized": hashes.get("total", ''),
                                "Hash_sha1": hashes.get("sha1", ''),
                                "Hash_md5": hashes.get("md5", ''),
                                "Hash_sha256": hashes.get("sha256", '')}

            array_hash.append(dict_hashres)

            dict_hash.update({"HASHES": array_hash})

            print(Fore.GREEN+Style.BRIGHT+"[HASH RESOURCES]--------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(array_hash)
            print(Cursor.DOWN(1))
        
        except UnboundLocalError:

            print(Fore.RED+Style.BRIGHT+"[NO INFO FOR THIS HASH]--------------------------------------------[HASH RESOURCES]"+Fore.RESET+Style.RESET_ALL)

        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

            

















    
