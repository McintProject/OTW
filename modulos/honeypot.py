# -------------------------------------------------------------------------------
# Name:        honeypot.py
# Purpose:     Módulo projecthoneypot.org for identifying spammers and the spambots
#              they use to scrape addresses from your website 
#           
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests
import httpbl

def analyze(api_key, ip):
    
    bl = httpbl.HttpBL('api_key')
    response = bl.query(ip)
    
    try:
        print('IP Address: {}'.format(ip))
        print('Threat Score: {}'.format(response['threat_score']))
        print('Days since last activity: {}'.format(response['days_since_last_activity']))
        print('Visitor type: {}'.format(', '.join([httpbl.DESCRIPTIONS[t] for t in response['type']])))
        return response
    except Exception:
        return {"error":"Error en Honeypot Checker"}
    