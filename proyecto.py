# Instituto de Estadísticas Globales
from funciones_proyecto import *
from modulo_reportes import *
from funciones_modulo2 import *
#---------------------------------------DICCIONARIO PARA LLAMAR FUNCIONES---------------------------------------------
opciones = {"1":poblacion, "2": paises, "3": indicadores, "4":gestion_informes, "5": menu_reportes}
while True:
#------------------------------------------------MENU PRINCIPAL-------------------------------------------------------
    try:
        limpiar_terminal()
        print("""
==================================
📊 ESTADISTICAS GLOBALES
==================================
1. Registrar datos de poblacion.
2. Agregar o mostar paises. 
3. Agregar o mostar indicadores.
4. Gestion de informacion.
5. Módulo de Reportes.
0. Salir del programa.
==================================
    """)
#---------------------------------------LLAMAR FUNCIONES,SALIR,AVISO DE ERRORES AL INTRODUCIR-----------------------------
        opc = input("Ingrese la opciona a realizar: ")
        if opc in opciones:
            opciones[opc]()
        elif opc == "0":
            print("\n👋 Saliendo del sistema. ¡Hasta pronto!")
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
