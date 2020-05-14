# -------------------------------------------------------------------------------
# Name:         BlockchainWrapper.py
# Purpose:      BlockchainInfo module to provide data on recent transactions & Wallets 
#               in the Bitcoin Blockchain 
#
# Author:      Jorge Iturria 
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

def trans_b(tr):

    try:

        url = "https://blockchain.info/rawtx/$tx_hash"
        
        response = requests.get("https://blockchain.info/rawtx/" + tr)
        
        if response.status_code == 404: 
        
            print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la Transacción solicitada"+Fore.RESET+Style.RESET_ALL)
        
            print(Cursor.DOWN(1))
        
            print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
        
            print(Cursor.DOWN(1))
        
            exit()
        
        respuesta = response.json()
        
        dict_trx = {}
        
        array_envio = []

        for inputs in respuesta["inputs"]:
        
            if 'inputs' != None:
        
                dict_input = {"Dirección de Envío": respuesta["inputs"][0]["prev_out"].get("addr", ''),
        
                              "Valor Total de Salida de la Transacción (Satoshis)": respuesta["inputs"][0]["prev_out"].get("value", '')}

        array_envio.append(dict_input)
        
        dict_trx.update({"Dirección de Envio": array_envio})
        
        array_recepcion1 = []
        
        for out in respuesta["out"]:
        
            if 'out' != None:
        
                dict_out1 =  {"Dirección de Recepción 1": respuesta["out"][0].get("addr", ''),
        
                              "Valor Transacción 1 (Satoshis)": respuesta["out"][0].get("value", '')}
        
        array_recepcion1.append(dict_out1)
        
        dict_trx.update({"Recepción1": array_recepcion1}) 
        
        array_recepcion2 = []
        
        try:

            for out in respuesta["out"]:
        
                if 'out' != None:
        
                    dict_out2 =  {"Dirección de Recepción 2": respuesta["out"][1].get("addr", ''),
        
                                  "Valor Transacción 2 (Satoshis)": respuesta["out"][1].get("value", '')}
        
            array_recepcion2.append(dict_out2)
        
            dict_trx.update({"Recepción2": array_recepcion2})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass
        
        array_recepcion3 = []
    
        try:
        
            for out in respuesta["out"]:
        
                if 'out' != None:
        
                    dict_out3 =  {"Dirección de Recepción 3": respuesta["out"][2].get("addr", ''),
        
                                  "Valor Transacción 3 (Satoshis)": respuesta["out"][2].get("value", '')}
    
        
            array_recepcion3.append(dict_out3)
        
            dict_trx.update({"Recepción3": array_recepcion3})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass
        
        array_recepcion4 = []
        
        try:

            for out in respuesta["out"]:
        
                if 'out' != None:
           
                    dict_out4 =  {"Dirección de Recepción 4": respuesta["out"][3].get("addr", ''),
        
                                  "Valor Transacción 4 (Satoshis)": respuesta["out"][3].get("value", '')}
        
            array_recepcion4.append(dict_out4)
        
            dict_trx.update({"Recepción4": array_recepcion4})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass
        
        array_recepcion5 = []
            
        try:

            for out in respuesta["out"]:
        
                if 'out' != None:
        
                    dict_out5 =  {"Dirección de Recepción 5": respuesta["out"][4].get("addr", ''),
        
                                  "Valor Transacción 5 (Satoshis)": respuesta["out"][4].get("value", '')}
        
            array_recepcion5.append(dict_out5)
        
            dict_trx.update({"Recepción5": array_recepcion5})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass

        array_block = []
        
        for block in respuesta:
        
            if ["block_height"] != None:
        
                dict_block = {}
        
                dict_block.update({"Número de Bloque": respuesta["block_height"]})
        
            if ["time"] != None:
        
                dict_block.update({"Time": respuesta["time"]})
        
        array_block.append(dict_block)

        dict_trx.update({"Bloque": array_block})

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"El Hash introducido no se corresponde con ninguna operación registrada en la Blockchain de Bitcoin"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()

    if (array_envio) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA]---------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_envio)
        print(Cursor.DOWN(1))

    if (array_recepcion1) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RECEIPT DATA INFO 1]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_recepcion1)
        print(Cursor.DOWN(1))

    if (array_recepcion2) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RECEIPT DATA INFO 2]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_recepcion2)
        print(Cursor.DOWN(1))  

    if (array_recepcion3) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RECEIPT DATA INFO 3]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_recepcion3)
        print(Cursor.DOWN(1))

    if (array_recepcion4) != []:

        print(Fore.GREEN+Style.BRIGHT+"[RECEIPT DATA INFO 4]-----------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_recepcion4)
        print(Cursor.DOWN(1))

    if (array_block) != []:
        print(Fore.GREEN+Style.BRIGHT+"[BLOCK INFO]--------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_block)
        print(Cursor.DOWN(1)) 
    
    print(Fore.CYAN+"Programa finalizado")
    print(Cursor.DOWN(1))

def direc_b(dr):

    try:

        url = "https://blockchain.info/rawaddr/$bitcoin_address"

        response = requests.get("https://blockchain.info/rawaddr/" + dr)

        if response.status_code == 404: 
            
            print(Fore.RED+Style.BRIGHT+"No se han obtenido datos para la Dirección solicitada"+Fore.RESET+Style.RESET_ALL)
            print(Cursor.DOWN(1))
            print (Fore.CYAN+"Programa Finalizado"+Fore.RESET)
            print(Cursor.DOWN(1))
            exit()

        respuesta = response.json()

        dict_direc = {}

        array_general = []

        for address in respuesta:
        
            if (["hash160"] != None):
        
                dict_general = {}
        
                dict_general.update({"Hash160":respuesta["hash160"]})
        
            if (["n_tx"] != None):
        
                dict_general.update({"Transacciones":respuesta["n_tx"]})
        
            if (["total_received"] != None):
        
                dict_general.update({"Total_Recibido (Satoshis)":respuesta["total_received"]})
        
            if (["total_sent"] != None):
        
                dict_general.update({"Total_Enviado (Satoshis)":respuesta["total_sent"]})
        
            if (["final_balance"] != None):
        
                dict_general.update({"Saldo (Satoshis)":respuesta["final_balance"]})
        
        array_general.append(dict_general)   
        
        dict_direc.update({"General": array_general})
        
        array_ent1 = []
        
        try:

            for txs in respuesta["txs"]:
        
                if 'txs' != None:
        
                    dict_ent1 = {"Dirección de Destino": respuesta["txs"][0]["out"][0]["addr"],
        
                                "Valor de Transacción (Satoshis)": respuesta["txs"][0]["out"][0]["value"],
        
                                "Bloque": respuesta["txs"][0]["block_height"]}
        
            array_ent1.append(dict_ent1)
        
            dict_direc.update({"Transacción de Entrada 1": array_ent1})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass
        
        array_ent2 = []
        
        try:

            for txs in respuesta["txs"]:
        
                if 'txs' != None:
        
                    dict_ent2 = {"Dirección de Destino": respuesta["txs"][1]["out"][0]["addr"],
        
                                "Valor de Transacción (Satoshis)": respuesta["txs"][1]["out"][0]["value"],
        
                                "Bloque": respuesta["txs"][1]["block_height"]}
        
            array_ent2.append(dict_ent2)
        
            dict_direc.update({"Transacción de Entrada 2": array_ent2})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass 
        
        array_ent3 = []
        
        try:

            for txs in respuesta["txs"]:
        
                if 'txs' != None:
        
                    dict_ent3 = {"Dirección de Destino": respuesta["txs"][2]["out"][0]["addr"],
        
                                "Valor de Transacción (Satoshis)": respuesta["txs"][2]["out"][0]["value"],
        
                                "Bloque": respuesta["txs"][2]["block_height"]}
        
            array_ent3.append(dict_ent3)
        
            dict_direc.update({"Transacción de Entrada 3": array_ent3})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass 
        
        array_ent4 = []
        
        try:

            for txs in respuesta["txs"]:
        
                if 'txs' != None:
        
                    dict_ent4 = {"Dirección de Destino": respuesta["txs"][3]["out"][0]["addr"],
        
                                "Valor de Transacción (Satoshis)": respuesta["txs"][3]["out"][0]["value"],
        
                                "Bloque": respuesta["txs"][3]["block_height"]}
        
            array_ent4.append(dict_ent4)
        
            dict_direc.update({"Transacción de Entrada 4": array_ent4})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass 

        array_ent5 = []
        
        try:

            for txs in respuesta["txs"]:
        
                if 'txs' != None:

                    dict_ent5 = {"Dirección de Destino": respuesta["txs"][4]["out"][0]["addr"],
        
                                "Valor de Transacción (Satoshis)": respuesta["txs"][4]["out"][0]["value"],
        
                                "Bloque": respuesta["txs"][4]["block_height"]}
        
            array_ent5.append(dict_ent5)

            dict_direc.update({"Transacción de Entrada 5": array_ent5})
        
        except (IndexError, KeyError, UnboundLocalError):
        
            pass 

    except json.decoder.JSONDecodeError:

        print(Fore.RED+"El Hash introducido no se corresponde con ninguna Dirección de Bitcoin"+Fore.RESET)
        print(Cursor.DOWN(1))
        print (Fore.CYAN+"Programa Finalizado")
        print(Cursor.DOWN(1))
        exit()
    
    if (array_general) != []:

        print(Fore.GREEN+Style.BRIGHT+"[GENERAL INFO]------------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_general)
        print(Cursor.DOWN(1))

    if (array_ent1) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA INFO 1]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ent1)
        print(Cursor.DOWN(1))

    if (array_ent2) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA INFO 2]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ent2)
        print(Cursor.DOWN(1))

    if (array_ent3) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA INFO 3]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ent3)
        print(Cursor.DOWN(1))

    if (array_ent4) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA INFO 4]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ent4)
        print(Cursor.DOWN(1))

    if (array_ent5) != []:

        print(Fore.GREEN+Style.BRIGHT+"[SENT DATA INFO 5]--------------------------------------------------------------------[STATUS OK]"+Fore.RESET+Style.RESET_ALL)
        print() 
        print(array_ent5)
        print(Cursor.DOWN(1))

    print(Fore.CYAN+"Programa finalizado")
    print(Cursor.DOWN(1))




