from funciones_proyecto import limpiar_terminal, leer_json
#-------------------------------------FUNCION PARA MOSTRAR LOS DATOS DE INDIA 2000-2023----------------------------------
def datos_india_2020_2023():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        ano = int(input("Escriba el año de inicio: "))
        anof = int(input("Escriba el año de fin: "))
        n = anof - ano
        limpiar_terminal()
        if anof < ano:
            print("❌ El año de fin debe ser mayor o igual al año de inicio.")
            input("\n🔄 Presiona ENTER para volver al menú...")
            return
        print("=" * 105)
        print(f"📋 DATOS POBLACION {pais.upper()} ({ano}-{anof})".center(105))
        print("=" * 105)
        print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")
        print("-" * 105)
        datos_filtrados = []
        while True:
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["ano"] >= ano and i["ano"] <= anof:
                    datos_filtrados.append(i)
            for i in datos_filtrados[:n+1]:
                print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
                print("-"*105)
            if  i["pais"] != pais and i["ano"] >= ano and i["ano"] <= anof:
                print(f"❌ El pais {pais} no esta en la lista o en el rango")
                break
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
#-----------------------------------------------Funcion para listar paises--------------------------------------------
def listar_paises():
    limpiar_terminal()
    print("""
=======================================================
                📋 LISTADO DE PAISES 
=======================================================
""")
    print(f"{'🌍 PAÍS':<20}| {'🔤 CÓDIGO ISO':<12}| {'🔤 CÓDIGO ISO3':<12}")  
    print("=" * 54)
    for i in leer_json("paises.json"):
        print(f"{i['nombre']:<20} | {i['codigo_iso']:<12} | {i['codigo_iso3']:<12}")
    print("=======================================================")
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#-----------------------------------------------LISTAR SEGUN EL INDICADOR SP.POP.TOTL-------------------------------------
def listar_SPPOPTOTL():
    limpiar_terminal()
    print("""
========================================================================================================
                                📋 LISTADO DE PAISES (SP.POP.TOTL)
========================================================================================================
""")
    print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
    print("-" * 105)
    for i in leer_json("poblacion.json"):
        if i["indicador_id"] == "SP.POP.TOTL":
            print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
    print("="*105)
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#-------------------------------------------LISTAR TODOS LOS PAISES HACE 10 AÑOS ----------------------------------------
def listar_todos_los_paises():
    año = int(input("Ingrese la cantidad de años a analizar (por ejemplo, 20 o 40): "))
    ultimos_años = 2024 - año
    limpiar_terminal()
    print(f"""
========================================================================================================
                                📋 LISTADO DE PAISES (ULTIMOS {año} AÑOS)
========================================================================================================
""")
    print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
    print("-" * 105)
    for i in leer_json("poblacion.json"):
        if i["ano"] >= ultimos_años:
            print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
    print("="*105)
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#-------------------------------------------POBLACION PARA INDIA AÑO 2022-------------------------------------------------
def india_2022():
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
#-----------------------------------------------POBLACION AÑO 2000--------------------------------------------------------------
def poblacion_2000():
    limpiar_terminal()
    año = int(input("Escribe el año limite (Se mostraran todos los paises antes de ese año): "))
    print(f"""
========================================================================================================
                             📋 LISTADO DE PAISES ANTES DEL AÑO {año}
========================================================================================================
""")
    print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
    print("-" * 105)
    for i in leer_json("poblacion.json"):
        if i["ano"] < año:
            print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
    print("="*105)
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#-----------------------------------------------POBLACION AÑO 2010--------------------------------------------------------------
def poblacion_2010():
    limpiar_terminal()
    año = int(input("Ingrese un año (Se mostraran los paises registrados a partir de ese año): "))
    print(f"""
========================================================================================================
                                📋 LISTADO DE PAISES DESDE {año}
========================================================================================================
""")
    print(f"{'📅 Año'.ljust(6)} | {'🌍 País'.ljust(12)} | {'🔤 Código ISO3'.ljust(15)} | {'📜 Indicador'.ljust(15)} | {'👥 Población'.ljust(15)} | {'🏷️ Unidad '.ljust(10)} | {'🔎 Estado'.ljust(12)}")  
    print("-" * 105)
    for i in leer_json("poblacion.json"):
        if i["ano"] >= año:
            print(f"{i['ano']:<6}  |   {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
    print("="*105)
    print(input("Ingrese ENTER PARA CONTINUAR..."))
#---------------------------------------------------------------PORCENTAJE DE CREMICMIENTO------------------------------------------------------------------------------
def porcentaje_crecimiento():
#DATOS DEL USUARIO
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        año = int(input("Ingrese el año de inicio: "))
        año2 = int(input("Ingrese el año de fin: "))
        limpiar_terminal()
        if año > año2:
            print("❌ El año de fin debe ser mayor o igual al año de inicio.")
            input("\n🔄 Presiona ENTER para volver al menú...")
            return
#TABLA
        print("=" * 105)
        print(f"📋 PORCENTAJE DE CRECIMIENTO {pais.upper()} ({año}-{año2})".center(105))
        print("=" * 105)
#BUCLE PARA CALCULAR EL VALOR 
        while True:
            po_2010 = None
            po_2020 = None
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais:
                    if i["ano"] == año:
                        po_2010 = i["valor"]
                    elif i["ano"] == año2:
                        po_2020 = i["valor"]
            porcentaje = ((po_2020 - po_2010) / po_2010) * 100
            resultado = round(porcentaje, 2)
#CONTENIDO TABLA
            print(f"El porcentaje aproximado de crecimiento poblacional del pais 🌍 {pais} es:  {resultado}%")
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
    except TypeError:
                print(f"❌ Error inesperado: {e}")
                input("\n🔄 Presiona ENTER para volver al menú...")
#------------------------------------------------------POBLACION AÑO 2023------------------------------------------------------------------------------------------ 
def pais_2023():
    try:
        pais = input("Escribe el pais a buscar: ").capitalize()
        año = int(input("Escribe el año a buscar: "))
        limpiar_terminal()
#TABLA
        print(f"""
========================================================================================================
                            📊 DISPONIBILIDAD DE DATOS DE POBLACIÓN PARA {pais}
========================================================================================================
    """)
        while True:
            for i in leer_json("poblacion.json"):
                if i["pais"] == pais and i["ano"] == año and i["estado"] == "disponible": #VALIDACIONES
                    print(f"PAIS: {i['pais']:<6}\n AÑOS CON DATOS DISPONIBLES {i['pais']:<10}  |   {i['codigo_iso3']:<12}   |   {i['indicador_id']:<15}|  {i['valor']:<15} | {i['unidad']:<10}| {i['estado']:<12}")
                    break
#FOR FALSO
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