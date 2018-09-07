# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:00:57 2018

Investigación para el desarollo de una clase que defina funciones saquen
información a través de métodos. 

El constructor crea un dataSet como atributo y sobre el se estraera informacion.

@author: Javier Carracedo
"""

import pandas as pd
from collections import Counter


class PreprocessingStatistics:
    def __init__(self, path):
        '''
            Constructor de la clase
        '''
        self.path= path
        self.dataSet = pd.read_csv(path.replace('\\','/'),index_col=0,encoding='latin1', low_memory=False)
    
    def getDataFrameByColumnsName(self, cad):
        '''
        DESCRIPCION:
            
            Devuelve un dataSet que contenga la subCadena 
            (que se pasa por parámetro). (IMPLEMENTADO)
        
        EJEMPLO: d = x.getDataFrameByColumnsName("location")
            
        '''
        #Buscamos en el dataSet todas las columnas que contengan esa subcadena.
        arrayDataSetColums = list(self.dataSet.columns.values)
        array = []
        
        for i in range(len(arrayDataSetColums)):
            if(cad in arrayDataSetColums[i]):
                array.append(arrayDataSetColums[i])
        
        df = self.dataSet[array]
        return  df
        
    def printColumnsDataset(self):
        '''
        DESCRIPCION:
            Muestra el nombre de las columnas y su indice cargadas en unn 
            dataSet, imprimiendo por consola. (IMPLEMENTADO)
            
        EJEMPLO: x.printColumnsDataset()
            
            -------------------------------------------------------------
            [Columna DataSet] - Nombre de la columna
            -------------------------------------------------------------
            [Column: 0 ] - bearer.apn
            [Column: 1 ] - bearer.msisdn
            [Column: 2 ] - bearer.imeisv
                .
                .
                .
            [Column: 110 ] - lte.pgw-teid-u
            [Column: 111 ] - lte.sgw-teid-c
            [Column: 112 ] - lte.sgw-teid-u
            [Column: 113 ] - lte.mme-teid
            [Column: 114 ] - lte.enodeb-teid
            -------------------------------------------------------------
            INFO: Hay  115  columnas de 115  que hay en total.
            -------------------------------------------------------------
        '''
        cont = 0
        col = self.dataSet.columns
        print("-------------------------------------------------------------")
        print("[Columna DataSet] - Nombre de la columna")
        print("-------------------------------------------------------------")
        for i in range (len(col)):
            print("[Column:",i,"]","-",col[i])
            cont = cont +1
        print("-------------------------------------------------------------")
        print("INFO: Hay ", cont," columnas de", self.dataSet.columns.size, " que hay en total.")
        print("-------------------------------------------------------------")
    
    def printColumnsDatasets(self,df1):
        '''
            DESCRIPCION:
                
            Muestra las columnas y su indice de un dataSet, imprimiendo por consola. 
            (IMPLEMENTADO)
            
            EJEMPLO:    
                a = x.getDataFrameByColumnsName("location")
                b = x.dataSet
                x.printColumnsDatasets(a)
                
                    -------------------------------------------------------------
                    [dataSetGeneral] - Columna sub Dataset:
                    -------------------------------------------------------------
                    [column: 29 ] - Colum: 0 - location.mcc
                    [column: 30 ] - Colum: 1 - location.mnc
                    [column: 31 ] - Colum: 2 - location.lac
                    [column: 32 ] - Colum: 3 - location.sac
                    [column: 33 ] - Colum: 4 - location.ci
                    -------------------------------------------------------------
                    INFO: Hay  5  columnas  115  que hay en total.
                    -------------------------------------------------------------
        '''
        cont = 0
        col = df1.columns
        print("\n-------------------------------------------------------------")
        print("[dataSetGeneral] - Columna sub Dataset:")
        print("-------------------------------------------------------------")
        for i in range (len(col)):
            print("[column:",self.dataSet.columns.get_loc(col[i]),"]","- Colum:",i ,"-",col[i])
            cont = cont +1
        print("-------------------------------------------------------------")
        print("INFO: Hay ", cont," columnas de", self.dataSet.columns.size, " que hay en total.")
        print("-------------------------------------------------------------")
        
    def printColumnsDatasetIfContains(self,subCadena):
        '''
            DESCRIPCION:
                
            Muestra las columnas y su indice de un dataSet, imprimiendo por consola,
            si contienen una subcadena que se le pasa por parámetro. (IMPLEMENTADO)
        '''
        cont = 0
        col = self.dataSet.columns
        print("-------------------------------------------------------------")
        print("Columnas que contienen la subcadena '",subCadena,"'.\n")
        for i in range (len(col)):
            if (subCadena in col[i]):        
                print("[column:",i,"]","-",col[i])
                cont = cont + 1
        print("-------------------------------------------------------------")
        print("\nINFO: Hay ", cont," columnas ", self.dataSet.columns.size, " que hay en total.")
        print("-------------------------------------------------------------")
        
    def printColumnsDatasetIfContainsWithPercentNullValues(self,subCadena):
        '''
            DESCRIPCION:
                
            Muestra las columnas y su indice de un dataSet, imprimiendo por consola,
            si contienen una subcadena que se le pasa por parámetro (IMPLEMENTADO)
            
            EJEMPLO:
            --------------------------------------------------------------------------
            [Numuero Columna] - Colum con subcadena: ' event ' y % NanValues by column
            --------------------------------------------------------------------------
            [column: 10 ] - event.text       2.17 % de NanValues
            [column: 11 ] - event.timestamp          5.27 % de NanValues
            [column: 24 ] - event.interim-id         6.43 % de NanValues
            [column: 41 ] - event.start-time         0.00 % de NanValues
            [column: 42 ] - event.stop-time          0.02 % de NanValues
            --------------------------------------------------------------------------
            INFO: Hay  5  columnas de 115  que hay en total.
            --------------------------------------------------------------------------
        '''
        cont = 0
        col = self.dataSet.columns
        print("--------------------------------------------------------------------------")
        print("[Numuero Columna] - Colum con subcadena: '",subCadena,"' y % NanValues by column")
        print("--------------------------------------------------------------------------")
        for i in range (len(col)):
            if (subCadena in col[i]):
                #Calculo del porcentaje de NanValues de la columna
                n = "{0:.2f}".format((self.dataSet.iloc[:,i].isnull().sum())/(len(self.dataSet))*100)
                print("[column:",i,"]","-",col[i],"\t",n,"% de NanValues")
                cont = cont +1
        print("--------------------------------------------------------------------------")
        print("INFO: Hay ", cont," columnas de", self.dataSet.columns.size, " que hay en total.")
        print("--------------------------------------------------------------------------")
        
    def printColumnsDatasetsIfContains(self, subCadena):
        '''
            Imprimiendo por consola, crea un dataSet con las columnas que contienen la subcadena
            que se le pasa por parámetro. Además, ofrece información de a qué columna corresponde
            del dataSet de la clase (IMPLEMENTADO)
            
            Ejemplo: 'getDataFrameByColumnsName("event")'
            
            -------------------------------------------------------------
            [Indice dataSetGeneral] - |columna sub Dataset: ' event '|.
            -------------------------------------------------------------
            [column: 10 ] - | Colum: 0 | - event.text
            [column: 11 ] - | Colum: 1 | - event.timestamp
            [column: 24 ] - | Colum: 2 | - event.interim-id
            [column: 41 ] - | Colum: 3 | - event.start-time
            [column: 42 ] - | Colum: 4 | - event.stop-time
            -------------------------------------------------------------
            Hay  5  columnas en total.
            -------------------------------------------------------------
        '''
        df1 = self.getDataFrameByColumnsName(subCadena)
        
        cont = 0
        col = df1.columns
        print("\n-------------------------------------------------------------")
        print("[Indice dataSetGeneral] - |columna sub Dataset: '",subCadena,"'|.")
        print("-------------------------------------------------------------")
        for i in range (len(col)):
            if (subCadena in col[i]):        
                print("[column:",self.dataSet.columns.get_loc(col[i]),"]","- | Colum:",i ,"| -",col[i])
                cont = cont +1
        print("-------------------------------------------------------------")
        print("Hay ", cont," columnas en total.")
        print("-------------------------------------------------------------")
        
    
    