#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:00:10 2023

@author: adrianfernandez
"""

import re

def obtenerFechaFacturacion(datos):
    """
    Esta funcion devuelve dos fechas en el caso de que haya un periodo de facturacion o una fecha en el caso de que el
    periodo de facturacion sea un dia en concreto.
    
    Parameters
    ----------
    datos : str
        string desde donde se obtendran los datos que se requieren

    Returns
    -------
    fechaFacturaInicio : str
        fecha de inicio de facturacion en caso de ser un periodo de facturacion o fecha de facturacion en caso de ser un dia en concreto
    fechaFacturaFin : str
        fecha de fin de facturacion en caso de ser un periodo de facturacion
        
    """
    #Si no hay datos se devuelve None
    if(datos == None or datos == ""):
        return None, None
    else:
        #Se declara expresion regular
        patronFecha = r"\d{,2}/\d{,2}/\d{,4}"
        #Se busca la expresion en el str datos
        resulFechas = re.findall(patronFecha, datos)
        #Si se ha encontrado varios resultados
        if len(resulFechas)>1:
            fechaFacturaInicio = resulFechas[0]
            fechaFacturaFin = resulFechas[1]
            #Se comprueba que las dos fechas no sean iguales
            if(fechaFacturaInicio == fechaFacturaFin):
                return fechaFacturaInicio,None
            else:
                return fechaFacturaInicio, fechaFacturaFin
        else:#Si solo hay un resultado
            fechaFacturaInicio = resulFechas
            return fechaFacturaInicio, None 

def obtenerImporteFacturacion(datos):
    """
    Esta funcion devuelve un listado con todos los importes de la factura
    
    Parameters
    ----------
    datos : str
        string desde donde se obtendran los datos que se requieren

    Returns
    -------
    valores : list
        lista que contiene todos los importes encontrados en el str datos
        
    """
    #Si no hay datos se devuelve None
    if((datos != None) or (datos != "")):
        #Se declara expresion regular
        patronImporte = r"\d+[,\.]\d{,2}"
        #Se busca la expresion en el str datos
        valores = re.findall(patronImporte, datos)
        return valores
    else:
        return None
    
#Declaracion de la URL donde buscar los datos
datos = "ARIAS CASTELLANO, DILIANA JOSE\nTRANSCANTÁBRICO, 11 - PORTAL\nCL DEL T\nL\n8 1-3\n28770 COLMENAR VIEJO\nCODIGO: 264459\nNIF : Y7729904D\nFECHA\nFACTURA\n31/08/22\n31/08/22\nCODIGO SAP: 000000050785779\nFACTURA\nNO.\n0224095856\n0224095857\nFECHA DE VENCIMIENTO: 07/09/22\nSEPA Direct Debit\nDIVISAS\nRESUMEN FACTURACION\nFECHA : 31/08/22\nNUMERO: 9643385430\nEUR\nEUR\nTOTAL\nDIVISAS\nB2M País de suministro: España\nB2Mobility GmbH\nWITTENER STRASSE 45\nTEL: 910 10 20 30\nFAX: 902 108 050\nNIF: ESN2765289J\nCONTACTO EN BP: tarjetasprofesionales@bp.com\nTOTAL\nEUR\nB2Mobility GmbH Inscrita en el R.M. de Bochum (Alemania) N.° de sociedad HRB 16999\nN.I.F.: N2765289J - NIF Intracomunitario ESN2765289J\nCR\nTOTAL\nEUR\nPag:\n96,11\n433,74\n529,85\nbp"

#Llamada a funciones
fecha_inicio, fecha_fin = obtenerFechaFacturacion(datos)
valores = obtenerImporteFacturacion(datos)

#No se encuentran fechas con la expresion regular utilizada
if(fecha_inicio == None and fecha_fin == None):
    print("No se ha encontrado la fecha de facturacion")
else:
    #Si no hay fecha_fin signfiica que la factura es solo de un dia
    if(fecha_fin == None):
        print("Fecha de facturacion:", fecha_inicio)
    else: #Si hay un periodo de facturracion de se imprimen ambos
        print("Fecha de inicio del período de facturacion:", fecha_inicio)
        print("Fecha de fin del período de facturacion:", fecha_fin)

#No se encuentran importes con la expresion regular utilizada
if(valores == None or len(valores) == 0):
    #No se ha encontrado el importe
    print("No se ha encontrado el importe de facturacion")
else:
    #Se imprime el importe total (siempre sera el ultimo valor encontrado en la factura)
    print("Importe total:", valores[len(valores)-1])
    

