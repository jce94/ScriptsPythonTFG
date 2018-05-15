# -*- coding: utf-8 -*-
"""
Editor de Spyder
Created on Wed May 16 00:40:01 2018

@author: Javier
"""

import pandas as pd
from collections import Counter

def printColumnsDataset(df0):
    '''Muestra las columnas y su indice de un dataSet, imprimiendo por consola.'''
    cont = 0
    col = df0.columns
    print("\n[Indice dataSetGeneral]")
    for i in range (len(col)):
        print("[column:",i,"]","-",col[i])
        cont = cont +1
    print("Hay ", cont," columnas en total.")

def printColumnsDatasets(df0,df1):
    '''Muestra las columnas y su indice de un dataSet, imprimiendo por consola.'''
    cont = 0
    col = df1.columns
    print("\n[Indice dataSetGeneral] - Columna sub Dataset:\n")
    for i in range (len(col)):
        print("[column:",df0.columns.get_loc(col[i]),"]","- Colum:",i ,"-",col[i])
        cont = cont +1
    print("Hay ", cont," columnas en total.")
    
def printColumnsDatasetIfContains(df0,subCadena):
    '''Muestra las columnas y su indice de un dataSet, imprimiendo por consola,
    si contienen una subcadena que se le pasa por parámetro.'''
    cont = 0
    col = df0.columns
    print("\n[Indice dataSetGeneral] - columna sub Dataset:",subCadena,".\n")
    for i in range (len(col)):
        if (subCadena in col[i]):        
            print("[column:",i,"]","-",col[i])
            cont = cont +1
    print("Hay ", cont," columnas en total.")
    
    
def printColumnsDatasetIfContainsWithPercentNullValues(df0,subCadena):
    '''Muestra las columnas y su indice de un dataSet, imprimiendo por consola,
    si contienen una subcadena que se le pasa por parámetro.'''
    cont = 0
    col = df0.columns
    print("\n[Indice dataSetGeneral] - columna sub Dataset:",subCadena,".\n")
    for i in range (len(col)):
        if (subCadena in col[i]):
            #Calculo del porcentaje de NanValues de la columna
            n = "{0:.2f}".format((df0.iloc[:,i].isnull().sum())/(len(df0))*100)
            print("[column:",i,"]","-",col[i],"-",n,"% de NanValues")
            cont = cont +1
    print("Hay ", cont," columnas en total.")
    
def printColumnsDatasetsIfContains(df0,df1,subCadena):
    '''Muestra las columnas y su indice de un dataSet, imprimiendo por consola,
    si contienen una subcadena que se le pasa por parámetro.'''
    cont = 0
    col = df1.columns
    print("\n[Indice dataSetGeneral] - columna sub Dataset:",subCadena,".\n")
    for i in range (len(col)):
        if (subCadena in col[i]):        
            print("[column:",df0.columns.get_loc(col[i]),"]","- Colum:",i ,"-",col[i])
            cont = cont +1
    print("Hay ", cont," columnas en total.")
    
    
def funtionCounter(dataFrame):
    ''''''
    array = []
    for i in range(len(dataFrame.columns)):
        p = dataFrame.iloc[:,i]
        c = Counter(p)
        array.append(c)
    return array
    
ruta = "" #TOP ADD RUTA ANTES DE EJECUTAR

dataSet = pd.read_csv(ruta,encoding='latin1', low_memory=False)

''' Columnas bearer 
    0 - bearer.imsi
    1 - bearer.apn
    2 - bearer.msisdn
    3 - bearer.imeisv
    4 - bearer.packetsUp
    5 - bearer.packetsDown
    6 - bearer.totalPackets
    7 - bearer.volumeUp
    8 - bearer.volumeDown
    9 - bearer.totalVolume
    10 - bearer.user-ip
    
    36 - bearer.charging-id
    
    44 - bearer.start-time
    45 - bearer.stop-time
    
    55 - bearer.rat-type-str
    
    86 - bearer.summary-throughput-up
    87 - bearer.summary-throughput-down
    88 - bearer.summary-throughput
    
    92 - bearer.summary-total-activity-up
    93 - bearer.summary-total-activity-down
    94 - bearer.summary-total-activity
    95 - bearer.total-volume-up
    96 - bearer.total-volume-down
'''
a = list(range(0,11))
b = [36,44,45,55,86,87,88]
c = list(range(92,97))

vector = a + b + c #Unión de los vectores

bearer = dataSet.iloc[:,vector]

'''
COLUMNAS: LOCATION
    30  -  location.mcc
    31  -  location.mnc
    32  -  location.lac
    33  -  location.sac
    34  -  location.ci
'''
location =   dataSet.iloc[:,30:35]

'''
COLUMNAS: NET
    0  -  net.cell-ip
    1  -  net.cell-port
    2  -  net.srv-ip
    3  -  net.srv-port
    4  -  net.tag
    5  -  net.application-tag
    6  -  net.avg-latency
    7  -  net.termination-code
    8  -  net.throughputUp
    9  -  net.throughputDown
    10  -  net.peak-throughputUp
    11  -  net.peak-throughputDown
    12  -  net.uplink
    13  -  net.duration
    14  -  net.ip-proto
    15  -  net.activity-duration
    16  -  net.activity-duration-up
    17  -  net.activity-duration-down
'''
net = dataSet.iloc[:,0:18]
'''
COLUMNAS: EVENT
    [column: 11 ] - event.text
    [column: 12 ] - event.timestamp
    [column: 25 ] - event.interim-id
    [column: 42 ] - event.start-time
    [column: 43 ] - event.stop-time
'''

vector = [11,12,25,42,43]
event = dataSet.iloc[:,vector]


#Eliminacion del dataSet "event" de las filas que en alguna columna tinen un nan.
dataEvent = event.dropna()
#Eliminacion del dataSet "bearer" de las filas que en alguna columna tinen un nan.
dataBearer = bearer.dropna()
#Eliminacion del dataSet "location" de las filas que en alguna columna tinen un nan.
dataLocation = location.dropna()
#Eliminacion del dataSet "net" de las filas que en alguna columna tinen un nan.
dataNet = net.dropna()



arrayCounter_dataBearer = funtionCounter(dataBearer)
arrayCounter_dataLocation = funtionCounter(dataLocation)
arrayCounter_dataNet = funtionCounter(dataNet)
arrayCounter_dataEvent= funtionCounter(dataEvent)

'''BORRADO DE VARIABLES AUXILIARES'''
del a,b,c, vector
#%%

#printColumnsDataset(dataSet)
#printColumnsDatasets(dataSet,location)
#printColumnsDatasetsIfContains(dataSet,net,"event")
#printColumnsDatasetIfContains(dataSet,"http")
printColumnsDatasetIfContainsWithPercentNullValues(dataSet,"gtp")
#%%
    