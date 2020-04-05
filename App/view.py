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
import sys
import controller 
import csv
from ADT import list as lt
from ADT import orderedmap as tree
from DataStructures import listiterator as it
from ADT import map as map

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 6")
    print("1- Cargar información")
    print("2- Buscar libro por llave (titulo) ")
    print("3- Consultar cuántos accidentes ocurrieron antes de una fecha - (rank)")
    print("4- Estado con mayor cantidad de accidentes en una fecha dada (req 4)")
    print("5- Consultar la cantidad de Accidentes por severidad para una fecha dada (req2)")
    print("6- Consultar la cantidad de accidentes por rating para un rango de fechas(requerimiento 3 del reto 3)")

    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input('Seleccione una opción para continuar\n')
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            print("Recursion Limit:",sys.getrecursionlimit())
            catalog = initCatalog ()
            loadData (catalog)
            print ('Tamaño Lista accidentes cargados: ' + str(lt.size(catalog['AccidentList'])))
            print ('Tamaño árbol Accidentes por ID: ' + str(tree.size(catalog['AccidentIDTree'])))
            print ('Tamaño árbol accidentes por fecha : ' + str(tree.size(catalog['yearsTree'])))
            print ('Altura árbol por ID: ' + str(tree.height(catalog['AccidentIDTree'])))
            print ('Altura árbol por fecha: ' + str(tree.height(catalog['yearsTree'])))
        elif int(inputs[0])==2:
            title = input("Nombre del titulo a buscar: ")
            book = controller.getBookTree(catalog,title)
            if book:
                print("Libro encontrado:",book['title'],book['average_rating'])
            else:
                print("Libro No encontrado")
        elif int(inputs[0])==3:
            title = input("Fecha a buscar: ")
            rank = controller.rankBookTree(catalog,title) 
            print("Hay ",rank," accidentes antes del "+title)
        elif int(inputs[0])==4:
            fecha= input('ingrese la fehca de la forma %YYYY-%mm-%dd')
            estado= controller.getEstate(catalog,fecha)
            if estado:
                print(estado)
                print('el estado con mayor cantidad de accidentes en la fecha',fecha,'es ',str(estado['Estado']),'con ', str(estado['Accidentes'], 'accidentes.'))
            else:
                print("no se encontro estado ")
        elif int(inputs[0])==5:
            year = input("Ingrese la fecha a consultar:")
            response = controller.getBookByYearRating(catalog, year) 
            if response: 
                print(response)
            else:
                print("No se encontraron Accidentes para la fecha",year)
        elif int(inputs[0])==6:
            years = input("Ingrese los años desde y hasta (%YYYY-%mm-%dd %Y-%m-%dd):")
            counter = controller.getBooksCountByYearRange(catalog, years) 
            if counter:
                print("Cantidad de accidentes entre las fechas",years,":")
                lista=map.valueSet(counter)
                for i in range(1,lt.size(lista)):
                    print(lt.getElement(lista,i))
            else:
                print("No se encontraron accidentes para el rango de fechas",years)   
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    #sys.setrecursionlimit(11000)
    main()