# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys
import requests
import traceback

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #type:ignore
fintoc_directory_path = os.path.join(base_path, "modules", "Fintoc")
fintoc_libs_path = os.path.join(fintoc_directory_path, "libs") 

if fintoc_libs_path not in sys.path:
    sys.path.append(fintoc_libs_path)


class Fintoc:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.getCert()
        
        
    def getCert(self):
        self.base_url = "https://api.fintoc.com/v1/links/"
        self.headers = {
            'accept': 'application/json',
            'Authorization': '{}'.format(self.api_key)
        }
        
        r = requests.get(self.base_url, headers=self.headers)

        if r.status_code == 200:
            return True
        if r.status_code == 401:
            raise Exception("Invalid API Key")
        
        
    def listLinks(self, status=None):
        url = "https://api.fintoc.com/v1/links/"
        
        if status:
            url += "?status={}".format(status)
        
        r = requests.get(url, headers=self.headers)
        return r.json()
    
    
    def retrieveLink(self, link_token):
        url = "https://api.fintoc.com/v1/links/{}".format(link_token)
        r = requests.get(url, headers=self.headers)
        return r.json()
    
    
    def listInvoices(self, link_token):
        url = "https://api.fintoc.com/v1/invoices?link_token={}".format(link_token)
        r = requests.get(url, headers=self.headers)
        return r.json()
    
    
    def listAccounts(self, link_token):
        url = "https://api.fintoc.com/v1/accounts?link_token={}".format(link_token)
        r = requests.get(url, headers=self.headers)
        return r.json()
    

    def retrieveAccount(self, account_id):
        url = "https://api.fintoc.com/v1/accounts/{}".format(account_id)
        r = requests.get(url, headers=self.headers)
        return r.json()

    
    def listMovements(self, account_id, link_token):
        url = "https://api.fintoc.com/v1/accounts/{}/movements?link_token={}".format(account_id, link_token)
        r = requests.get(url, headers=self.headers)
        return r.json()
        

    def retrieveMovement(self, movement_id, account_id):
        url = "https://api.fintoc.com/v1/accounts/{}/movements/{}".format(account_id, movement_id)
        r = requests.get(url, headers=self.headers)
        return r.json()        
        
        

module = GetParams("module")

try:
    if module == "config":
        api_key = GetParams("secret_key")
        account_id = GetParams("account_id")
        fintoc = Fintoc(account_id, api_key)
        SetVar("result", fintoc)
    
    if module == "listLinks":
        status = GetParams("status")
        result = GetVar("result")
        
        SetVar("result", result.listLinks(status))
    
    if module == "retrieveLink":
        link_token = GetParams("link_token")
        result = GetVar("result")
        
        SetVar("result", result.retrieveLink(link_token))
        
    if module == "listInvoices":
        link_token = GetParams("link_token")
        result = GetVar("result")
        
        SetVar("result", result.listInvoices(link_token))
        
    if module == "listAccounts":
        link_token = GetParams("link_token")
        result = GetVar("result")
        
        SetVar("result", result.listAccounts(link_token))
    
    if module == "retrieveAccount":
        account_id = GetParams("account_id")
        result = GetVar("result")
        
        SetVar("result", result.retrieveAccount(account_id))
        
    if module == "listMovements":
        account_id = GetParams("account_id")
        link_token = GetParams("link_token")
        result = GetVar("result")
        
        SetVar("result", result.listMovements(account_id, link_token))
        
    if module == "retrieveMovement":
        movement_id = GetParams("movement_id")
        account_id = GetParams("account_id")
        result = GetVar("result")
        
        SetVar("result", result.retrieveMovement(movement_id, account_id))
    
except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e