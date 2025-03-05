#Funciones para el modulo de reportes del proyecto
from funciones_proyecto import *
from funciones_modulo import *
from funciones_modulo2 import *
from funciones_modulo3 import *
opciones = {
            "1": datos_india_2020_2023, "2": listar_paises, "3": listar_SPPOPTOTL, "4": listar_todos_los_paises,
            "5": india_2022, "6": poblacion_2000, "7": poblacion_2010, "8": porcentaje_crecimiento, "9": pais_2023,
            "10": poblacion_mas_baja, "11": numero_registros_por_ano, "12": porcentaje_crecimiento2, "13": poblacion_mayor,
            "14": año_especifico, "15": poblacion_menos_rango, "16": promedio_poblacion, "17":disponibles, "18": poblacion_disponible,
            "19": poblacion_especifica, "20": mayor, "21": decadas, "22": pais_20,"23": años_sin_datos, "24": poblacion_mas_alta, "25": ultima_funcion
            }

def menu_reportes():
    while True:
        limpiar_terminal()
        try:
#------------------------------------------------MENU PRINCIPAL-------------------------------------------------------
            print("""
==================================================================================================
                                    📊 MÓDULO DE REPORTES  
==================================================================================================
1.  Consultar datos de población dentro de un rango de tiempo.  
2.  Listar países con sus códigos ISO e SO3.  
3.  Obtener datos de población para el indicador 'SP.POP.TOTL'.  
4.  Consultar datos de población de los últimos X años para todos los países.  
5.  Consultar la población de un país en un año específico.  
6.  Obtener la población total de todos los países antes de un año determinado.  
7.  Consultar la población total registrada después de un año específico.  
8.  Calcular el porcentaje de crecimiento poblacional de un país en un período determinado.  
9.  Obtener la población de un país en un año específico (si los datos están disponibles).  
10. Identificar el año con la población más baja registrada para un país.  
11. Determinar el número de registros de población disponibles por año.  
12. Listar los países con un crecimiento poblacional superior al 2% dentro de un rango.  
13. Identificar los años en los que la población de un pais superó los X millones.
14. Obtener la población total registrada para todos los países en un año especifico.
15. Obtener la población menos registrada para un pais en los últimos X años.
16. Promedio de población registrada para un pais en un rango especifico.
17. Cantidad de años con datos de población disponibles para un pais.
18. Listar los países con datos de población disponibles para cada año en un rango especifico.
19. Consultar la población de un país en un año específico.
20. Años en los que la población de un pais creció X cantidad en comparación con el año anterior.
21. Población registrada de un pais en cada década desde X años.
22. Población total registrada para todos los países en un año especifico.
23. Años en los que no hay datos de población disponibles para India.
24. Año con la población más alta registrada para un pais.
25. Años con datos de población disponibles para más de 50 países.
0.  Volver al menú principal.  
==================================================================================================
""")
            opc = input("Ingrese la opcion a realizar: ")
            if opc in opciones:
                opciones[opc]()
            elif opc == "0":
                print("\n🔄 Regresando al menú principal...")
                input("Presiona ENTER para continuar...")
                break
            else:
                print("❌ Error: Opción inválida. Intenta de nuevo.")
                input("\n🔄 Presiona ENTER para volver al menú...")
#-----------------------------------------------EXCEPCION DE ERROES------------------------------------------------------
        except ValueError:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
        except KeyboardInterrupt:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
        except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\n🔄 Presiona ENTER para volver al menú...")
