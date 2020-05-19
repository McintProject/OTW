# -------------------------------------------------------------------------------
# Name:         LibreBormeWrapper.py
# Purpose:      Módulo LibreBorme para la búsqueda de Personas y Empresas
#               inscritas en el Boletín Oficial del Registro Mercantil de España
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
from colorama import *
import os
import re

def search_persons(nombre):

    response = requests.get("https://libreborme.net/borme/api/v1/persona/search/?q=" + nombre.replace(" ", "%20") + "&page=1")

    search = response.json()
    
    dict_names = {}

    array_names = []

    if 'objects' in search:

        for objects in search["objects"]:     
 
            dict_object = {}
                
            if (objects["name"] != None): 

                dict_object.update({"Nombre": objects["name"]})

            array_names.append(dict_object)

            dict_names.update({"NAMES": array_names})

        if dict_names == {}:

            print(Fore.RED+Style.BRIGHT+"No se han obtenido resultados para la búsqueda realizada"+Fore.RESET+Style.RESET_ALL)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
            print(Cursor.DOWN(1))
            exit()

        else:

            try:
                
                if (array_names[0]) != []:

                    print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 1]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                    print() 
                    print(array_names[0])
                    print(Cursor.DOWN(1))   
            
            except IndexError:

                pass

            try:
                
                if (array_names[1]) != []:
                    print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 2]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                    print() 
                    print(array_names[1])
                    print(Cursor.DOWN(1))   
            
            except IndexError:

                pass

            try:
                
                if (array_names[2]) != []:

                    print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 3]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                    print() 
                    print(array_names[2])
                    print(Cursor.DOWN(1))   
            
            except IndexError:

                pass

            try:
                
                if (array_names[3]) != []:
                    print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 4]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                    print() 
                    print(array_names[3])
                    print(Cursor.DOWN(1))   
            
            except IndexError:

                pass

            try:
                
                if (array_names[4]) != []:

                    print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 5]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                    print() 
                    print(array_names[4])
                    print(Cursor.DOWN(1))   
            
            except IndexError:

                pass

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def search_companies(empresa):
       
        response = requests.get("https://libreborme.net/borme/api/v1/empresa/search/?q=" + empresa + "&page=1")

        search_comp = response.json()

        dict_companies = {}

        array_companies = []

        if 'objects' in search_comp:

            for objects in search_comp["objects"]:     

                dict_objectc = {}
                   
                if (objects["name"] != None):

                    dict_objectc.update({"Nombre": objects["name"]})

                array_companies.append(dict_objectc)

                dict_companies.update({"COMPANIES": array_companies})

            if dict_companies == {}:

                print(Fore.RED+Style.BRIGHT+"No se han obtenido resultados para la búsqueda realizada"+Fore.RESET+Style.RESET_ALL)
                print(Cursor.DOWN(1))
                print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
                print(Cursor.DOWN(1))
                exit()

            else: 

                try:
                
                    if (array_companies[0]) != []:
                        print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 1]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                        print() 
                        print(array_companies[0])
                        print(Cursor.DOWN(1))   
            
                except IndexError:

                    pass

                try:
                
                    if (array_companies[1]) != []:

                        print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 2]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                        print() 
                        print(array_companies[1])
                        print(Cursor.DOWN(1))   
            
                except IndexError:

                    pass

                try:
                
                 if (array_companies[2]) != []:

                        print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 3]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                        print() 
                        print(array_companies[2])
                        print(Cursor.DOWN(1))   
            
                except IndexError:

                    pass

                try:
                
                    if (array_companies[3]) != []:
                        print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 4]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                        print() 
                        print(array_companies[3])
                        print(Cursor.DOWN(1))   
            
                except IndexError:

                    pass

                try:
                
                    if (array_companies[4]) != []:

                        print(Fore.GREEN+Style.BRIGHT+"[RESULTADO 5]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                        print() 
                        print(array_companies[4])
                        print(Cursor.DOWN(1))   
            
                except IndexError:

                    pass

        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))

def persons(apellidos, nombre):
    
    response = requests.get("https://libreborme.net/borme/api/v1/persona/" + apellidos.replace(" ", "-") + "-" + nombre.replace(" ", "-") + "/")

    try:

        person = response.json()

    except json.decoder.JSONDecodeError:

        print(Fore.RED+Style.BRIGHT+"No se han obtenido resultados para la búsqueda realizada"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    try:
    
        dict_persons = {}
        
        array_persons_general = []

        if 'date_updated' != None:

            dict_persons_general = {}

            dict_persons_general.update({"LAST_UPDATE": person["date_updated"]})

        array_persons_general.append(dict_persons_general)

        dict_persons.update({"GENERAL INFO": array_persons_general})

        array_cargos_actuales = []

        if 'cargos_actuales' in person:

            for cargos_actuales in person["cargos_actuales"]:

                if (cargos_actuales["name"] != None):

                    dict_cargos = {}

                    dict_cargos.update({"Company_Name": cargos_actuales["name"]})

                if (cargos_actuales["title"] != None):

                    dict_cargos.update({"Company_Title": cargos_actuales["title"]})

                if (cargos_actuales["date_from"] != None):

                    dict_cargos.update({"From": cargos_actuales["date_from"]})

                array_cargos_actuales.append(dict_cargos)

            dict_persons.update({"ACTUAL_POSITIONS": array_cargos_actuales})

        array_cargos_historial = []

        if 'cargos_historial' in person:

            for cargos_historial in person["cargos_historial"]:

                if (cargos_historial["name"] != None):

                    dict_cargos_historial = {}

                    dict_cargos_historial.update({"Company_Name": cargos_historial["name"]})

                if (cargos_historial["title"] != None):

                    dict_cargos_historial.update({"Company_Title": cargos_historial["title"]})

                if (cargos_historial["date_to"] != None):

                    dict_cargos_historial.update({"To": cargos_historial["date_to"]})

                array_cargos_historial.append(dict_cargos_historial)

            if len(array_cargos_historial) != 0:
                dict_persons.update({"HISTORY_POSITIONS": array_cargos_historial})           
        
        if dict_persons != {}:

            if array_persons_general != []:

                print(Fore.GREEN+Style.BRIGHT+"[INFO GENERAL]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                print() 
                print(str(array_persons_general))
                print(Cursor.DOWN(1))
     
            if array_cargos_actuales != []:

                print(Fore.GREEN+Style.BRIGHT+"[CARGOS ACTUALES]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                print() 
                array_cargos_actuales.reverse() 
                print(str(array_cargos_actuales[0:9]))
                print(Cursor.DOWN(1)) 
        
            if array_cargos_historial != []:

                print(Fore.GREEN+Style.BRIGHT+"[CARGOS HISTÓRICOS]---------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
                print() 
                array_cargos_historial.reverse()
                print(str(array_cargos_historial[0:9]))
                print(Cursor.DOWN(1))
        
    except UnboundLocalError:
        pass
    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))

def empresas(empresa):

    response = requests.get("https://libreborme.net/borme/api/v1/empresa/" + empresa.replace(" ", "-") + "/")

    try:
    
        empresa = response.json()

    except json.decoder.JSONDecodeError:

        print(Fore.RED+Style.BRIGHT+"No se han obtenido resultados para la búsqueda realizada"+Fore.RESET+Style.RESET_ALL)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        print(Cursor.DOWN(1))
        exit()

    try:
    
        dict_empresas = {}
     
        array_empresas_general = []

        if 'name' != None:

            dict_empresas_general = {}

            dict_empresas_general.update({"name": empresa["name"]})

        if 'type' != None:

            dict_empresas_general.update({"type": empresa["type"]})

        if 'date_updated' != None:

            dict_empresas_general.update({"date_updated": empresa["date_updated"]})

        array_empresas_general.append(dict_empresas_general)

        dict_empresas.update({"GENERAL INFO": array_empresas_general})
 
        array_cargos_actuales_p = []

        if 'cargos_actuales_p' in empresa:

            for cargos_actuales_p in empresa["cargos_actuales_p"]:

                if (cargos_actuales_p["name"] != None):

                    dict_cargos_p = {}

                    dict_cargos_p.update({"Name": cargos_actuales_p["name"]})

                if (cargos_actuales_p["title"] != None):

                    dict_cargos_p.update({"Position_Title": cargos_actuales_p["title"]})

                if (cargos_actuales_p["date_from"] != None):

                    dict_cargos_p.update({"From": cargos_actuales_p["date_from"]})

                array_cargos_actuales_p.append(dict_cargos_p)

            if len(array_cargos_actuales_p) != 0:
 
                dict_empresas.update({"ACTUAL_POSITIONS": array_cargos_actuales_p})

        array_cargos_historial_p = []

        if 'cargos_historial_p' in empresa:

            for cargos_historial_p in empresa["cargos_historial_p"]:

                if (cargos_historial_p["name"] != None):

                    dict_cargos_historial_p = {}

                    dict_cargos_historial_p.update({"Name": cargos_historial_p["name"]})

                if (cargos_historial_p["title"] != None):

                    dict_cargos_historial_p.update({"Position_Title": cargos_historial_p["title"]})

                if (cargos_historial_p["date_to"] != None):

                    dict_cargos_historial_p.update({"To": cargos_historial_p["date_to"]})

                array_cargos_historial_p.append(dict_cargos_historial_p)

            if len(array_cargos_historial_p) != 0 :

                dict_empresas.update({"HISTORY_POSITIONS": array_cargos_historial_p})    

        array_relatedc1 = []

        if 'cargos_actuales_c' in empresa:

            for cargos_actuales_c in empresa["cargos_actuales_c"]:

                if (cargos_actuales_c["name"] != None):

                    dict_relatedCompanies = {}

                    dict_relatedCompanies.update({"RELATED_COMPANIES": empresa["cargos_actuales_c"][0]["name"]})

            array_relatedc1.append(dict_relatedCompanies)

            if len(array_relatedc1) != 0:

                dict_empresas.update({"RELATED_COMPANIES": array_relatedc1}) 
            
        array_relatedc2 = []

        if 'cargos_historial_c' in empresa:

            for cargos_historial_c in empresa["cargos_historial_c"]:

                if (cargos_historial_c["name"] != None):

                    dict_relatedCompaniesh = {}

                    dict_relatedCompaniesh.update({"HISTORY_RELATED_COMPANIES": empresa["cargos_historial_c"][0]["name"]})

            array_relatedc2.append(dict_relatedCompaniesh)

            if len(array_relatedc2) != 0:

                dict_empresas.update({"RELATEC_COMPANIES": array_relatedc2})

    except UnboundLocalError:

        pass

    if dict_empresas != {}:
              
        if array_empresas_general != []:

            print(Fore.GREEN+Style.BRIGHT+"[INFO GENERAL]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()    
            print(str(array_empresas_general))
            print(Cursor.DOWN(1))
     
        if array_cargos_actuales_p != []:

            print(Fore.GREEN+Style.BRIGHT+"[CARGOS ACTUALES]---------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()  
            array_cargos_actuales_p.reverse() 
            print(str(array_cargos_actuales_p[0:9]))
            print(Cursor.DOWN(1))
        
        if array_cargos_historial_p != []:

            print(Fore.GREEN+Style.BRIGHT+"[CARGOS HISTORICOS]-------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()  
            array_cargos_historial_p.reverse() 
            print(str(array_cargos_historial_p[0:9]))
            print(Cursor.DOWN(1))

        if array_relatedc1 != []:

            print(Fore.GREEN+Style.BRIGHT+"[EMPRESAS RELACIONADAS ACTUALES]------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(str(array_relatedc1))
            print(Cursor.DOWN(1))

        if array_relatedc2 != []:

            print(Fore.GREEN+Style.BRIGHT+"[EMPRESAS RELACIONADAS HISTORICAS]----------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(str(array_relatedc2))
            print(Cursor.DOWN(1))

        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
