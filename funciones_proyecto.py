import os
import json
def leer_json(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as arch:
            return json.load(arch)
#-------------------------------------------Escribir en el JSON-------------------------------------------
def escribir_json(nombre_archivo, diccionario):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diccionario, archivo, indent=4)
#-----------------------------------Agregar diccionarios---------------------------------------------------
def agregar_diccionario_a_json(nombre_archivo, nuevo_diccionario):
    datos_existentes = leer_json(nombre_archivo)
    datos_existentes.append(nuevo_diccionario)
    escribir_json(nombre_archivo, datos_existentes)
#---------------------------------Funcion limpiar terminal----------------------------------------------
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  
#----------------------------------------------------------Funcion poblacion---------------------------------------------------------------------------------------------
def poblacion():
    while True:
        limpiar_terminal()
        print("""
=======================================================
        📊 RESGISTRO DE DATOS DE POBLACION
=======================================================
              """)
        try: #Verificar errores
            año = int(input("📅 Escribe el año a registrar: "))
#----------------------------Bucle para validacion de unicamente caracteres-------------------------------------------------
            while True:
                pais = str(input("🌍 Escribe el pais a registrar: ")).capitalize()
                if pais.replace(" ", "").isalpha():
                    break
                print("❌ Error: El país solo debe contener letras. Intenta nuevamente.")
            while True:
                codigo_iso3 = str(input("🔤 Escriba el codigo ISO3 del pais (Ejemplo: 'BRA'): ")).upper()
                if codigo_iso3.replace(" ", "").isalpha() and len(codigo_iso3) == 3: 
                    break
                print("❌ Error: El codigo ISO debe tener exactamente 3 letras. Intenta nuevamente.")
            while True:
                indicador = str(input("📌 Escribe el indicador del pais (Ejemplo: 'SP.POP.TOTL'): ")).upper()
                indicador = "".join(i for i in indicador if i.isalpha())
                if len(indicador) == 9: 
                    nuevo_indicador =  f"{indicador[:2]}.{indicador[2:5]}.{indicador[5:]}"
                    break
                print("❌ Error: El indicador solo debe contener letras. Intenta nuevamente.")
            while True:
                descripcion_indicador = str(input("📜 Escriba la descripcion del indicador (Ejemplo: 'Población rural'): ")).capitalize()
                if descripcion_indicador.replace(" ", "").isalpha(): 
                    break
                print("❌ Error: La descripcion del indicador solo debe contener letras. Intenta nuevamente.")
            while True:
                try:
                    valor_poblacion = int(input("👥 Escriba el valor de la población: "))
                    break
                except ValueError:
                    print("El valor debe ser un numero entero positivo (+)")
            while True:
                estado_observacion = str(input("🔎 Escribe la disponibilidad (Ejemplo: 'Disponible'): ")).lower()
                if estado_observacion.replace(" ", "").isalpha(): 
                    break
                print("❌ Error: la disponibilidad solo debe contener letras. Intenta nuevamente.")
            while True:
                pregunta3  = input("🏷️ ¿Aplica unidad de medida? 1. (SI) 0. (NO) ")
                if pregunta3 == "1":
                    while True:
                        unidad_medida = str(input("    🏷️ Escriba la unidad de medida (Ejemplo: 'Rural'): ")).lower()
                        if unidad_medida.replace(" ", "").isalpha(): 
                            break
                        print("❌ Error: La unidad de medida solo debe contener letras. Intenta nuevamente.")
                    break
                elif pregunta3 == "0":
                    unidad_medida = "personas"
                    print("✅ Se asignó la unidad de medida predeterminada: 'personas'")
                    break
#---------------------------------------------CREACION DEL DICCIONARIO-------------------------------------------
            diccionario_poblacion = {
                "ano": año,
                "pais": pais,
                "codigo_iso3": codigo_iso3,
                "indicador_id": nuevo_indicador,
                "descripcion": descripcion_indicador,
                "valor": valor_poblacion,
                "estado": estado_observacion,
                "unidad": unidad_medida
            }
            agregar_diccionario_a_json("poblacion.json",diccionario_poblacion)
            print("✅ Los datos fueron agregados correctamente\n")
            print("=======================================================")
            print(input("Ingrese ENTER PARA CONTINUAR..."))
            limpiar_terminal()
            break
#---------------------------------------VALIDACION DE ERRORES---------------------------------------------------
        except IOError as e:
            print(f"❌ Ocurrio un error inesperado. {e}")
            input("\n🔄 Presiona ENTER para volver al intentarlo...")
        except KeyboardInterrupt:
            print("❌ Intente de nuevo, ha ocurrido un error")
            input("\n🔄 Presiona ENTER para volver al intentarlo...")
        except ValueError:
            print("❌ Intente de nuevo, ha ocurrido un error")
            input("\n🔄 Presiona ENTER para volver a intentarlo...")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            input("\n🔄 Presiona ENTER para volver al intentarlo...")
#-----------------------------------------FUNCION PARA PAISES, REGISTRO Y MUESTRA----------------------------------------
def paises():
    while True:
        limpiar_terminal()
        print("""
====================================
           🌍 PAISES 
====================================
1. Agregar un nuevo pais.
2. Mostrar los paises del sistema.
====================================
    """)
        try: 
            opc = input("Ingrese la opcion a realizar: ")
#----------------------------------------------REGISTRAR UN PAIS ---------------------------------------------
            if opc == "1":
                limpiar_terminal()
                while True:
                    print("""
=======================================================
                ➕ AGREGAR UN PAIS  
=======================================================
""")
                    pais = str(input("🌍 Escribe el pais a registrar: ")).capitalize()
                    if pais.replace(" ", "").isalpha():
                        break
                    print("❌ Error: El país solo debe contener letras. Intenta nuevamente.")
                while True:
                    codigo_iso = str(input("🔤 Escriba el codigo ISO del pais (Ejemplo: 'US'): ")).upper()
                    if codigo_iso.replace(" ", "").isalpha() and len(codigo_iso) == 2: 
                        break
                    print("❌ Error: El codigo ISO debe tener exactamente 2 letras. Intenta nuevamente.")
                while True:
                    codigo_iso3 = str(input("🔤 Escriba el codigo ISO3 del pais (Ejemplo: 'USA'): ")).upper()
                    if codigo_iso3.replace(" ", "").isalpha() and len(codigo_iso3) == 3: 
                        break
                    print("❌ Error: El codigo ISO debe tener exactamente 3 letras. Intenta nuevamente.")
#----------------------------------------------CREACION DEL DICCIONARIO--------------------------------------------------
                diccionario_paises = {
                "nombre": pais,
                "codigo_iso": codigo_iso,
                "codigo_iso3": codigo_iso3
                }
                agregar_diccionario_a_json("paises.json",diccionario_paises)
                print("✅ Los datos fueron agregados correctamente\n")
                print("=======================================================")
                input(("Ingrese ENTER PARA CONTINUAR..."))
                limpiar_terminal()
                limpiar_terminal()
#-----------------------------------------MOSTRAR TABLA DE LOS PAISES EN LA BASE DE DATOS-------------------------------
            elif opc == "2":
                limpiar_terminal()
                print("""
=======================================================
                📋 LISTADO DE PAISES 
=======================================================""")
                print(f"{'🌍 PAÍS':<20}| {'🔤 CÓDIGO ISO':<12}| {'🔤 CÓDIGO ISO3':<12}")  
                print("=" * 54)
                for i in leer_json("paises.json"):
                    print(f"{i['nombre']:<20} | {i['codigo_iso']:<12} | {i['codigo_iso3']:<12}")
                print("=======================================================")
                input("Ingrese ENTER PARA CONTINUAR...")
                limpiar_terminal()
                limpiar_terminal()
                break
#-----------------------------------------------VALIDACION DE ERRORES-----------------------------------------------------
        except IOError as e:
            print(f"❌ Ocurrio un error inesperado. {e}")
            break
        except KeyboardInterrupt:
            print("❌ Intente de nuevo, ha ocurrido un error")
            break
        except ValueError:
            print("❌ Intente de nuevo, ha ocurrido un error")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            break
#-------------------------------------------FUNCION INDICADORES----------------------------------------------------
def indicadores():
    while True:
        limpiar_terminal()
        print("""
======================================
           📌 INDICADORES 
======================================
1. Agregar un nuevo indicador.
2. Mostrar los indicadores en sistema.
======================================
    """)
        try:
            opc = input("Ingrese la opcion a realizar: ")
            if opc == "1":
                limpiar_terminal()
#----------------------------Bucle para validacion de unicamente caracteres-----------------------------------------------
                while True:
                    print("""
=======================================================
               ➕ AGREGAR UN INDICADOR
=======================================================
""")
                    indicador = str(input("📌 Escribe el indicador del pais (Ejemplo: 'SP.POP.TOTL'): ")).upper()
                    indicador = "".join(i for i in indicador if i.isalpha())
                    if len(indicador) == 9: 
                        nuevo_indicador =  f"{indicador[:2]}.{indicador[2:5]}.{indicador[5:]}"
                        break
                    print("❌ Error: El indicador solo debe contener un total de nueve letras. Intenta nuevamente.")
                while True:
                    descripcion_indicador = str(input("📜 Escriba la descripcion del indicador (Ejemplo: 'Población rural'): ")).capitalize()
                    if descripcion_indicador.replace(" ", "").isalpha(): 
                        break
                    print("❌ Error: La descripcion del indicador solo debe contener letras. Intenta nuevamente.")
#----------------------------------------------CREACION DEL DICCIONARIO--------------------------------------------------
                diccionario_indicadores = {
                     "id_indicador": nuevo_indicador,
                    "descripcion": descripcion_indicador
                }
                agregar_diccionario_a_json("indicadores.json",diccionario_indicadores)
                print("✅ Los datos fueron agregados correctamente\n")
                print("=======================================================")
                print(input("Ingrese ENTER PARA CONTINUAR..."))
#-----------------------------------------MOSTRAR TABLA DE LOS INDICADORES EN LA BASE DE DATOS-----------------------------
            elif opc == "2":
                limpiar_terminal()
                print("""
=========================================================
                📋 LISTADO DE INDICADORES 
=========================================================
""")
                print(f"{'🔤 ID INDICADOR':<15}| {'📜 DESCRIPCIÓN':<30}")  
                print("=" * 57)
                for i in leer_json("indicadores.json"):
                    print(f"{i['id_indicador']:<15} | {i['descripcion']:<30}")
                print("="*57)
                input("Ingrese ENTER PARA CONTINUAR...")
                break
#-----------------------------------------------VALIDACION DE ERRORES-----------------------------------------------------
        except IOError as e:
            print(f"❌ Ocurrio un error inesperado. {e}")
            break
        except KeyboardInterrupt:
            print("❌ Intente de nuevo, ha ocurrido un error")
            break
        except ValueError:
            print("❌ Intente de nuevo, ha ocurrido un error")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            break
#-------------------------------------------------GESTION DE INFORMES--------------------------------------------------------