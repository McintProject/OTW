# -----------------------------------------------------------------------------
# Name:         otw.py
# Purpose:      Trabajo Fin de Master --- Ciberinteligencia ---
#              
# Author:      Jorge I
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Isabel Muñoz & Jorge Iturria
# Licence:     GNU V3
# -----------------------------------------------------------------------------
from modulos import config
from modulos import shodan
from modulos import virustotal
from modulos import censys
from modulos import xforce
from modulos import riskiq
from modulos import fraudguard
from modulos import botscout
from modulos import clifinal
from modulos import dehased
from modulos import blockchain
from modulos import scylla
from modulos import userchecker

from modulos import libreborme

import clearbit
from colorama import *
from collections import defaultdict
from requests.auth import HTTPBasicAuth
import base64
import sys
import os
import re

desc = Fore.CYAN+ """

   ____  _______       __
  / __ \/_  __/ |     / /
 / / / / / /  | | /| / / 
/ /_/ / / /   | |/ |/ /  
\____/ /_/    |__/|__/   Alpha Version
                         
                                                                  
"""+ Fore.RESET

print (desc)

print(Fore.WHITE+'''
--------------------------------------
-----Selecciona el tipo de entrada----
--------------------------------------

1) IP
2) DOMINIO
3) URL
4) CERTIFICADOS
5) HASH (Malware)
6) TRANSACCIÓN / DIRECCIÓN BITCOIN
7) EMAIL
8) PERSONAS Y EMPRESAS
9) NICKS & USERNAMES
'''+Fore.RESET)
print(Cursor.FORWARD(1))

entrada = input(Fore.WHITE+'Seleccione el Input >> '+Fore.RESET)

if entrada == '1':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) SHODAN
B) VIRUS TOTAL
C) CENSYS
D) IBM X-FORCE EXCHANGE
E) RISKIQ
F) FRAUDGUARD
G) BOTSCOUT
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)
    
    if modulo == 'A':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))
        
        resultado_shodan = shodan.ip_f(config.SHODAN_API_KEY, ip)

    elif modulo == 'B':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_virustotal = virustotal.vipm_f(config.VIRUS_TOTAL_API_KEY, ip)

    elif modulo == 'C':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_censys = censys.cip_f(config.auth, ip)

    elif modulo == 'D':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_xforce = xforce.xip_reputacion(config.auth, ip)
        resultado_xforce = xforce.xip_dns(config.auth, ip)
        resultado_xforce = xforce.xip_malware(config.auth, ip)
        resultado_xforce = xforce.xip_whois(config.auth, ip)

    elif modulo == 'E':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_riskiq = riskiq.risk_ipe(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipm(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipo(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipdns(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipuni(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipcert(config.auth, ip)
        resultado_riskiq = riskiq.risk_ipwhois(config.auth, ip)

    elif modulo == 'F':

        target = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_fraudguard = fraudguard.ip_fraud(config.auth, target)

    elif modulo == 'G':

        ip = input('Introduzca la IP >> ')

        print(Cursor.FORWARD(1))

        resultado_botscout = botscout.botip_f(config.BOTSCOUT_API_KEY, ip)
        
    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")


elif entrada == '2':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) VIRUS TOTAL
B) CENSYS
C) IBM X-FORCE EXCHANGE
D) RISKIQ
E) CLEARBIT (Información sobre Empresas)
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        dominio = input('Introduzca el Dominio >> ')

        print(Cursor.FORWARD(1))

        resultado_virustotal = virustotal.vdm_f(config.VIRUS_TOTAL_API_KEY, dominio)

    elif modulo == 'B':

        domain = input('Introduzca el Dominio >> ')

        print(Cursor.FORWARD(1))

        resultado_censys = censys.cdm_f(config.auth, domain)

    elif modulo == 'C':

        domain = input('Introduzca el Dominio >> ')

        print(Cursor.FORWARD(1))

        resultado_xforce = xforce.domain_rep(config.auth, domain)
        resultado_xforce = xforce.domain_whois(config.auth, domain)

    elif modulo == 'D':

        dominio = input('Introduzca el Dominio >> ')

        print(Cursor.FORWARD(1))

        resultado_riskiq = riskiq.risk_dme(config.auth, dominio)
        resultado_riskiq = riskiq.risk_dmm(config.auth, dominio )
        resultado_riskiq = riskiq.risk_dmo(config.auth, dominio )
        resultado_riskiq = riskiq.risk_dms(config.auth, dominio )
        resultado_riskiq = riskiq.risk_dmdns(config.auth, dominio )
        resultado_riskiq = riskiq.risk_dmuni(config.auth, dominio )
        resultado_riskiq = riskiq.risk_dmwhois(config.auth, dominio )

    elif modulo == 'E':

        dominio = input('Introduzca el Dominio >> ')

        print(Cursor.FORWARD(1))

        resultado_clifinal = clifinal.cldomain_f(config.CLEARBIT_API_KEY, dominio)

    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '3':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) VIRUS TOTAL
B) IBM X-FORCE EXCHANGE
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        resource = input('Introduzca la URL >> ')

        print(Cursor.FORWARD(1))

        resultado_virustotal = virustotal.url_f(config.VIRUS_TOTAL_API_KEY, resource)

    elif modulo == 'B':

        url = input('Introduzca la URL >> ')

        print(Cursor.FORWARD(1))

        resultado_xforce = xforce.url_rep(config.auth, url) 
        resultado_xforce = xforce.url_dns(config.auth, url)
        resultado_xforce = xforce.url_whois(config.auth, url)

    else:
        
        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '4':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) CENSYS
B) RISQIK
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        ct = input('Introduzca la el Certificado sha256 >> ')

        print(Cursor.FORWARD(1))

        resultado_censys = censys.ct_f(config.auth, ct)

    elif modulo == 'B':

        hash = input('Introduzca el Certificado sha1 >> ')

        print(Cursor.FORWARD(1))

        resultado_riskiq = riskiq.risk_cert(config.auth, hash)

    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '5':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) VIRUS TOTAL    
B) IBM X-FORCE EXCHANGE
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        hash = input('Introduzca el Hash md5, sha1 o sha256 >> ')

        print(Cursor.FORWARD(1))

        resultado_virustotal = virustotal.hash_f(config.VIRUS_TOTAL_API_KEY, hash)

    elif modulo == 'B':

        hash = input('Introduzca el Hash md5, sha1 o sha256 >> ')

        print(Cursor.FORWARD(1))

        resultado_xforce = xforce.mal_hash(config.auth, hash) 

    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '6':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) TRANSACCIONES (BLOCKCHAIN.INFO)
B) DIRECCIONES DE BITCOIN (BLOCKCHAIN.INFO)
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        tr = input('Introduzca el Hash de la Transacción >> ')

        print(Cursor.FORWARD(1))

        resultado_blockchain = blockchain.trans_b(tr)

    elif modulo == 'B':

        dr = input('Introduzca el Hash de la Dirección >> ')

        print(Cursor.FORWARD(1))

        resultado_blockchain = blockchain.direc_b(dr)

    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '7':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) CLEARBIT (Información sobre Personas)
B) DEHASED (Emails,Passwords, Usernames, Hashes o Números de Teléfono)
C) BOTSCOUT (Bots)
D) SCYLLA (Emails)
E) SCYLLA (Passwords)
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        email = input('Introduzca el Email >> ')

        print(Cursor.FORWARD(1))

        resultado_clifinal = clifinal.clemail_f(config.CLEARBIT_API_KEY, email)

    elif modulo == 'B':

        target = input('Introduzca el Email >> ')

        print(Cursor.FORWARD(1))

        resultado_dehased = dehased.dehas_f(config.auth, target)

    elif modulo == 'C':

        email = input('Introduzca el Email >> ')

        print(Cursor.FORWARD(1))

        resultado_botscout = botscout.botemail_f(config.BOTSCOUT_API_KEY, email)
        
    elif modulo == 'D':

        email = input('Introduzca el Email >> ')

        print(Cursor.FORWARD(1))

        resultado_scylla = scylla.scylla_mail(config.auth, email)

    elif modulo == 'E':

        contraseña = input('Introduzca el Password >> ')

        print(Cursor.FORWARD(1))

        resultado_scylla = scylla.scylla_pass(config.auth, contraseña)
        
    else:
            
        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '8':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) CLEARBIT (Personas a través de un email)
B) CLEARBIT (Empresas a través de un Dominio)
C) LIBREBORME (Búsqueda de Personas)
D) LIBREBORME (Búsqueda de Empresas)
E) LIBREBORME (Información sobre Personas)
F) LIBREBORME (Información sobre Empresas)
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        email = input('Introduzca el Email de la Persona >> ')

        print(Cursor.FORWARD(1))

        resultado_clifinal = clifinal.clemail_f(config.CLEARBIT_API_KEY, email)

    elif modulo == 'B':

        dominio = input('Introduzca el Dominio de la Empresa >> ')

        print(Cursor.FORWARD(1))

        resultado_clifinal = clifinal.cldomain_f(config.CLEARBIT_API_KEY, dominio)

    elif modulo == 'C':

        nombre = input('Introduzca el Nombre y Apellidos de la Persona a buscar >> ')

        print(Cursor.FORWARD(1))

        resultado_libreborme = libreborme.search_persons(nombre)
        
    elif modulo == 'D':

        empresa = input('Introduzca el Nombre de la Empresa a buscar >> ')

        print(Cursor.FORWARD(1))

        resultado_libreborme = libreborme.search_companies(empresa)


    elif modulo == 'E':

        apellidos = input('Introduzca los Apellidos de la Persona a Investigar (N en lugar de Ñ) >> ')

        print(Cursor.FORWARD(1))

        nombre = input('Introduzca el Nombre de la Persona a Investigar (N en lugar de Ñ) >> ')

        print(Cursor.FORWARD(1))

        resultado_libreborme = libreborme.persons(apellidos, nombre)

    elif modulo == 'F':

        empresa = input('Introduzca el Nombre de la Empresa a Investigar >> ')

        print(Cursor.FORWARD(1))

        resultado_libreborme = libreborme.empresas(empresa)

    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

elif entrada == '9':

    print(Fore.WHITE+'''
------------------------------------------
-----Selecciona el Módulo a utilizar------
------------------------------------------

A) USERCHECKER (Nicks, Usernames)
B) DEHASED (Emails,Passwords, Usernames, Hashes o Números de Teléfono)
C) BOTSCOUT (Bots)
'''+Fore.RESET)

    print(Cursor.FORWARD(1))

    modulo = input(Fore.WHITE+'Seleccione su opción >> '+Fore.RESET)

    if modulo == 'A':

        username = input('Introduzca el Username / Nick  >> ')

        print(Cursor.FORWARD(1))

        resultado_userchecker = userchecker.instagram(username)  
        resultado_userchecker = userchecker.facebook(username) 
        resultado_userchecker = userchecker.twitter(username)  
        resultado_userchecker = userchecker.pinterest(username) 
        resultado_userchecker = userchecker.flickr(username) 
        resultado_userchecker = userchecker.github(username) 
        resultado_userchecker = userchecker.reddit(username)

    elif modulo == 'B':

        target = input('Introduzca el Username / Nick  >> ')

        print(Cursor.FORWARD(1))

        resultado_dehased = dehased.dehas_f(config.auth, target)

    elif modulo == 'C':

        name = input('Introduzca el Username / Nick  >> ')

        print(Cursor.FORWARD(1))

        resultado_botscout = botscout.botname_f(config.BOTSCOUT_API_KEY, name)
        
    else:

        print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")

else:

    print("Ninguna opción seleccionada. Lanze de nuevo el programa y seleccione una de entre las disponibles")




    


        















        

    





