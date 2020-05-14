# -------------------------------------------------------------------------------
# Name:         ClearbitWrapper.py
# Purpose:      Clearbit module to obtain information from People & Companies, based on an Email or a Domain 
#
# Author:      Jorge Iturria
# Contact:     pyproject@protonmail.com 
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------
from collections import defaultdict
import clearbit
import requests
import json
from colorama import *
import os
import re

from modulos.config import CLEARBIT_API_KEY

def clemail_f(apikey, email):
    
    if '@' in email:

        print(Fore.GREEN+"Email introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Email introducido no es correcto. Lanze de nuevo el Programa e introduzca de nuevo el Email"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()

    clearbit.key = CLEARBIT_API_KEY

    try:
        
        lookup = clearbit.Enrichment.find(email=email, stream=True)

    except requests.exceptions.HTTPError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    dict_principal = {}
 
    try:
        
        for person in lookup["person"]:

            if "name" != None:

                array_general = []
            
                dict_gen =  {"id" : lookup["person"].get("id", ''),
                             "fullName" : lookup["person"]["name"].get("fullName", ''),
                             "email" : lookup["person"].get("email", ''),
                             "location" : lookup["person"].get("location", ''),
                             "timeZone" : lookup["person"].get("timeZone", '')}

        array_general.append(dict_gen)

        dict_principal.update({"General": array_general})

    except TypeError:

        print(Fore.RED+"El Email introducido no se encuentra en nuestra Base de Datos"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for geo in lookup["person"]:

            if 'geo' != None:

                array_geo = []

                dict_geo = {"city": lookup["person"]["geo"].get("city", ''),
                            "state": lookup["person"]["geo"].get("state", ''),
                            "country": lookup["person"]["geo"].get("country", '')}

        array_geo.append(dict_geo)

        dict_principal.update({"Geo": array_geo})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for employment in lookup["person"]:

            if 'employment' != None:

                array_employment = []

                dict_employment = {"title": lookup["person"]["employment"].get("title", ''),
                                  "role": lookup["person"]["employment"].get("role", ''),
                                  "company": lookup["person"]["employment"].get("name", ''),
                                  "domain": lookup["person"]["employment"].get("domain", '')}

        if dict_employment["company"] != None:
        
            array_employment.append(dict_employment)

        dict_principal.update({"Empleo": array_employment})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for linkedin in lookup["person"]:

            if "handle" != None:

                array_linkedin = []

                dict_linkedin = {"Linkedin": lookup["person"]["linkedin"].get("handle", '')}

        if dict_linkedin["Linkedin"] != None:

            array_linkedin.append(dict_linkedin)

        dict_principal.update({"Linkedin": array_linkedin})

    except (KeyError, UnboundLocalError):

        pass

    try:

        for facebook in lookup["person"]:

            if 'handle' != None:

                array_facebook = []

                dict_facebook = {"Facebook": lookup["person"]["facebook"].get("handle", '')}
        
        if dict_facebook["Facebook"] != None:
        
            array_facebook.append(dict_facebook)
        

        dict_principal.update({"Facebook": array_facebook})

    except (KeyError, UnboundLocalError):

        pass

    try:
            
        for github in lookup["person"]:

            if "handle" != None:

                array_github = []

                dict_github = {"Github": lookup["person"]["github"].get("handle", '')}

        if dict_github["Github"] != None:

            array_github.append(dict_github)

        dict_principal.update({"Github": array_github})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for twitter in lookup["person"]:

            if 'handle' != None:

                array_twitter = []

                dict_twitter = {"Twitter": lookup["person"]["twitter"].get("handle", ''),
                                "id": lookup["person"]["twitter"].get("id", ''),
                                "bio": lookup["person"]["twitter"].get("bio", ''),
                                "followers": lookup["person"]["twitter"].get("followers", ''),
                                "following": lookup["person"]["twitter"].get("following", ''),
                                "location": lookup["person"]["twitter"].get("location", ''),
                                "site": lookup["person"]["twitter"].get("site", '')}

        if dict_twitter["Twitter"] != None:

            array_twitter.append(dict_twitter)

        dict_principal.update({"Twitter": array_twitter})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for gravatar in lookup["person"]:
    
            if 'handle' != None:

                array_gravatar = []

                dict_gravatar = {"Gravatar": lookup["person"]["gravatar"].get("handle", '')}

        if dict_gravatar["Gravatar"] != None:

            array_gravatar.append(dict_gravatar)

        dict_principal.update({"Gravatar": array_gravatar})

    except (KeyError, UnboundLocalError):

        pass

    if (array_general) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_general)
        print(Cursor.DOWN(1))

    if (array_geo) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GEO INFO]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_geo)
        print(Cursor.DOWN(1))

    if (array_employment) != []:

        print(Fore.GREEN+Style.BRIGHT+"[EMPLOYMENT]-------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_employment)
        print(Cursor.DOWN(1))

    if (array_linkedin) != []:

        print(Fore.GREEN+Style.BRIGHT+"[LINKEDIN]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_linkedin)
        print(Cursor.DOWN(1))

    if (array_facebook) != []:

        print(Fore.GREEN+Style.BRIGHT+"[FACEBOOK]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_facebook)
        print(Cursor.DOWN(1))

    if (array_github) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GITHUB]-----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_github)
        print(Cursor.DOWN(1)) 

    if (array_twitter) != []:

        print(Fore.GREEN+Style.BRIGHT+"[TWITTER]----------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_twitter)
        print(Cursor.DOWN(1))

    if (array_gravatar) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GRAVATAR]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_gravatar)
        print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def cldomain_f(apikey, dominio):

    dom = re.compile(r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6}$')

    if dom.search(dominio): 

        print(Fore.GREEN+"Nombre de Dominio introducido correctamente"+Fore.RESET)
        print(Cursor.DOWN(1))

    else:

        print(Fore.RED+"El Nombre de Dominio introducido no es válido. Lanze de nuevo el Programa e introdúzcalo de nuevo"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    try:
        
        clearbit.key = CLEARBIT_API_KEY

        lookup = clearbit.Enrichment.find(domain=dominio, stream=True)

    except requests.exceptions.HTTPError:

        print(Fore.RED+"Api_key del Servicio inválida o no introducida. Revise el archivo config.py del Módulo"+ Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

        exit()

    dict_domains = {}

    try:
        array_info = []

        dict_info = {}
        if (lookup["id"] != None):
            dict_info.update({"Id" : lookup["id"]})
        if (lookup["name"] != None):
            dict_info.update({"Name" : lookup["name"]})
        if (lookup["legalName"] != None):
            dict_info.update({"LegalName" : lookup["legalName"]})
        if (lookup["domain"] != None):
            dict_info.update({"Domain" : lookup["domain"]})
        if (lookup["description"] != None):
            dict_info.update({"Description" : lookup["description"]})
        if (lookup["foundedYear"] != None):
            dict_info.update({"FoundedYear" : lookup["foundedYear"]})
        if (lookup["location"] != None):
            dict_info.update({"Location" : lookup["location"]})
        if (lookup["phone"] != None):
            dict_info.update({"Phone" : lookup["phone"]})

        array_info.append(dict_info)

        dict_domains.update({"Info": array_info})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for category in lookup["category"]:

            if "category" != 0:

                array_category = []

                dict_category = {"sector": lookup["category"].get("sector", ''),
                                 "industry": lookup["category"].get("industry", '')}

        if dict_category["sector"] != None:
        
            array_category.append(dict_category)
    
        dict_domains.update({"Category": array_category})

    except requests.exceptions.HTTPError:

        pass

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for site in lookup["site"]:

            if "site" != 0:

                array_site = []

                dict_site = {"phoneNumbers": lookup["site"].get("phoneNumbers", ''),
                             "emailAddresses": lookup["site"].get("emailAddresses", '')}

        if dict_site["phoneNumbers"] != []:

            array_site.append(dict_site)


        dict_domains.update({"Contacto": array_site})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for metrics in lookup["metrics"]:

            if "metrics" != None:

                array_metrics = []

            dict_metrics = {"employees" : lookup["metrics"].get("employees", ''),
                            "estimatedAnnualRevenue" : lookup["metrics"].get("estimatedAnnualRevenue", '')}

        if dict_metrics["employees"] != None:

            array_metrics.append(dict_metrics)
    
        dict_domains.update({"Metricas": array_metrics})

    except (KeyError, UnboundLocalError):

        pass

    try: 
        
        for facebook in lookup["facebook"]:

            if "facebook" != None:

                array_facebook = []

                dict_facebook = {"facebook" : lookup["facebook"].get("handle", ''),
                                 "likes" : lookup["facebook"].get("likes", '')}

        if dict_facebook["facebook"] != None:
        
            array_facebook.append(dict_facebook)

        dict_domains.update({"Facebook": array_facebook})

    except (KeyError, UnboundLocalError):

        pass

    try:
        
        for twitter in lookup["twitter"]:

            if "twitter" != None:

                array_twitter = []

                dict_twitter = dict_twitter = {"Twitter" : lookup["twitter"].get("handle", ''),
                                               "id" : lookup["twitter"].get("id", ''),
                                               "bio" : lookup["twitter"].get("bio", ''),
                                               "followers" : lookup["twitter"].get("followers", ''),
                                               "following" : lookup["twitter"].get("following", ''),
                                               "location" : lookup["twitter"].get("location", ''),
                                               "site" : lookup["twitter"].get("site", '')}

        if dict_twitter["Twitter"] != None:

            array_twitter.append(dict_twitter)


        dict_domains.update({"Twitter": array_twitter})

    except (KeyError, UnboundLocalError):
        pass

    try: 

        for linkedin in lookup["linkedin"]:

            if "linkedin" != None:

                array_linkedin = []

                dict_linkedin = {"Linkedin" : lookup["linkedin"].get("handle", '')}

        if dict_linkedin["Linkedin"] != None:

            array_linkedin.append(dict_linkedin)

        dict_domains.update({"Linkedin": array_linkedin})

    except (KeyError, UnboundLocalError):

        pass
    try: 
        
        if (array_info) != []:

            print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_info)
            print(Cursor.DOWN(1))

        if (array_category) != []:

            print(Fore.GREEN+Style.BRIGHT+"[CATEGORY]----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_category)
            print(Cursor.DOWN(1))

        if (array_site) != []:

            print(Fore.GREEN+Style.BRIGHT+"[CONTACT]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_site)
            print(Cursor.DOWN(1))

        if (array_metrics) != []:

            print(Fore.GREEN+Style.BRIGHT+"[METRICS]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_metrics)
            print(Cursor.DOWN(1))

        if (array_facebook) != []:

            print(Fore.GREEN+Style.BRIGHT+"[FACEBOOK]----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_facebook)
            print(Cursor.DOWN(1))

        if (array_twitter) != []:

            print(Fore.GREEN+Style.BRIGHT+"[TWITTER]-----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_twitter)
            print(Cursor.DOWN(1))

        if (array_linkedin) != []:

            print(Fore.GREEN+Style.BRIGHT+"[LINKEDIN]----------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print() 
            print(array_linkedin)
            print(Cursor.DOWN(1))

    except (requests.exceptions.HTTPError, UnboundLocalError):

        print(Fore.RED+"El Nombre de Dominio introducido no se encuentra en nuestra BBDD"+Fore.RESET)   
        print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))







