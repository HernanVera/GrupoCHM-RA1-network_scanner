<<<<<<< HEAD
import subprocess
import socket

# 1. Función para hacer ping a un equipo
def ping(host):
    comando = ["ping", "-n", "1", "-w", "500", host]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    if resultado.returncode == 0:
        return True
    else:
        return False

# 2. Función para barrer la red buscando equipos activos
def ping_sweep(red_base):
    hosts_activos = []
    print(f"\nIniciando escaneo rápido en la red {red_base}X ...")
    
    for numero in range(1, 255):
        ip_objetivo = f"{red_base}{numero}"
        if ping(ip_objetivo):
            print(f"[+] Equipo activo encontrado: {ip_objetivo}")
            hosts_activos.append(ip_objetivo)
            
    return hosts_activos

# 3. Función para revisar si una puerta (puerto) está abierta
def scan_port(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        resultado = s.connect_ex((host, port))
        if resultado == 0:
            return True
        else:
            return False
    except:
        return False
    finally:
        s.close()

# 4. Función para escanear una lista de puertos
def port_scan(host, ports, timeout=1):
    puertos_abiertos = []
    print(f"\nEscaneando puertos en el equipo {host}...")
    
    for puerto in ports:
        if scan_port(host, puerto, timeout):
            print(f"    [+] Puerto {puerto} está ABIERTO 🔓")
            puertos_abiertos.append(puerto)
            
    return puertos_abiertos

# ==========================================
# BLOQUE DE EJECUCIÓN 
# ==========================================
if __name__ == "__main__":
    print("--- INICIANDO ESCÁNER DE RED INACAP ---")
    
    # Esta es tu red base (según lo que vimos en tu terminal)
    mi_red = "192.168.1." 
    
    # Ejecutamos el barrido de red (sin comillas en la variable)
    equipos_activos = ping_sweep(mi_red)
    
    # Si encontramos equipos, escaneamos los puertos del primero
    if equipos_activos:
        primer_equipo = equipos_activos[0]
        puertos_a_revisar = [21, 22, 80, 443] 
        port_scan(primer_equipo, puertos_a_revisar)
    else:
        print("No se encontraron equipos activos en esta red.")
=======
import socket    # Para hablar con otros computadores
import os        # Para usar el comando 'ping'
import argparse  # Para que el usuario elija qué IP escanear

# Configuramos el menú de opciones
parser = argparse.ArgumentParser(description="Escáner de Red - INACAP")
parser.add_argument("-t", "--target", help="IP a escanear")
args = parser.parse_args()
>>>>>>> ab2e002339a82f425667492e78b407b4dfb7cfb7
