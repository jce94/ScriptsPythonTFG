# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:03:56 2018

    Investigación para el desarrollo de una clase que de muestre estadísticas
    gráficas a partir de un archivo.csv.
    
    Las estadísticas serán enfocadas a visualizar información acerca de la
    cantidad y el porcentaje de NanValues que hay en un determinado dataSet.

@author: Javier Carracedo Esteban
"""
#-----------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ClassPreprocessingGraphics:
    def __init__(self, path):
        '''
            Constructor de la clase
        '''
        self.path= path
        self.dataSet = pd.read_csv(path.replace('\\','/'),index_col=0,
                                   encoding='latin1', low_memory=False)
        
    def plotColumnsMenorSinCorte(self,i):
        '''
            DESCRIPCION: 
                Visualiza una gráfica de barras ordenadas de mayor a menor numero
                de muestras de % de NanValues por columna. (IMPLEMENTADA)
        '''                   
        
        #Separacion de la ruta. Last element of array, name file
        array = self.path.split('\\')
        
        '''Busqueda de % de NaN values por columna.'''
            
        t = self.dataSet.shape[0] #Numero de columnas. 
        porc_NaNValues = ((self.dataSet.isnull().sum())/t)*100        
        n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.       
        porc_NaNValues_order = n.sort_values(ascending=False)       
        vector = porc_NaNValues_order[porc_NaNValues_order>30] #Datos X        
        labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y        
        
        if (0<=i) and (100>=i):
            plt.style.use('seaborn')
            vector = porc_NaNValues_order[porc_NaNValues_order<i] #Datos X
            labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y
            
            objects = labels
            y_pos = np.arange(len(objects))
            performance = vector
             
            plt.bar(y_pos, performance, align='center', alpha=0.5,)
            plt.xticks(y_pos, objects,rotation='vertical')
            plt.ylabel('% de NanN Values\n por columna.')    
            plt.tight_layout()           
            plt.title(str(vector.size) + ' de 116 columnas con un porcentaje menor al ' +
                      str(i) + '% de NanValues.\n\n' + 'Name File: '+array[-1])
            plt.tight_layout()
            plt.show()
        
        else:
            print("-------------------------------------------------")
            print('WARNING!!! -> Valor del argumento fuera de rango.')
            print("-------------------------------------------------")
       
    def plotColumnsMenorConCorte(self,i,corte):
        '''
            DESCRIPCION: 
                Muestra un grafica con los porcentaje sobre cada columna, 
                menores al % que se le pasa por parámetro hasta 0%,
                de NaN Values en el DataSet. Ordenados de mayor a menor. 
                Mostrando el nombre de la columna. Además se dibuja sobreponiendo 
                una función horizontal que se encuentra a una altura del corte 
                que se le pasa por parámetro. Por ejemplo, un 50%. 
                
                (IMPLEMENTADA)
        ''' 
        #Separacion de la ruta. Last element of array, name file
        array = self.path.split('\\')
        
        t = self.dataSet.shape[0] #Numero de columnas.
        
        porc_NaNValues = ((self.dataSet.isnull().sum())/t)*100
        
        n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.
        
        porc_NaNValues_order = n.sort_values(ascending=False)
        
        vector = porc_NaNValues_order[porc_NaNValues_order>30] #Datos X
        
        labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y
        
        
        if (0<=i) and (100>=i):
            plt.style.use('seaborn')
            vector = porc_NaNValues_order[porc_NaNValues_order<i] #Datos X
            labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y
            
            objects = labels
            y_pos = np.arange(len(objects))
            performance = vector
             
            plt.bar(y_pos, performance, align='center', alpha=0.5,)
            plt.xticks(y_pos, objects,rotation='vertical')
            plt.ylabel('% de NanN Values\n por columna.')
    
            plt.plot(np.ones(len(labels))+(corte-1),'r--')
            
            font = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 20,
            }
            plt.text(len(labels)-5,corte+1,str(corte)+'%',fontdict=font)
            plt.tight_layout()
            plt.title(str(vector.size) + ' de 116 columnas con un porcentaje menor al ' + str(i) + '% de NanValues.\n\n' + 'Name File: '+array[-1])
            plt.tight_layout()
            plt.show() 
        else:
            print("-------------------------------------------------")
            print('WARNING!!! -> Valor del argumento fuera de rango.')
            print("-------------------------------------------------")
    
    
    def plotColumns(self, a, b):
       '''
           DESCRIPCION:    
               A partir de una lista (ordenada de mayor a menor) de NaN Values por 
               columnas. Muestra entre dos posiciones de la lista las columnas en forma gráfica.
               Posicion de la lista inicial 0 y mayor 115. La lista tiene 116 elementos.
               
               (IMPLEMENTADA PERO DAFALLOS A VECES Y NECESITA MEJORAR LA SALIDA POR PANTALLA)
       '''
       
        array = self.path.split('/')
        '''Busqueda de % de NaN values por columna.'''
            
        t = self.dataSet.shape[0] #Numero de columnas.
        
        porc_NaNValues = ((self.dataSet.isnull().sum())/t)*100
        
        n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.
        
        porc_NaNValues_order = n.sort_values(ascending=False)
        
        valores = pd.DataFrame(porc_NaNValues_order) #EXLCUSIVO PARA LA FUNCION  plotColumns(a, b)
        
        vector = porc_NaNValues_order[porc_NaNValues_order>30] #Datos X
        
        labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y
        
        if (0<=a) and (b<117) and (a<=b):
             
            
            #Nombre de las columnas
            objects = list(porc_NaNValues_order.index)
            
            y_pos = np.arange(len(objects[a:b]))
           
            #Valor de las columnas
            performance = valores.iloc[:,0]
            
            y = objects[a:b]#NombresDeColumnas.
            x = performance[a:b]
            print(len(y))
            plt.bar(y_pos, x, align='center', alpha=0.8,color='blue')
            plt.style.use('seaborn')
            plt.xticks(y_pos, y,rotation='vertical')
            plt.ylabel('% de NanN Values\n por columna.')
            if b == performance.size :#Controla el ultimo caso.
                plt.title('Columnas entre ' + str(performance[a])+ "% y " + str(performance[b-1]) + "% de NaN Values.\n" + "Name file: " + array[-1])
            else:
                plt.title('Columnas entre ' + str(performance[a])+ "% y " + str(performance[b]) + "% de NaN Values.\n" + "Name file: " + array[-1])              
            
               #plt.style.use('matplotlibrc')
           
            plt.ylim([0,100])
           
            
            plt.tight_layout()
            plt.show()
            
        else:
            print("---------------------------------------------------------------")
            print('WARNING!!! -> Valor del argumento fuera de rango o valor a < b.')
            print("---------------------------------------------------------------")