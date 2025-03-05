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