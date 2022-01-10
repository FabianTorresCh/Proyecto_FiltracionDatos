"""
APUNTES DE ANOTACION SQL

SELECT
SQL:            SELECT column1, column2, column3 FROM BDtabla;
PYTHON:     BDtabla[["column1", "column2", "column3"]]
"""



# -----------------------------------------------------------
# IMPORT LIBRARY
import pandas as LibraryPandas
import os

# -----------------------------------------------------------
# VARIABLE

# VARIABLE DE INICIO DE PROGRAMA
ProgramRun = str()  # VARIABLE PROGRAM RUN

# ELEMENTOS DE LECTURA DE ARCHIVO
FileCsvDirection = str() # DIRECCION DE CARPETA DE ARCHIVO
FileCsvName = str() # NOMBRE DEL ARCHIVO
FileCsv = () # VARIABLE DE LECTURA .CSV
RegistroLog = int() # CANTIDAD DE FILAS
AbscisaMax = int() # ABSCISA MAXIMA O VALOR MAXIMO DE LA COLUMNA
AbscisaMin = int() # ABSCISA MINIMA O VALOR MINIMO DE LA COLUMNA


# VARIABLES DE CICLO DE VERIFICACION
AbscisaN1=int() # PRIMER REGISTRO
AbscisaN2=int() # SEGUNDO REGISTRO
AbscisaBoolean = int() # VALIDACION DE CONTENIDO DE LISTA
AbscisaContador=int() # NUEVO REGISTRO DE ABSCISA
AbscisaIntervalo = int(10) # INTERVALOS DE ABSCISA


# ELEMENTOS DE TABLAS
Columna_PK = str ("P.K.")
Columna_Desfase = str ("Desfase")
Columna_Ordenada = str ("Ordenada")
Columna_Abscisa = str ("Abscisa")
Columna_Elevacion = str ("Elevación")
Columna_Descripcion = str ("Descripción")


# -----------------------------------------------------------
# FUNCIONES


# -----------------------------------------------------------
# PROGRAM STRUCTURE
print("█ █ PROGRAMA ► ►")
print("FILTRACION DE COORDENADAS")

# PROGRAM START
while ProgramRun != "N" and ProgramRun != "n":

    ProgramRun = str("Y")
    os.system("cls") # LIMPIEZA DE PANTALLA


    # PROGRAM MENU
    if ProgramRun == "Y" or ProgramRun == "y":

        FileCsvDirection = str("D:\OneDrive\PROGRAMACION\PROJECT - COORDINATE FILTERING")
        print("\nDIRECION DE ARCHIVO: "+FileCsvDirection)

        FileCsvName = str("COORD - PRUEBA")
        print("\nNOMBRE DE ARCHIVO: "+FileCsvName)

        FileCsvFormato = str(".CSV")
        print("\nEXTENCION DE ARCHIVO: "+FileCsvFormato)

        FileCsvDirectionFull = str(FileCsvDirection+"\\"+FileCsvName+FileCsvFormato)
        print("\nDIRECCION TOTAL: "+FileCsvDirectionFull)

        FileCsv = LibraryPandas.read_csv(FileCsvDirectionFull,header=0)
        print("\nVARIABLE DE ARCHIVO: FileCsv")

        RegistroLog = len(FileCsv)
        print("\nNUMERO DE REGISTROS: ", RegistroLog)

        AbscisaMax = FileCsv["PK"].max()
        print("\nVALOR MAXIMO: ", AbscisaMax)

        AbscisaMin = FileCsv["PK"].min()
        print("\nVALOR MINIMO: ", AbscisaMin)




        print("\n-----------------------------------------------------------------------------")
        print("TABLA DE COORDENADAS ORIGINAL - FILAS 70 A LA 90")
        print(FileCsv[70:90])
        print("-----------------------------------------------------------------------------")

        # CREACION DE COLUMNA DE COCIENTE
        # IMPLEMENTACION DE COCIENTE/RESIDUO 0 CON DIVISOR IGUAL A 10
        FileCsv["COCIENTE"] = FileCsv["PK"]%10


        FileCsv=FileCsv[FileCsv["COCIENTE"] == 0.00]    # MUESTRA FILAS CON VALOR 0 EN LA COLUMNA DE COCIENTE


        FileCsv=FileCsv.drop_duplicates("PK") # ELIMINA FILAS CON VALOR DUPLICADOS DE LA COLUMNA DE PK, EL VALOR QUE PERMANECE ES EL PRIMER VALOR

        # ORDENAR TABLA POR PK
        FileCsv=FileCsv.sort_values("PK")


        """ NOTA IMPORTANTE
        METODO PARA REALIZAR LA VALIDACION DE DATOS FALTANTE
        
        MEDIANTE UN CICLO, REALIZARA BUSQUEDAS Y VERIFICARA EXISTENCIA DE DATO
        1. SE DEBERA ASIGNAR A UNA VARIABLE (VAR1), EL DATO MINIMO DE LA COLUMNA PK (VAR1 COMO VARIABLE CONTADOR)Y ASIGNAR A UNA VARIABLE (VAR2) EL DATO MAXIMO DE LA COLUMNA PK
        2. CON LA VARIABLE (VAR1) SE REALIZARA EL CILO, SUMANDO 10 POR CADA CICLO HASTA LLEGAR AL MAXIMO VALOR (VAR2), CERRANDO EL CLICLO
        3. POR CADA CICLO SE REALIZARA LO SIGUIENTE
        3.1 VALIDACION DEL DATO EXISTENTE CON UNA VARIABLE DE TIPO BOOLEANO (VAR3) REALIZANDO BUSQUEDA
        3.2 SI EL DATO SE ENCUENTRA Y (VAR3) ES VERDADERO, SE REALIZARA UNA ADICION DE 10 A LA (VAR1), REPITIENDO EL CICLO
        3.3 SI EL DATO NO SE ENCUENTRA Y (VAR3) ES FALSO, SE DEBERA AGREGAR UNA FILA CON EL VALOR DE VAR1 EN LA COLUMNA PK, REASIGNANDO A VAR1 EL VALOR MINIMO DE LA COLUMNA PK, SE REALIZARA LA REORDENA LA LISTA.
        3.4 AL REASIGNAR EL VALOR DE MINIMO DE LA COLUMNA PK A VAR1, INDICA QUE REINICIARA LA VERIFICACION DE LA LISTA
        
        """

        print("XXX TIPO DE LISTA: ",type(FileCsv) )

        AbscisaContador=AbscisaMin
        while (AbscisaContador <= AbscisaMax):

            AbscisaN1 = FileCsv[FileCsv["PK"] == AbscisaContador]
            AbscisaBoolean=len(AbscisaN1)

            if(AbscisaBoolean!=0):
                AbscisaN1 = float(AbscisaN1["PK"])
                print(">>> ABSCISA ENCONTRADA: ",AbscisaN1)
                AbscisaContador = AbscisaContador+AbscisaIntervalo
            else:
                print("+++ ABSCISA FALTANTE: ",AbscisaContador)
                nueva_fila = {'PK':AbscisaContador, 'DESFASE': 0, 'NORTE':0, 'ESTE':0, 'ELEVACION':0, 'DESCRIPCION':'-','COCIENTE':0}
                FileCsv = FileCsv.append(nueva_fila, ignore_index=True)
                print("VALIDACION DE AGREGADO: ",FileCsv[FileCsv["PK"] == AbscisaContador])
                AbscisaContador=AbscisaMin
                FileCsv = FileCsv.sort_values("PK")



        """
        print("LABORATORIO")
        # ENCUENTRA LA FILA CON EN VALOR SELECCIONADO
        AbscisaN1=FileCsv[FileCsv["PK"] == 86900]
        print("VALOR DE BUSQUEDA",len(AbscisaN1))
        # SOBRE-ESCRITURA DE LA VARIABLE, SE FORZA EL CAMBIO DE LA VARIABLE DE TIPO LISTA A FLOAT
        # CON EL VALOR SELECCIONADO SEGUN LA COLUMNA INDICADA
        AbscisaN1=float(AbscisaN1["PK"])
        print("DATO 1: ",AbscisaN1) # VERIFICACION DE EL DATO
        """


        # -------------------------------------------
        print("\nVERIFICACION DE CAMBIO REALIZADO")
        print(FileCsv[FileCsv["PK"] == AbscisaMin])

        # -------------------------------------------
        # VALIDACION DE EELEMENTOS
        # PROCESO DE IDENTIFICACION DE DATOS FALTANTES



        # TABLA FILTRADA
        #FileCsv = FileCsv.sort_values("PK")
        print("\n\n-----------------------------------------------------------------------------")
        print("TABLA DE COORDENADAS FILTRADA - FILAS 0 AL 9")
        print(FileCsv[0:10])
        print("\n-----------------------------------------------------------------------------")
        print("TABLA DE COORDENADAS FILTRADA - FILAS 67 AL 75")
        print(FileCsv[67:75])


        print("\n-----------------------------------------------------------------------------")
        print("TABLA DE COORDENADAS FILTRADA - FULL")
        print(FileCsv)

        FileCsv=FileCsv[["PK", "DESFASE", "NORTE", "ESTE", "ELEVACION", "DESCRIPCION"]]
        print("EXPORTAR ARCHIVO")
        FileCsv.to_csv(FileCsvName+" - (FILTRADO)"+FileCsvFormato,index=False)








        ProgramRun = str("N")

    # -----------------------------------------------------------
    # VALOR DIFERENTE DE Y / y
    elif ProgramRun != "Y" or ProgramRun != "y":
        print("ERROR DE VALOR >> INGRESE NUEVO VALOR")
        print("VALORES ADMITIDOS >> Y / y / N / n")
    # -----------------------------------------------------------
    # VALOR DE CIERRE DE PROGRAMA
    elif ProgramRun == "N" and ProgramRun == "n":
        print("█ █ PROGRAMA ► ► PROGRAMA CERRADO")  # CIERRE DE PROGRAMA
# PROGRAM CLOSED
print("█ █ PROGRAMA ► ► PROCESO TERMINADO", end="")  # CIERRE DE PROGRAMA
