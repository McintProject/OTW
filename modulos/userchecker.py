# -------------------------------------------------------------------------------
# Name:         UserCheckWrapper.py
# Purpose:      UserCheck module to check if a Nick or UserName 
#               exists in Mayor Social Network & Forums
#              
# Author:      Jorge Iturria 
# Contact:     pyproject@protonmail.com
#
# Created:     30/04/2020
# Copyright:   Copyright (C) 2020 - Jorge Iturria
# Licence:     GNU V3
# -------------------------------------------------------------------------------
import requests
import json
from urllib import request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import urllib3
from colorama import *
import os
import re

def instagram(username):

    url = "https://instagram.com/" + username + "/"

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[INSTAGRAM]--------------------[STATUS OK]---------[EL USUARIO INTRODUCIDO EXISTE IN INSTAGRAM]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[INSTAGRAM]------------------[NOT FOUND]---------[EL USUARIO INTRODUCIDO NO EXISTE EN INSTAGRAM]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def facebook(username):

    url = "https://www.facebook.com/" + username

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[FACEBOOK]---------------------[STATUS OK]---------[EL USUARIO INTRODUCIDO EXISTE IN FACEBOOK]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[FACEBOOK]--------------------[NOT FOUND]--------[EL USUARIO INTRODUCIDO NO EXISTE EN FACEBOOK]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def twitter(username):

    url = "https://twitter.com/" + username

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[TWITTER]----------------------[STATUS OK]---------[EL USUARIO INTRODUCIDO EXISTE IN TWITTER]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[TWITTER]--------------------[NOT FOUND]---------[EL USUARIO INTRODUCIDO NO EXISTE EN TWITTER]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def pinterest(username):

    url = "https://www.pinterest.es/" + username + "/"

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[PINTEREST]---------------------[STATUS OK]--------[EL USUARIO INTRODUCIDO EXISTE IN PINTEREST]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[PINTEREST]-------------------[NOT FOUND]--------[EL USUARIO INTRODUCIDO NO EXISTE EN PINTEREST]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def flickr(username):

    url = "https://www.flickr.com/photos/" + username + "/"

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[FLICKR]------------------------[STATUS OK]--------[EL USUARIO INTRODUCIDO EXISTE IN FLICKR]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[FLICKR]---------------------[NOT FOUND]------------[EL USUARIO INTRODUCIDO NO EXISTE EN FLICKR]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def github(username):

    url = "https://github.com/" + username  

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[GITHUB]------------------------[STATUS OK]-----------[EL USUARIO INTRODUCIDO EXISTE IN GITHUB]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[GITHUB]----------------------[NOT FOUND]-----------[EL USUARIO INTRODUCIDO NO EXISTE EN GITHUB]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

def reddit(username):

    url = "https://www.reddit.com/user/" + username + "/"

    try:

        response = request.urlopen(url)

        if response.status == 200:

            print(Fore.GREEN+Style.BRIGHT+"[REDDIT]------------------------[STATUS OK]-----------[EL USUARIO INTRODUCIDO NO EXISTE EN REDDIT]"+Fore.RESET+Style.RESET_ALL)
            print()
            print(Fore.CYAN+url+Fore.RESET)
            print(Cursor.DOWN(1))

    except HTTPError as e:

            if e.code == 404:

                print(Fore.RED+Style.BRIGHT+"[REDDIT]----------------------[NOT FOUND]-----------[EL USUARIO INTRODUCIDO NO EXISTE EN REDDIT]"+Fore.RESET+Style.RESET_ALL)
                print()
                print(Cursor.DOWN(1))

    print (Fore.CYAN+"Programa Finalizado")
    print(Cursor.DOWN(1))