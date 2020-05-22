# -------------------------------------------------------------------------------
# Name:        alienvault.py
# Purpose:     Consultar la reputación de una dirección ip o dominio 
#                             
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests, json, sys
import urllib.request


def ip(api_key, ip):
    
    header={'X-OTX-API-KEY':api_key}
    print("\nALIENVAULT ------------------------------------------\n")
    print("\n-- GENERAL ----------------- ")

    try:
       general = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/general', headers=header)
       print(json.dumps(general.json(),indent=2))
       malware = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/malware', headers=header)
       malware_list = malware.json()
       if "count" in malware_list:
          print("\n-- MALWARE ----------------- ")
          print(json.dumps(malware.json(),indent=2))

       url_list = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/url_list', headers=header)
       urls = url_list.json()
       if urls["actual_size"]!=0:
          print("\n-- URL LIST ------------ ")
          print(json.dumps(url_list.json(),indent=2))

       passive_dns = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/passive_dns', headers=header)
       print("\n-- PASSIVE DNS -------------- ")
       print(json.dumps(passive_dns.json(),indent=2))

       http_scans = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/http_scans', headers=header)
       print("\n-- HTTP SCAN -------------- ")
       print(json.dumps(http_scans.json(),indent=2))

       geo = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/geo', headers=header)
       print("\n-- GEO -------------- ")
       print(json.dumps(geo.json(),indent=2))

       reputation = requests.get('https://otx.alienvault.com:443/api/v1/indicators/IPv4/' + ip + '/reputation', headers=header)
       repu = reputation.json()
       if repu["reputation"] is not None:
         print("\n-- REPUTATION -------------- ")
         print(json.dumps(reputation.json(),indent=2))
    
       return 0
 
    except Exception:
      return {"error":"Error en Hunter"}

   
def domain(api_key, domain):
    
    header={'X-OTX-API-KEY':api_key}
    print("\nALIENVAULT ------------------------------------------\n")
    print("\n-- GENERAL ----------------- ")

    try:
      
      general = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/general', headers=header)
      print(json.dumps(general.json(),indent=2))
    
      malware = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/malware', headers=header)
      malware_list = malware.json()
      if "count" in malware_list:
         print("\n-- MALWARE ----------------- ")
         print(json.dumps(malware.json(),indent=2))
    
      url_list = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/url_list', headers=header)
      urls = url_list.json()
      if urls["actual_size"]!=0:
         print("\n-- URL LIST ------------ ")
         print(json.dumps(url_list.json(),indent=2))

      print("\n-- PASSIVE DNS -------------- ")
      passive_dns = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/passive_dns', headers=header)
      print(json.dumps(passive_dns.json(),indent=2))
    
      print("\nGEO  -------------- ")
      geo = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/geo', headers=header)
      print(json.dumps(geo.json(),indent=2))
    
      who = requests.get('https://otx.alienvault.com:443/api/v1/indicators/domain/' + domain + '/whois', headers=header)
      whois = who.json()
      if whois["count"]!=0:
           print("\n-- WHOIS ------------- ")
           print(json.dumps(who.json(),indent=2))
    
    
      return 0
 
    except Exception:
      return {"error":"Error en Hunter"}


