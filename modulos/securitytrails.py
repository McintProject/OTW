# -------------------------------------------------------------------------------
# Name:        securitytrails.py
# Purpose:     Módulo Securitytrals SecurityTrails enables you to explore complete
#              current and historical data for any internet assets. It's DNS, IP, 
#              domain, SSL and open ports intelligence made ... The free version only
#              include domain and subdomain information
#
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests

def domain(api_key, domain):
    parametros = {
        'apikey': api_key
    }
    r = requests.get("https://api.securitytrails.com/v1/domain/" + domain,  params=parametros)

    try:
        return r.json()
    except Exception:
        return {"error":"Error en SecurityTrails"}

def subdomain(api_key, domain):
    parametros = {
        'apikey': api_key
    }
    r = requests.get("https://api.securitytrails.com/v1/domain/" + domain + "/subdomains",  params=parametros)

    try:
        return r.json()
    except Exception:
        return {"error":"Error en SecurityTrails"}

