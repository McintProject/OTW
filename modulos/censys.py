# -------------------------------------------------------------------------------
# Name:         CensysWrapper.py
# Purpose:      Censys module to obtain information related about an IP, a Domain, or a Certificate
#
# Author:      Jorge I
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------

from collections import defaultdict
import sys
import requests
import json
import re
import os
from colorama import *

from modulos.config import UID, SECRET

def cip_f(apikei, ip):
    
    ipp = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

    if ipp.search(ip): 

        print(Fore.GREEN+"IP introducida correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"La IP introducida no es válida. Lanze de nuevo el Programa e introduzca de nuevo la IP"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()
    
    API_URL = "https://censys.io/api/v1/view/ipv4/"

    response = requests.get(API_URL + str(ip), auth=(UID, SECRET))

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la IP solicitada"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 403:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_censys = {}
   
    array_location = []
    
    
    try:

        for location in respuesta["location"]:
    
            if (location != None):
    
                dict_location = {"country": None, "country_code": None, "registered_country": None}
    
                dict_location.update({"country": respuesta["location"]["country"]})
    
            if (location != None):
    
                dict_location.update({"country_code": respuesta["location"]["country_code"]})
    
            if (location != None):
    
                dict_location.update({"registered_country": respuesta["location"]["registered_country"]})
    
        array_location.append(dict_location)
    
    
        dict_censys.update({"location": array_location})
    
    except KeyError:
    
        pass
    
    array_autonomous_system = []
    
    try:
    
        for autonomous_system in respuesta["autonomous_system"]:
    
            if (autonomous_system != None):
    
                dict_autonomous_system = {}
    
                dict_autonomous_system.update({"description": respuesta["autonomous_system"]["description"]})
    
            if (autonomous_system != None):
    
                dict_autonomous_system.update({"routed_prefix": respuesta["autonomous_system"]["routed_prefix"]})
    
            if (autonomous_system != None):
    
                dict_autonomous_system.update({"country_code": respuesta["autonomous_system"]["country_code"]})
    
            if (autonomous_system != None):
    
                dict_autonomous_system.update({"asn": respuesta["autonomous_system"]["asn"]})
    
        array_autonomous_system.append(dict_autonomous_system)
    
        dict_censys.update({"AS": array_autonomous_system})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_metadata = []
      
    try:
    
        for metadata in respuesta["metadata"]:
    
            if (metadata != None):
    
                dict_metadata = {"os": None}
    
                dict_metadata.update({"os": respuesta["metadata"]["os"]})

        array_metadata.append(dict_metadata)
     
        dict_censys.update({"metadata": array_metadata})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    try:
    
        array_protocols = []
 
        for protocols in respuesta["protocols"]:
    
            if (protocols != None):
    
                dict_protocols = {}
    
                dict_protocols.update({"protocols": respuesta["protocols"]})

        array_protocols.append(dict_protocols)
    
        dict_censys.update({"protocols": array_protocols})
    
    except (KeyError, UnboundLocalError):
    
        pass
  
    array_ftp = []
    
    try:
    
        for puerto in respuesta['ports']:
    
            if respuesta[str(puerto)].get('ftp') != None:
    
                dict_ftp = {"banner": respuesta["21"]["ftp"]["banner"].get("banner", ''),
    
                            "product": respuesta["21"]["ftp"]["banner"]["metadata"].get("product", '')}


        array_ftp.append(dict_ftp)
    
        dict_censys.update({"ftp": array_ftp})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_postgres = []
    
    try:
    
        for puerto in respuesta['ports']:
    
            if respuesta[str(puerto)].get('postgres') != None:
    
                dict_postgres = {"issuer_dn": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"].get("issuer_dn", ''),
    
                                 "fingerprint_sha256": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", ''),
    
                                 "validity": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"]["validity"].get("end", '')}

        array_postgres.append(dict_postgres)
    
        dict_censys.update({"postgres": array_postgres})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_https = []

    try:
    
        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('https') != None:

                dict_https = {"product": respuesta["443"]["https"]["get"]["metadata"].get("product", ''),
    
                              "fingerprint_sha256": respuesta["443"]["https"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", ''),
    
                              "validity": respuesta["443"]["https"]["tls"]["certificate"]["parsed"]["validity"].get("end", '')}
    
    
        array_https.append(dict_https)
    
        dict_censys.update({"https": array_https})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_ssh = []

    try:

        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('ssh') != None:
    
                dict_ssh = {"comment": respuesta["22"]["ssh"]["v2"]["banner"].get("comment", ''),
    
                            "raw": respuesta["22"]["ssh"]["v2"]["banner"].get("raw", ''),
    
                            "software": respuesta["22"]["ssh"]["v2"]["banner"].get("software", ''),
    
                            "version": respuesta["22"]["ssh"]["v2"]["banner"].get("version", '')}

        array_ssh.append(dict_ssh)
    
        dict_censys.update({"ssh": array_ssh})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_http = []
    
    try:
    
        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('http') != None:
    
                dict_http = {"server": respuesta["80"]["http"]["get"]["headers"].get("server", ''),
    
                             "status_line": respuesta["80"]["http"]["get"].get("status_line", ''),
    
                             "title": respuesta["80"]["http"]["get"].get("title", '')}
    
        array_http.append(dict_http)
    
        dict_censys.update({"http": array_http})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_http2 = []
    
    try:
    
        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('http') != None:
    
                dict_http2 = {"server": respuesta["8080"]["http"]["get"]["headers"].get("server", ''),
    
                              "status_line": respuesta["8080"]["http"]["get"].get("status_line", '')}
    
        array_http2.append(dict_http2)
    
        dict_censys.update({"http1": array_http2})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_smtp = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('smtp') != None: 
    
                dict_smtp = {"banner": respuesta["25"]["smtp"]["starttls"].get("banner", ''),
    
                             "fingerprint_sha256": respuesta["25"]["smtp"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_smtp.append(dict_smtp)
    
        dict_censys.update({"smtp": array_smtp})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_smb = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('smb') != None:
    
                dict_smb = {"version": respuesta["445"]["smb"]["banner"]["metadata"].get("version", '')}
    
        array_smb.append(dict_smb)

        dict_censys.update({"smb": array_smb})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_mssql = []
    
    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('mssql') != None:
    
                dict_mssql = {"encrypt_mode": respuesta["1433"]["mssql"]["banner"].get("encrypt_mode", ''),
    
                              "version": respuesta["1433"]["mssql"]["banner"].get("version", ''),
    
                              "fingerprint_sha256": respuesta["1433"]["mssql"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}
  
        array_mssql.append(dict_mssql)
    
        dict_censys.update({"mssql": array_mssql})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_mysql = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('mysql') != None:

                dict_mysql = {"server_version": respuesta["3306"]["mysql"]["banner"].get("server_version", ''),
    
                              "protocol_version": respuesta["3306"]["mysql"]["banner"].get("protocol_version", ''),
    
                              "fingerprint_sha256": respuesta["3306"]["mysql"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}
    
        array_mysql.append(dict_mysql)
    
        dict_censys.update({"mysql": array_mysql})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_pop3 = []

    try:

        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('pop3') != None:

                dict_pop3 = {"banner": respuesta["110"]["pop3"]["starttls"].get("banner", ''),
    
                             "description": respuesta["110"]["pop3"]["starttls"]["metadata"].get("description", ''),
    
                             "fingerprint_sha256": respuesta["110"]["pop3"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}
    
        array_pop3.append(dict_pop3)
    
        dict_censys.update({"pop": array_pop3})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_imap = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('imap') != None:

                dict_imap = {"banner": respuesta["143"]["imap"]["starttls"].get("banner", ''),
    
                             "description": respuesta["143"]["imap"]["starttls"]["metadata"].get("description", ''),
    
                             "fingerprint_sha256": respuesta["143"]["imap"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}
    
        array_imap.append(dict_imap)
    
        dict_censys.update({"imap": array_imap})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_rdp = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('rdp') != None:
    
                dict_rdp = {"description": respuesta["3389"]["rdp"]["banner"]["metadata"].get("description", ''),
    
                            "version": respuesta["3389"]["rdp"]["banner"]["metadata"].get("version", '')}
    
        array_rdp.append(dict_rdp)
    
        dict_censys.update({"rdp": array_rdp})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    if (array_location) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[LOCATION]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_location)
    
            print(Cursor.DOWN(1))
    
    if (array_autonomous_system) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[AUT. SYSTEM]--------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_autonomous_system)
    
            print(Cursor.DOWN(1))
    
    if (array_metadata) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[METADATA]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_metadata)
    
            print(Cursor.DOWN(1))
    
    if (array_protocols) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[PROTOCOLS]----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_protocols)
    
            print(Cursor.DOWN(1))
    
    if (array_ftp) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[FTP]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_ftp)
    
            print(Cursor.DOWN(1))
    
    if (array_postgres) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[POSTGRES]---------------------------------------------------------------- [STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_postgres)
    
            print(Cursor.DOWN(1))
    
    if (array_https) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[HTTPS]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_https)
    
            print(Cursor.DOWN(1))
    
    if (array_ssh) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[SSH]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_ssh)
    
            print(Cursor.DOWN(1))
    
    if (array_http) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[HTTP]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_http)
    
            print(Cursor.DOWN(1))
    
    if (array_http2) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[HTTP2]-------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_http2)
    
            print(Cursor.DOWN(1))
    
    if (array_smtp) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[SMTP]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_smtp)
    
            print(Cursor.DOWN(1))
    
    if (array_smb) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[SMB]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_smb)
    
            print(Cursor.DOWN(1))
    
    if (array_mssql) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[MSSQL]-------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_mssql)
    
            print(Cursor.DOWN(1))
    
    if (array_mysql) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[MYSQL]-------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_mysql)
    
            print(Cursor.DOWN(1))
    
    if (array_pop3) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[POP3]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_pop3)
    
            print(Cursor.DOWN(1))
    
    if (array_imap) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[IMAP]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_imap)
    
            print(Cursor.DOWN(1))
    
    if (array_rdp) != []:
    
            print(Fore.GREEN+Style.BRIGHT+"[RDP]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
            print() 
    
            print(array_rdp)
    
            print(Cursor.DOWN(1))  

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def cdm_f(apikei, domain):

    dom = re.compile(r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6}$')

    if dom.search(domain): 

        print(Fore.GREEN+"Nombre de Dominio introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El nombre de Dominio introducido no es válido. Lanze de nuevo el Programa e introdúzcalo de nuevo"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    API_URL = "https://censys.io/api/v1/view/websites/"

    response = requests.get(API_URL + str(domain), auth=(UID, SECRET))

    if response.status_code == 404: 

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Dominio solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 403:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_censysdm = {}

    array_general = []

    try:
        
        if "domain" != None:

            dict_general = {}

            dict_general.update({"domain": respuesta["domain"]})

    except KeyError:

        pass

    try:
    
        if "alexa_rank" != None:

            dict_general.update({"alexa_rank": respuesta["alexa_rank"]})

    except KeyError:

        pass

    try:

        if "updated_at" != None:

            dict_general.update({"updated_at": respuesta["updated_at"]})

    except KeyError:

        pass

    array_general.append(dict_general)
    
    dict_censysdm.update({"General": array_general})
    
    array_protocolsdm = []
    
    try:

        for protocols in respuesta["protocols"]:
    
            if (protocols[0] != None):
    
                dict_protocolsdm = {}
    
                dict_protocolsdm.update({"protocols": respuesta["protocols"]})

        array_protocolsdm.append(dict_protocolsdm)
    
        dict_censysdm.update({"protocols": array_protocolsdm})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_metadatadm = []
    
    try:
    
        for metadata in respuesta["metadata"]:
    
            if (metadata[0] != None):
    
                dict_metadatadm = {"os": respuesta["metadata"].get("os", '')}
 
        array_metadatadm.append(dict_metadatadm)
    
        dict_censysdm.update({"metadata": array_metadatadm})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_ftp = []
    
    try:

        for puerto in respuesta['ports']:
    
            if respuesta[str(puerto)].get('ftp') != None:
    
                dict_ftp = {"banner": respuesta["21"]["ftp"]["banner"].get("banner", ''),
    
                            "product": respuesta["21"]["ftp"]["banner"]["metadata"].get("product", '')}

        array_ftp.append(dict_ftp)
   
        dict_censysdm.update({"ftp": array_ftp})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_postgres = []

    try:

        for puerto in respuesta['ports']:
    
            if respuesta[str(puerto)].get('postgres') != None:

                dict_postgres = {"issuer_dn": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"].get("issuer_dn", ''),
    
                                 "fingerprint_sha256": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", ''),
    
                                 "validity": respuesta["5432"]["postgres"]["banner"]["tls"]["certificate"]["parsed"]["validity"].get("end", '')}
  
        array_postgres.append(dict_postgres)

        dict_censysdm.update({"postgres": array_postgres})
    
    except (KeyError, UnboundLocalError):
    
        pass
   
    array_https = []

    try:
    
        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('https') != None:

                dict_https = {"fingerprint_sha256": respuesta["443"]["https"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", ''),
    
                              "validity": respuesta["443"]["https"]["tls"]["certificate"]["parsed"]["validity"].get("end", '')}

        array_https.append(dict_https)
 
        dict_censysdm.update({"https": array_https})
    
    except (KeyError, UnboundLocalError):
    
        pass
   
    array_ssh = []
    
    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('ssh') != None:

                dict_ssh = {"comment": respuesta["22"]["ssh"]["v2"]["banner"].get("comment", ''),
    
                            "raw": respuesta["22"]["ssh"]["v2"]["banner"].get("raw", ''),
    
                            "software": respuesta["22"]["ssh"]["v2"]["banner"].get("software", ''),
    
                            "version": respuesta["22"]["ssh"]["v2"]["banner"].get("version", '')}

        array_ssh.append(dict_ssh)
   
        dict_censysdm.update({"ssh": array_ssh})
    
    except (KeyError, UnboundLocalError):
    
        pass
  
    array_http = []
    
    try:
    
        for puerto in respuesta["ports"]:

            if respuesta[str(puerto)].get('http') != None:

                dict_http = {}
    
                dict_http.update({"status_line": respuesta["80"]["http"]["get"]["status_line"]})

            try:

                if respuesta[str(puerto)].get('http_www') != None:
    
                    dict_http.update({"title": respuesta["80"]["http"]["get"]["title"]})
    
            except KeyError:
    
                pass

            try:

                if respuesta[str(puerto)].get('http') != None:
    
                    dict_http.update({"description": respuesta["80"]["http"]["get"]["metadata"]["description"]})
    
            except KeyError:
    
                pass
    
            try:
    
                if respuesta[str(puerto)].get('http_www') != None:
    
                    dict_http.update({"server": respuesta["80"]["http"]["get"]["headers"]["server"]})
    
            except KeyError:
    
                pass
    
        array_http.append(dict_http)
    
        dict_censysdm.update({"http": array_http})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_http2 = []
    
    try:
    
        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('http') != None:

                dict_http2 = {"server": respuesta["8080"]["http"]["get"]["headers"].get("server", ''),
    
                              "status_line": respuesta["8080"]["http"]["get"].get("status_line", '')}

        array_http2.append(dict_http2)
 
        dict_censysdm.update({"http2": array_http2})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_smtp = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('smtp') != None:

                dict_smtp = {"banner": respuesta["25"]["smtp"]["starttls"].get("banner", ''),
    
                             "fingerprint_sha256": respuesta["25"]["smtp"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_smtp.append(dict_smtp)
    
        dict_censysdm.update({"smtp": array_smtp})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_smb = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('smb') != None:

                dict_smb = {"version": respuesta["445"]["smb"]["banner"]["metadata"].get("version", '')}

        array_smb.append(dict_smb)

        dict_censysdm.update({"smb": array_smb})
    
    except (KeyError, UnboundLocalError):
    
        pass
 
    array_mssql = []
 
    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('mssql') != None:

                dict_mssql = {"encrypt_mode": respuesta["1433"]["mssql"]["banner"].get("encrypt_mode", ''),
    
                              "version": respuesta["1433"]["mssql"]["banner"].get("version", ''),
    
                              "fingerprint_sha256": respuesta["1433"]["mssql"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_mssql.append(dict_mssql)

        dict_censysdm.update({"mssql": array_mssql})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_mysql = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('mysql') != None:

                dict_mysql = {"server_version": respuesta["3306"]["mysql"]["banner"].get("server_version", ''),
    
                              "protocol_version": respuesta["3306"]["mysql"]["banner"].get("protocol_version", ''),
    
                              "fingerprint_sha256": respuesta["3306"]["mysql"]["banner"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_mysql.append(dict_mysql)

        dict_censysdm.update({"mysql": array_mysql})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    array_pop3 = []

    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('pop3') != None:

                dict_pop3 = {"banner": respuesta["110"]["pop3"]["starttls"].get("banner", ''),
    
                              "description": respuesta["110"]["pop3"]["starttls"]["metadata"].get("description", ''),
    
                              "fingerprint_sha256": respuesta["110"]["pop3"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_pop3.append(dict_pop3)

        dict_censysdm.update({"pop": array_pop3})
    
    except (KeyError, UnboundLocalError):
    
        pass

    array_imap = []

    try:
 
        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('imap') != None:

                dict_imap = {"banner": respuesta["143"]["imap"]["starttls"].get("banner", ''),
    
                             "description": respuesta["143"]["imap"]["starttls"]["metadata"].get("description", ''),
    
                             "fingerprint_sha256": respuesta["143"]["imap"]["starttls"]["tls"]["certificate"]["parsed"].get("fingerprint_sha256", '')}

        array_imap.append(dict_imap)

        dict_censysdm.update({"imap": array_imap})
    
    except (KeyError, UnboundLocalError):
    
        pass
 
    array_rdp = []
 
    try:

        for puerto in respuesta["ports"]:
    
            if respuesta[str(puerto)].get('rdp') != None:

                dict_rdp = {"description": respuesta["3389"]["rdp"]["banner"]["metadata"].get("description", ''),
    
                            "version": respuesta["3389"]["rdp"]["banner"]["metadata"].get("version", '')}

        array_rdp.append(dict_rdp)

        dict_censysdm.update({"rdp": array_rdp})
    
    except (KeyError, UnboundLocalError):
    
        pass
    
    if (array_general) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[GENERAL]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_general)
    
        print(Cursor.DOWN(1))
    
    if (array_protocolsdm) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[PROTOCOLS]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_protocolsdm)
    
        print(Cursor.DOWN(1)) 
    
    if (array_metadatadm) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[METADATA]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_metadatadm)
    
        print(Cursor.DOWN(1))
    
    if (array_ftp) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[FTP]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_ftp)
    
        print(Cursor.DOWN(1))
    
    if (array_postgres) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[POSTGRES]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_postgres)
    
        print(Cursor.DOWN(1))
    
    if (array_https) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[HTTPS]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_https)
    
        print(Cursor.DOWN(1))
    
    if (array_ssh) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[SSH]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_ssh)
    
        print(Cursor.DOWN(1))
    
    if (array_http) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[HTTP]-------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_http)
    
        print(Cursor.DOWN(1))
    
    if (array_http2) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[HTTP2]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_http2)
    
        print(Cursor.DOWN(1))
    
    if (array_smtp) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[SMTP]-------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_smtp)
    
        print(Cursor.DOWN(1))
    
    if (array_smb) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[SMB]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_smb)
    
        print(Cursor.DOWN(1))
    
    if (array_mssql) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[MSSQL]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_mssql)
    
        print(Cursor.DOWN(1))
    
    if (array_mysql) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[MYSQL]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_mysql)
    
        print(Cursor.DOWN(1))
    
    if (array_pop3) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[POP3]-------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_pop3)
    
        print(Cursor.DOWN(1))
    
    if (array_imap) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[IMAP]-------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_imap)
    
        print(Cursor.DOWN(1))
    
    if (array_rdp) != []:
    
        print(Fore.GREEN+Style.BRIGHT+"[RDP]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
    
        print() 
    
        print(array_rdp)
    
        print(Cursor.DOWN(1))  

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def ct_f(apikei, ct):
    
    ctp = re.compile(r'[A-Fa-f0-9]{64}')

    if ctp.search(ct): 

        print(Fore.GREEN+"Hash introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Hash introducido no es válido. Lanze de nuevo el Programa e introduzca un Hash en sha256"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    API_URL = "https://censys.io/api/v1/view/certificates/"

    response = requests.get(API_URL + str(ct), auth=(UID, SECRET))

    if response.status_code == 404:

        print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para el Certificado solicitado"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    if response.status_code == 403:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+Style.BRIGHT+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    respuesta = response.json()

    dict_ct = {}

    array_parsed = []

    try:
    
        for  parsed in respuesta["parsed"]:
                
            if (parsed[0] != None):

                    dict_parsed = {"organizational_unit": respuesta["parsed"]["subject"].get("organizational_unit", ''),
                                   "issuer_dn": respuesta["parsed"].get("issuer_dn", ''),
                                   "serial_number": respuesta["parsed"].get("serial_number", ''),
                                   "fingerprint_sha256": respuesta["parsed"].get("fingerprint_sha256", ''),
                                   "fingerprint_sha1": respuesta["parsed"].get("fingerprint_sha1", ''),
                                   "fingerprint_md5": respuesta["parsed"].get("fingerprint_md5", ''),
                                   "names": respuesta["parsed"].get("names", '')}

        array_parsed.append(dict_parsed)
 
        dict_ct.update({"parsed": array_parsed})

    except (KeyError, UnboundLocalError):
            pass

    array_sign = []

    try:
        
        for  subject_key_info in respuesta["parsed"]:

            if (parsed[0] != None):

                dict_sign = {"name": respuesta["parsed"]["subject_key_info"]["key_algorithm"].get("name", ''),
                            "length": respuesta["parsed"]["subject_key_info"].get("rsa_public_key", ''),
                            "name": respuesta["parsed"]["signature"]["signature_algorithm"].get("name", ''),
                            "oid": respuesta["parsed"]["signature"]["signature_algorithm"].get("oid")}

        array_sign.append(dict_sign)

        dict_ct.update({"Keys": array_sign})

    except UnboundLocalError:

        pass

    array_val = []

    try:

        for  validity in respuesta["parsed"]:

            if (parsed[0] != None):


                dict_val = {"start": respuesta["parsed"]["validity"].get("start", ''),
                            "end": respuesta["parsed"]["validity"].get("end", '')}

        array_val.append(dict_val)

        dict_ct.update({"Validity": array_val})

    except (KeyError, UnboundLocalError):

        pass

    if (array_parsed) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_parsed)
        print(Cursor.DOWN(1))

    if (array_sign) != []:

        print(Fore.GREEN+Style.BRIGHT+"[PUBLIC KEYS]------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_sign)
        print(Cursor.DOWN(1))

    if (array_val) != []:

        print(Fore.GREEN+Style.BRIGHT+"[VALIDITY]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_val)
        print(Cursor.DOWN(1))  

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))