##FUNCIONES DEL PUNTO 10 AL 18
from funciones_modulo import *
from funciones_proyecto import *

def poblacion_mas_baja():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        limpiar_terminal()
        print(f"""
========================================================================================================
                        📋 LISTADO DE {pais.upper()} POBLACION MAS BAJA
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
            min_valor = min(lista_pobla)
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["valor"] == min_valor:
                    print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
                    break    
            if i["pais"] != pais: 
                print(f"❌ El pais {pais} no esta en la lista o en el rango")
            print("="*105)
            print(input("Ingrese ENTER PARA CONTINUAR..."))
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
#----------------------------------------NUMERO DE REGISTROS--------------------------------------------------------
def numero_registros_por_ano():
    try:
        limpiar_terminal()
        while True:
            registros_por_ano = {}

            for i in leer_json("poblacion.json"):
                ano = i["ano"]

                if ano in registros_por_ano:
                    registros_por_ano[ano]['conteo'] += 1  
                else:
                    registros_por_ano[ano] = {
                        'ano': ano,         
                        'conteo': 1,        
                    }

            print(f"{'Año'.ljust(6)} | {'Número de registros'.ljust(20)}")
            print("-" * 60)

            for ano, data in registros_por_ano.items():
                print(f"{str(data['ano']).ljust(6)} | {str(data['conteo']).ljust(20)}")

            input("Ingrese ENTER PARA CONTINUAR")
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
#------------------------------------------------------------CRECIMIENTO 2%--------------------------------------------------------
def porcentaje_crecimiento2():
    try:
        año = int(input("Ingrese el año de inicio: "))
        año2 = int(input("Ingrese el año de fin: "))
        limpiar_terminal()
        if año > año2:
            print("❌ El año de fin debe ser mayor o igual al año de inicio.")
            input("\n🔄 Presiona ENTER para volver al menú...")
            return
        print("=" * 105)
        print(f"📋 PORCENTAJE DE CRECIMIENTO ({año}-{año2})".center(105))
        print("=" * 105)
        while True:
            crecimiento_paises = {}
            for i in  leer_json("poblacion.json"):
                pais =i["pais"]
                ano = i["ano"]
                poblacion = i["valor"]

                if año <= ano <= año2:
                    if pais not in crecimiento_paises:
                        crecimiento_paises[pais] = {}
                    crecimiento_paises[pais][ano] = poblacion

            paises_con_alto_crecimiento = []

            for pais, valores in crecimiento_paises.items():
                anos_disponibles = sorted(valores.keys())

                if len(anos_disponibles) < 2:
                    continue  # Si no hay suficientes datos, pasamos al siguiente país

                # Obtener la población del año inicial y final
                pop_inicio = valores[anos_disponibles[0]]
                pop_fin = valores[anos_disponibles[-1]]

                # Calcular tasa de crecimiento promedio anual
                tasa_crecimiento = ((pop_fin - pop_inicio) / pop_inicio) * 100 / (anos_disponibles[-1] - anos_disponibles[0])

                if tasa_crecimiento > 2:
                    paises_con_alto_crecimiento.append((pais, round(tasa_crecimiento, 2)))

            if paises_con_alto_crecimiento:
                for pais, crecimiento in paises_con_alto_crecimiento:
                    print(f"🌍 País: {pais}\n   📈 Crecimiento promedio: {crecimiento}% anual")
                    print("-" * 80)
            else:
                print(f"⚠️ No se encontraron países con un crecimiento poblacional superior al 2% en el rango {año} - {año2}.")

            input("Ingrese ENTER para continuar...")
            break
    except ValueError:
        print("❌ Error: Entrada inválida. Asegúrese de ingresar números.")
        input("\n🔄 Presione ENTER para volver al menú...")
    except KeyboardInterrupt:
        print("\n❌ Operación interrumpida por el usuario.")
        input("\n🔄 Presione ENTER para volver al menú...")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        input("\n🔄 Presione ENTER para volver al menú...")
#------------------------------------------POBLACION SUPERIO A 1.000M-----------------------------------------------
def poblacion_mayor():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        cantidad = int(input("Ingrese la cantididad minima de habitantes: "))
        limpiar_terminal()
        print(f"""
=========================================================================================================
                   📋 LISTADO DE {pais.upper()} SUPERIOR {cantidad} MILLONES DE HABITANTES
=========================================================================================================
    """)
        print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
        print("-" * 105)
        while True: 
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["valor"] >= cantidad : #VALIDACIONES
                    print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")    
            if i["pais"] != pais and i["valor"] < cantidad: #PARTE NEGATIVA DEL FOR  
                print(f"❌ El pais {pais} no esta en la lista o en el rango")
            print("="*105)
            print(input("Ingrese ENTER PARA CONTINUAR..."))
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
#-----------------------------Mostrar todos los paises en un año especifico----------------------------------------------
def año_especifico():
    try:
        año = int(input("Escribe el año a buscar: "))
        limpiar_terminal()
        print(f"""
========================================================================================================
                                📋 LISTADO DE TODOS LOS PAISES EN ({año})
========================================================================================================
    """)
        print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
        print("-" * 105)
        while True:
            for i in leer_json("poblacion.json"):
                if i["ano"] == año:
                    print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")

            print("="*105)
            print(input("Ingrese ENTER PARA CONTINUAR..."))
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
#---------------------------------POBLACION MENOS REGISTRADA--------------------------------------------------------
def poblacion_menos_rango():
    limpiar_terminal()
    pais = input("Ingrese el pais a buscar: ").capitalize()
    año = int(input("Ingrese la cantidad de años a analizar (por ejemplo, 20 o 40): "))
    ultimos_años = 2024 - año
    print(f"""
========================================================================================================
                             📋 LISTADO DE PAISES EN LOS ULTIMOS {año} AÑOS 
========================================================================================================
""")
    print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
    print("-" * 105)
    lista_pobla = []
    valor = 0
    for i in leer_json("poblacion.json"):
        if i["pais"] == pais and i["ano"] > ultimos_años:
            valor = i['valor'] 
            lista_pobla.append(valor)
    
    min_valor = min(lista_pobla)
    for i in leer_json("poblacion.json"):
        if i["ano"] > ultimos_años and i["pais"] == pais and i["valor"] == min_valor:
            print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
    print("="*105)
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#----------------------------------------PROMEDIO POBLACION REGISTRADA-------------------------------------------------------
def promedio_poblacion():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        ano = int(input("Escriba el año de inicio: "))
        anof = int(input("Escriba el año de fin: "))
        n = anof - ano 
        poblacion = []
        limpiar_terminal()
        if anof < ano:
            print("❌ El año de fin debe ser mayor o igual al año de inicio.")
            input("\n🔄 Presiona ENTER para volver al menú...")
            return 
        print("=" * 105)
        print(f"📋 PROMEDIO POBLACION DE {pais.upper()} ENTRE LOS AÑOS ({ano}-{anof})".center(105))
        print("=" * 105)
        while True:
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["ano"] >= ano and i["ano"] <= anof:
                    poblacion.append(i["valor"])
            promedio = sum(poblacion) / len(poblacion)
            resultado = round(promedio)
            print(f"El promedio del pais 🌍 {pais} en un rango de {n} años es:  {resultado}")
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
#---------------------------------Cantidad de años con datos de población disponibles para India.-------------------------------------------------
def disponibles():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        limpiar_terminal()
        while True:
            anos_disponibles = set()

            for i in leer_json("poblacion.json"):
             if i["pais"] == pais and i["estado"] == "disponible":
                anos_disponibles.add(i["ano"])
            
            cantidad_anos = len(anos_disponibles)

            if cantidad_anos == 0:
                print(f"⚠️ No se encontraron datos de población disponibles para {pais}.")
            else:
                print(f"{'Año'.ljust(6)} | {'Número de registros'.ljust(20)}")
                print("-" * 60)

                print(f"PAIS: {pais}\nAÑOS CON CANTIDAD DISPONIBLE: {cantidad_anos}\nAÑOS REGISTRADOS: {sorted(anos_disponibles)}")

                input("Ingrese ENTER PARA CONTINUAR")
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
#-------------------------------------------Listar los países con datos de población disponibles para cada año entre 2000 y 2023.-----------------------
def poblacion_disponible():
    try:
        año = int(input("Ingrese el año de inicio: "))
        año2 = int(input("Ingrese el año de fin: "))
        limpiar_terminal()
        if año > año2:
            print("❌ El año de fin debe ser mayor o igual al año de inicio.")
            input("\n🔄 Presiona ENTER para volver al menú...")
            return
        print("=" * 70)
        print(f"📋 PAISES CON DATOS DE POBLACION DISPONIBLES ({año}-{año2})".center(70))
        print("=" * 70)
        while True:
            paises_ano = {}
            for i in  leer_json("poblacion.json"):
                pais =i["pais"]
                ano = i["ano"]
                poblacion = i["valor"]

                if año <= ano <= año2:
                    if ano not in paises_ano:
                        paises_ano[ano] = set()
                    paises_ano[ano].add(pais)

            for ano in sorted(paises_ano.keys()):
                paises_lista = ", ".join(sorted(paises_ano[ano]))
                print(f"{str(ano).ljust(6)} | {paises_lista}")

            print("=" * 70)
            input("\n🔄 Presiona ENTER para volver al menú...")
            break
    except ValueError:
        print("❌ Error: Entrada inválida. Asegúrese de ingresar números.")
        input("\n🔄 Presione ENTER para volver al menú...")
    except KeyboardInterrupt:
        print("\n❌ Operación interrumpida por el usuario.")
        input("\n🔄 Presione ENTER para volver al menú...")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        input("\n🔄 Presione ENTER para volver al menú...")
