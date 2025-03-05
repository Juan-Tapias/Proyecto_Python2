#FUNCIONES DE LA 19 A LA 25
from funciones_modulo import *
from funciones_proyecto import *

def poblacion_especifica():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        año = int(input("Escribe el año a buscar: "))
        limpiar_terminal()
        print(f"""
========================================================================================================
                                📋 LISTADO DE {pais.upper()} ({año})
========================================================================================================
    """)
        print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
        print("-" * 105)
        while True:
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["ano"] == año:
                    print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
                    break    
            if i["pais"] != pais and i["ano"] != año: 
                print(f"❌ El pais {pais} no esta en la lista o en el rango")
            print("="*105)
            input("Ingrese ENTER PARA CONTINUAR...")
            break
    except ValueError:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except KeyboardInterrupt:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\n🔄 Presiona ENTER para volver al menú...")
def mayor():
    limpiar_terminal()
    ano = int(input("Escribe el valor de la poblacion: "))
    try:
        india_poblacion = sorted(
            [i for i in leer_json("poblacion.json") if i["pais"] == "India"], key=lambda x: x["ano"]
        )

        print(f"\n📊 AÑOS EN LOS QUE LA POBLACIÓN DE INDIA CRECIÓ MÁS DE {ano} HABITANTES")
        print("=" * 70)
        print("🌍 País: India\n")

        while True:
            años_crecimiento = []

            for i in range(1, len(india_poblacion)):
                ano_actual = india_poblacion[i]["ano"]
                poblacion_actual = india_poblacion[i]["valor"]
                poblacion_anterior = india_poblacion[i - 1]["valor"]

                crecimiento = poblacion_actual - poblacion_anterior

                if crecimiento > ano:
                    años_crecimiento.append(ano_actual)

            if años_crecimiento:
                print("📅 Años con crecimiento superior a 1 millón de personas:")
                for año in años_crecimiento:
                    print(f"➡️ {año}")
            else:
                print("❌ No se encontraron años con crecimiento mayor a 1 millón.")
                
            print("=" * 70)
            input("Ingrese ENTER PARA CONTINUAR...")
            break
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'poblacion.json'.")
    except json.JSONDecodeError:
        print("❌ Error: El archivo 'poblacion.json' no tiene un formato JSON válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
def decadas():
    limpiar_terminal()    
    try:
        while True:
            pais = input("Escribe el pais a buscar: ").capitalize()
            decada = int(input("Escribe desde que decada quieres buscar los valores: "))
            if decada % 10 == 0:
                pais_poblacion = {i["ano"]: i["valor"] for i in leer_json("poblacion.json") if i["pais"] == pais}

                decadas = list(range(decada, 2030, 10))

                print(f"\n📊 POBLACIÓN REGISTRADA DE {pais} EN CADA DÉCADA DESDE {decada}")
                print("=" * 70)
                print(f"🌍 País: {pais}")

                for decada in decadas:
                    if decada in pais_poblacion:
                        print(f"📅 {decada}:  {pais_poblacion[decada]:,} personas")
                        input("Presiona ENTER PARA CONTINUA...")
                        break
                    else:
                        print(f"📅 {decada}:  ❌ Datos no disponibles")
                print("=" * 70)
            else: 
                print("❌ Error: Escribe una decada correcta ")

    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'poblacion.json'.")
    except json.JSONDecodeError:
        print("❌ Error: El archivo 'poblacion.json' no tiene un formato JSON válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def años_sin_datos():
    limpiar_terminal()
    try:
        while True:
            pais = input("Escribe el pais a buscar: ").capitalize() 
            anos_disponibles = {i["ano"] for i in leer_json("poblacion.json") if i["pais"] == pais and i["estado"] == "disponible"}

            if anos_disponibles:
                primer_ano = min(anos_disponibles)
                ultimo_ano = max(anos_disponibles)
                todos_los_anos = set(range(primer_ano, ultimo_ano + 1))

                anos_sin_datos = sorted(todos_los_anos - anos_disponibles)

                print(f"\n📊 AÑOS SIN DATOS DE POBLACIÓN DISPONIBLES PARA {pais}")
                print("=" * 70)
                print(f"🌍 País: {pais}")

                if anos_sin_datos:
                    for ano in anos_sin_datos:
                        print(f"❌ {ano}")
                else:
                    print("✅ Todos los años tienen datos disponibles.")
                print("\n⚠️ Estos años no tienen datos de población registrados en la base de datos.")
                print("=" * 70)
            else:
                print("❌ No hay registros de población para India en la base de datos.")
            input("Presiona ENTER PARA CONTINUA...")
            break
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'poblacion.json'.")
    except json.JSONDecodeError:
        print("❌ Error: El archivo 'poblacion.json' no tiene un formato JSON válido.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def poblacion_mas_alta():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        limpiar_terminal()
        print(f"""
========================================================================================================
                        📋 LISTADO DE {pais.upper()} POBLACION MAS ALTA
========================================================================================================
    """)
        print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
        print("-" * 105)
        while True:
            lista_pobla = []
            valor = 0
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais:
                    valor = i['valor'] 
                    lista_pobla.append(valor)

            # Obtiene el minimo valor de la lista_pobla
            max_valor = max(lista_pobla)
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["valor"] == max_valor:
                    print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
                    break    
            if i["pais"] != pais: 
                print(f"❌ El pais {pais} no esta en la lista o en el rango")
            print("="*105)
            input("Ingrese ENTER PARA CONTINUAR...")
            break
    except ValueError:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except KeyboardInterrupt:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\n🔄 Presiona ENTER para volver al menú...")

def ultima_funcion():
    try:
        limpiar_terminal()
        while True:
            registros_por_año = {}

            for i in leer_json("poblacion.json"):
                if i["estado"] == "disponible":
                    año = i["ano"]
                    pais = i["pais"]

                    if año not in registros_por_año:
                        registros_por_año[año] = set() 
                    registros_por_año[año].add(pais)

            años_con_mas_de_50 = sorted([año for año, paises in registros_por_año.items() if len(paises) > 50])

            print("\n📊 AÑOS CON DATOS DE POBLACIÓN PARA MÁS DE 50 PAÍSES")
            print("=" * 70)
            if años_con_mas_de_50:
                for año in años_con_mas_de_50:
                    print(f"✅ {año}")
            else:
                print("❌ No hay años con datos disponibles para más de 50 países.")

            print("=" * 70)
            input("Ingrese ENTER PARA CONTINUAR...")
            break
    except ValueError:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except KeyboardInterrupt:
                print("❌ Intente de nuevo, ha ocurrido un error")
                input("\n🔄 Presiona ENTER para volver al menú...")
    except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\n🔄 Presiona ENTER para volver al menú...")