#!/usr/bin/env python

import base64
import sys

def Descrypto(varSenha):
    password = varSenha.encode("utf-8")    
    decoded = base64.b64decode(password)
    original_text = decoded.decode("utf-8")
    #print(original_text) #para executar manualmente descomente o print
    return original_text
