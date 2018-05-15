# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:04:41 2018

@author: Javier Carracedo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter




'''
#Lectura del dataset.

dataSet = pd.read_csv(r, encoding='latin',low_memory=False)


#Busqueda de % de NaN values por columna.
    
t = dataSet.shape[0] #Numero de columnas.

porc_NaNValues = ((dataSet.isnull().sum())/t)*100

n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.

porc_NaNValues_order = n.sort_values(ascending=False)

valores = pd.DataFrame(porc_NaNValues_order) #EXLCUSIVO PARA LA FUNCION  plotColumns(a, b)

vector = porc_NaNValues_order[porc_NaNValues_order>30] #Datos X

labels = list(porc_NaNValues_order.index[len(porc_NaNValues_order)-len(vector):len(porc_NaNValues_order)])#Datos Y
'''

'''######################################################################################################################'''
'''
    Muestra un grafica con los porcentaje sobre cada columna, menores al % que se le pasa por parámetro hasta 0%,
    de NaN Values en el DataSet. Ordenados de mayor a menor. Mostrando el nombre de la columna. Además se dibuja sobreponiendo una función horizontal
    que se encuentra a una altura del corte que se le pasa por parámetro. Por ejemplo, un 50%.
    
    :param i: Valor de tanto por ciento hasta le cual se quiere visualizar. Valor valido entre 0 y 100, ambos incluidos.
    :param i: Porcentaje para dibujar la barra horizontal de corte.
    Ejemplo de uso de funcion:   "plotColumnsMenor(30,15)", "plotColumnsMenor(10,5)", "plotColumnsMenor(60.6,30.6)", etc
    
'''
def plotColumnsMenorConCorte(i,corte,r):
    '''Estraccion del nombre del fichero para visualizarlo'''
    array = r.split('/')
    #Lectura del dataset.

    dataSet = pd.read_csv(r, encoding='latin',low_memory=False)
    
    
    '''Busqueda de % de NaN values por columna.'''
        
    t = dataSet.shape[0] #Numero de columnas.
    
    porc_NaNValues = ((dataSet.isnull().sum())/t)*100
    
    n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.
    
    porc_NaNValues_order = n.sort_values(ascending=False)
    
    valores = pd.DataFrame(porc_NaNValues_order) #EXLCUSIVO PARA LA FUNCION  plotColumns(a, b)
    
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
        plt.title(str(vector.size) + ' de 116 columnas con un porcentaje menor al ' + str(i) + '% de NanValues.\n\n' + 'Name File: '+array[4])
    else:
        print('Valor del argumento fuera de rango.')
   
    plt.tight_layout()
    plt.show()
'''######################################################################################################################'''


'''
    Muestra un grafica con los porcentaje sobre cada columna, menores al % que se le pasa por parámetro hasta 0%,
    de NaN Values en el DataSet. Ordenados de mayor a menor. Mostrando el nombre de la columna.
    
    :param i: Valor de tanto por ciento hasta le cual se quiere visualizar. Valor valido entre 0 y 100, ambos incluidos.
    
    Ejemplo de uso de funcion:   "plotColumnsMenor(30)", "plotColumnsMenor(10)", "plotColumnsMenor(60.6)", etc
    
'''
def plotColumnsMenorSinCorte(i,r):
    '''Estraccion del nombre del fichero para visualizarlo'''
    array = r.split('/')
    #Lectura del dataset.

    dataSet = pd.read_csv(r, encoding='latin',low_memory=False)
    
    
    '''Busqueda de % de NaN values por columna.'''
        
    t = dataSet.shape[0] #Numero de columnas.
    
    porc_NaNValues = ((dataSet.isnull().sum())/t)*100
    
    n = np.round(porc_NaNValues, decimals=2) #Redondeo a dos decimales.
    
    porc_NaNValues_order = n.sort_values(ascending=False)
    
    valores = pd.DataFrame(porc_NaNValues_order) #EXLCUSIVO PARA LA FUNCION  plotColumns(a, b)
    
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
       
        plt.title(str(vector.size) + ' de 116 columnas con un porcentaje menor al ' + str(i) + '% de NanValues.\n\n' + 'Name File: '+array[4])
    else:
        print('Valor del argumento fuera de rango.')
   
    plt.tight_layout()
    plt.show()
'''######################################################################################################################'''

'''######################################################################################################################'''
'''
    A partir de una lista (ordenada de mayor a menor) de NaN Values por columnas. Muestra 
    entre dos posiciones de la lista las columnas en forma gráfica.
    Posicion de la lista inicial 0 y mayor 115. La lista tiene 116 elementos.
    
    :param a: Posicion de la lista. Valores permitidos de 0 a 115 incluidos.
    :param b: Posicion de la lista (¡TOP a<b!). Valores permitidos de 1 a 116 incluidos.
    
    Ejemplo de uso de funcion:   "plotColumns(30, 70)", "plotColumns(30, 31)","plotColumns(0,116)", etc
    
'''
def plotColumns(a, b,r):
    '''Estraccion del nombre del fichero para visualizarlo'''
    array = r.split('/')
    #Lectura del dataset.

    dataSet = pd.read_csv(r, encoding='latin',low_memory=False)
    
    
    '''Busqueda de % de NaN values por columna.'''
        
    t = dataSet.shape[0] #Numero de columnas.
    
    porc_NaNValues = ((dataSet.isnull().sum())/t)*100
    
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
            plt.title('Columnas entre ' + str(performance[a])+ "% y " + str(performance[b-1]) + "% de NaN Values.\n" + "Name file: " + array[4])
        else:
            plt.title('Columnas entre ' + str(performance[a])+ "% y " + str(performance[b]) + "% de NaN Values.\n" + "Name file: " + array[4])              
        
           #plt.style.use('matplotlibrc')
       
        plt.ylim([0,100])
       
        
        plt.tight_layout()
        plt.show()
        
    else:
        print("Valores no validos para diseñar la grafica")
'''######################################################################################################################'''
