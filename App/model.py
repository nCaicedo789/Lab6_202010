"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import orderedmap as tree
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    catalog = {'booksTitleTree':None,'yearsTree':None,'booksList':None}
    #implementación de Black-Red Tree (brt) por default
    catalog['AccidentIDTree'] = tree.newMap ()
    catalog['yearsTree'] = tree.newMap ()
    catalog['AccidentList'] = lt.newList("ARRAY_LIST")
    catalog['yearsTree_rank']=tree.newMap()
    return catalog

def newTree_rank(row):
    fecha= strToDate(row['Start_Time'],'%Y/%m/%d %H:%M:%S')
    fecha_map={'fecha':fecha, 'Accidentes':1}
    return fecha

def addTree_rank(catalog, row):
    accidente= newTree_rank(row)
    tree.put(catalog['yearsTree_rank'],accidente['fecha'],accidente, greater)

def newAccident (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    book = {"ID": row['ID'], "Severity":row['Severity'], "Start_Time":row['Start_Time'], 'State':row['State']}
    return book

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['AccidentList']
    book = newAccident(row)
    lt.addLast(books, book)

def addBookTree (catalog, row):
    """
    Adiciona libro al tree con key=title
    """
    book = newAccident(row)
    #catalog['booksTitleTree'] = tree.put(catalog['booksTitleTree'], int(book['book_id']), book, greater)
    catalog['AccidentIDTree']  = tree.put(catalog['AccidentIDTree'] , book['ID'], book, greater)

def newYear (year, row):
    """
    Crea una nueva estructura para almacenar los libros por año 
    """
    yearNode = {"year":year, "ratingMap":None, "count":1,'severity':None, 'state':None}
    yearNode['severity']= {1:0, 2:0, 3:0, 4:0}
    sev= int(row['Severity'])
    yearNode['severity'][sev]+=1
    yearNode ['ratingMap'] = map.newMap(40009,maptype='PROBING')
    city = {'Ciudad':row['City'], 'Accidentes':1}
    map.put(yearNode['ratingMap'],city['Ciudad'], city, compareByKey)

    yearNode['state']= tree.newMap()
    estado= {'Estado':row['State'], 'Accidentes':1}
    tree.put(yearNode['state'],estado['Estado'], estado, greater)
    return yearNode

def addYearTree (catalog, row):
    """
    Adiciona el libro al arbol anual key=original_publication_year
    """
    yearText= row['Start_Time']
    if row['Start_Time']:
        yearText=row['Start_Time'][0:row['Start_Time'].index(' ')]     
    year = strToDate(yearText,'%Y-%m-%d')
    yearNode = tree.get(catalog['yearsTree'], year, greater)
    if yearNode:
        yearNode['count']+=1
        sev= int(row['Severity'])
        yearNode['severity'][sev]+=1
        city = row['City']
        ratingCount = map.get(yearNode['ratingMap'], city, compareByKey)
        if  ratingCount:
            ratingCount['Accidentes']+=1
        else:
            ciudad=  {'Ciudad':row['City'], 'Accidentes':1}
            map.put(yearNode['ratingMap'], ciudad['Ciudad'], ciudad, compareByKey)

        
        state= row['State']
        state_count= tree.get(yearNode['state'],state,greater)
        if state_count:
            state_count['Accidentes']+=1
        else:
            estado= {'Estado':row['State'], 'Accidentes':1}
            tree.put(yearNode['state'], estado['Estado'],estado,greater)
    else:
        yearNode = newYear(year,row)
        catalog['yearsTree']  = tree.put(catalog['yearsTree'] , year, yearNode, greater)

def cambio_de_llaves_valor(catalog,fecha):
    fecha= strToDate(fecha,'%Y-%m-%d')
    años= tree.valueSet(catalog['yearsTree'])
    new_tree= tree.newMap()

    for i in range (1, lt.size(años)):
        elemento=lt.getElement(años,i)
        estados= tree.valueSet(elemento['state'])
        for x in range(1,lt.size(estados)):
            lt.getElement(estados,x)
            tree.put(new_tree,elemento['Accidentes'], elemento, greater)

    años['state']= new_tree



# Funciones de consulta


def getBookTree (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return tree.get(catalog['booksTitleTree'], bookTitle, greater)

def rankBookTree (catalog, fecha):
    """
    Retorna la cantidad de llaves menores (titulos) dentro del arbol
    """
    fecha=fecha+' 00:00:00'
    fecha= strToDate(fecha,'%Y/%m/%d %H:%M:%S')
    return tree.rank(catalog['yearsTree_rank'], fecha, greater)

def selectBookTree (catalog, pos):
    """
    Retorna la operación select (titulos) dentro del arbol
    """
    return tree.select(catalog['booksTitleTree'], pos) 

def getBookByYearRating (catalog, year):
    """
    Retorna la cantidad de libros por rating para un año
    """
    año=strToDate(year,'%Y-%m-%d')
    yearNode= tree.get(catalog['yearsTree'],año,greater)
    if yearNode:
        sev=yearNode['severity']
        sev['total']= sev[1]+sev[2]+sev[3]+sev[4]
        return sev
    else:
        return None


def getBooksCountByYearRange (catalog, years):
    """
    Retorna la cantidad de libros por rating para un rango de años
    """
    
    startYear = strToDate(years.split(" ")[0],'%Y-%m-%d')
    endYear = strToDate(years.split(" ")[1],'%Y-%m-%d')
    yearList = tree.valueRange(catalog['yearsTree'], startYear, endYear, greater)
    counter = 0
    cities= map.newMap(40009,maptype='PROBING')
    if yearList:
        iteraYear=it.newIterator(yearList)
        while it.hasNext(iteraYear):
            yearElement = it.next(iteraYear)
            #print(yearElement['year'],yearElement['count'])
            counter += yearElement['count']
            keys= map.keySet(yearElement['ratingMap'])
            for i in range(1, lt.size(keys)):
                city_key= lt.getElement(keys,i)
                city= map.get(cities,city_key,compareByKey)
                if city:
                    city['Accidentes']+=1
                else:
                    ciudad={'ciudad':city_key, 'Accidentes':1}
                    map.put(cities,ciudad['ciudad'],ciudad,compareByKey)
        total={'total_Accidentes':counter}
        map.put(cities,'total',total,compareByKey)


        return cities
    return None

def Accidentes_estado_fecha(catalog, fecha):
    fecha= strToDate(fecha,'%Y-%m-%d')
    arbol_fecha= tree.get(catalog['yearsTree'],fecha,greater)
    estados= tree.valueSet(arbol_fecha['state'])
    for i in range(1,lt.size(estados)+1):
        respuesta= {'Estado':None, 'Accidentes':0}
        est= lt.getElement(estados,i)
        if respuesta['Accidentes']< est['Accidentes']:
            respuesta= est
    return respuesta


    



# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def compareByTitle(bookTitle, element):
    return  (bookTitle == element['title'] )

def greater (key1, key2):
    
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1

def strToDate(date_string, format):
    
    try:
        # date_string = '2016/05/18 13:55:26' -> format = '%Y/%m/%d %H:%M:%S')
        return datetime.strptime(date_string,format)
    except:
        return datetime.strptime('1900', '%Y')

