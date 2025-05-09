import subprocess
import re
def obtener_plan_activo():
    # Ejecutar el comando
    resultado = subprocess.run(["powercfg", "/getactivescheme"], capture_output=True, text=True)
    
    # Buscar el nombre del plan activo entre paréntesis
    import re
    match = re.search(r"\((.+)\)", resultado.stdout)
    if match:
        return match.group(1)
    return "No se pudo obtener el plan activo"

def cambio_eco():
    # Comando corregido para activar el plan Economizador
    resultado = subprocess.run(
        ["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"],
        capture_output=True,
        text=True
    )
    
    # Verificar si el comando se ejecutó correctamente
    if resultado.returncode == 0:
        return "Plan de energía cambiado a Economizador exitosamente."
    else:
        return f"Error al cambiar el plan de energía: {resultado.stderr}"
    
def cambio_equilibrado():
    # Comando corregido para activar el plan Economizador
    resultado = subprocess.run(
        ["powercfg", "/setactive", "381b4222-f694-41f0-9685-ff5bb260df2e"],
        capture_output=True,
        text=True
    )
    
    # Verificar si el comando se ejecutó correctamente
    if resultado.returncode == 0:
        return "Plan de energía cambiado a Equilibrado exitosamente."
    else:
        return f"Error al cambiar el plan de energía: {resultado.stderr}"
    
def cambio_alto_rendimiento():
    # Comando corregido para activar el plan Economizador
    resultado = subprocess.run(
        ["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"],
        capture_output=True,
        text=True
    )
    
    # Verificar si el comando se ejecutó correctamente
    if resultado.returncode == 0:
        return "Plan de energía cambiado a Alto Rendimiento exitosamente."
    else:
        return f"Error al cambiar el plan de energía: {resultado.stderr}"


def crear_maximo_rendimiento():
    base_max_rendimiento_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"

    # Crear el plan duplicando desde el GUID base
    resultado = subprocess.run(
        ["powercfg", "/duplicatescheme", base_max_rendimiento_guid],
        capture_output=True,
        text=True
    )
    
    if resultado.returncode == 0:
        return "Plan Máximo Rendimiento creado exitosamente."
    else:
        return f"Error al crear el plan Máximo Rendimiento: {resultado.stderr}"

# 2. Función para obtener el GUID del plan "Máximo Rendimiento"
def obtener_guid_maximo_rendimiento():
    # Ejecutar el comando para listar los planes de energía
    resultado = subprocess.run(
        ["powercfg", "/list"],
        capture_output=True,
        text=True,
        shell=True  # Agregado para mejor compatibilidad con Windows
    )
    
    # Verificar si el comando se ejecutó correctamente
    if resultado.returncode != 0:
        return None
    
    # Buscar el primer plan "Máximo rendimiento"
    for linea in resultado.stdout.splitlines():
        if "ximo rendimiento" in linea:
            partes = linea.split(":")
            guid = partes[1].split("(")[0].strip() if len(partes) > 1 else linea.split("(")[0].strip()
            return guid
    
    return None

# 3. Función para activar el plan de energía utilizando su GUID
def activar_plan_por_guid(guid):
    if not guid:
        return "No se proporcionó un GUID válido para activar."
    
    resultado = subprocess.run(
        ["powercfg", "/setactive", guid],
        capture_output=True,
        text=True
    )
    
    if resultado.returncode == 0:
        return "Plan de energía activado exitosamente."
    else:
        return f"Error al activar el plan de energía: {resultado.stderr}"