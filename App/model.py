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
    return catalog


def newBook (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    book = {"ID": row['ID'], "Severity":row['Severity'], "Start_Time":row['Start_Time']}
    return book

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['AccidentList']
    book = newBook(row)
    lt.addLast(books, book)

def addBookTree (catalog, row):
    """
    Adiciona libro al tree con key=title
    """
    book = newBook(row)
    #catalog['booksTitleTree'] = tree.put(catalog['booksTitleTree'], int(book['book_id']), book, greater)
    catalog['AccidentIDTree']  = tree.put(catalog['AccidentIDTree'] , book['ID'], book, greater)

def newYear (year, row):
    """
    Crea una nueva estructura para almacenar los libros por año 
    """
    yearNode = {"year":year, "ratingMap":None, "count":1,}
    yearNode['IDlist']= lt.newList()
    lt.addLast(yearNode['IDlist'],row['ID'])
    yearNode ['ratingMap'] = map.newMap(2001,maptype='PROBING')
    intRating = row['City']
    map.put(yearNode['ratingMap'],intRating, 1, compareByKey)
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
        intRating = row['City']
        ratingCount = map.get(yearNode['ratingMap'], intRating, compareByKey)
        if  ratingCount:
            ratingCount+=1
            map.put(yearNode['ratingMap'], intRating, ratingCount, compareByKey)
        else:
            map.put(yearNode['ratingMap'], intRating, 1, compareByKey)
    else:
        yearNode = newYear(year,row)
        catalog['yearsTree']  = tree.put(catalog['yearsTree'] , year, yearNode, greater)

# Funciones de consulta


def getBookTree (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return tree.get(catalog['booksTitleTree'], bookTitle, greater)

def rankBookTree (catalog, bookTitle):
    """
    Retorna la cantidad de llaves menores (titulos) dentro del arbol
    """
    return tree.rank(catalog['AccidentIDTree'], bookTitle, greater)

def selectBookTree (catalog, pos):
    """
    Retorna la operación select (titulos) dentro del arbol
    """
    return tree.select(catalog['booksTitleTree'], pos) 

def getBookByYearRating (catalog, year):
    """
    Retorna la cantidad de libros por rating para un año
    """
    yearElement=tree.get(catalog['yearsTree'], strToDate(year,'%Y'), greater)
    response=''
    if yearElement:
        ratingList = map.keySet(yearElement['ratingMap'])
        iteraRating=it.newIterator(ratingList)
        while it.hasNext(iteraRating):
            ratingKey = it.next(iteraRating)
            response += 'Rating '+str(ratingKey) + ':' + str(map.get(yearElement['ratingMap'],ratingKey,compareByKey)) + '\n'
        return response
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

