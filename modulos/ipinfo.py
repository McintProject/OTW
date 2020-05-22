# -------------------------------------------------------------------------------
# Name:        ipinfo.py
# Purpose:     Módulo ipinfo proporciona información relacionada con la 
#              localización de la dirección IP
#            
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests


def analyze(api_key, ip):
      
    r = requests.get("https://ipinfo.io/" + ip + "?token="+ api_key)

    try:
        return r.json()
    except Exception:
        return {"error":"Error en Ipinfo"}
   
