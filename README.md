# 🔍 Network Scanner - Proyecto RA1 (Redes Avanzadas)

Este proyecto consiste en un escáner de red local desarrollado en **Python**. La herramienta permite descubrir dispositivos conectados en un segmento de red específico y realizar un mapeo de puertos TCP activos, proporcionando una funcionalidad similar a una versión simplificada de **Nmap**.

## 👥 Integrantes y Roles
El equipo de trabajo está compuesto por:

* **Hernán Vera** - *Líder de Proyecto* (Gestión de repositorio y coordinación).
* **Matias Peralta** - *Desarrollador* (Implementación de lógica en Python y Scapy).
* **Claudio Zambra** - *Documentador* (Redacción técnica y manuales de uso).

---

## 🚀 Funcionalidades Principales
* **Escaneo ARP:** Envía peticiones de difusión (broadcast) para obtener direcciones IP y MAC de equipos activos.
* **Escaneo de Puertos:** Verifica sockets TCP en puertos comunes (21, 22, 80, 443, 8080) para detectar servicios abiertos.
* **Reporte Organizado:** Muestra los resultados en una tabla clara dentro de la consola.

## 🛠️ Requisitos del Sistema

Para que el script funcione correctamente, asegúrate de tener instalado:

1. **Python 3.x**
2. **Librería Scapy:** ```bash
   pip install scapy
Npcap (Obligatorio en Windows): Es el controlador que permite a Python "hablar" con la tarjeta de red. Descárgalo en npcap.com.

Nota: Durante la instalación, marcar la casilla "Install Npcap in WinPcap API-compatible Mode".

📖 Instrucciones de Uso
[!IMPORTANT]
Privilegios de Administrador: El escaneo de red requiere acceso a nivel de socket crudo. Debes ejecutar Visual Studio Code o la Terminal como Administrador.

Clonar el proyecto:

Bash
git clone [https://github.com/HernanVera/GrupoCHM-RA1-network_scanner.git](https://github.com/HernanVera/GrupoCHM-RA1-network_scanner.git)
Configurar la red:
Edita el archivo escaneoredes.py y asegúrate de que la variable target_network coincida con tu red (ejemplo: 192.168.1.1/24).

Ejecutar:

Bash
python escaneoredes.py

⚠️ Aviso Legal
Este software ha sido creado con fines exclusivamente educativos para la asignatura de Redes Avanzadas. El uso de herramientas de escaneo en redes ajenas sin autorización previa puede ser ilegal. El equipo no se responsabiliza por el mal uso de esta herramienta.

© 2026 - Grupo CHM
5. Ve a **GitHub Desktop**, escribe el mensaje de "Commit" y dale a **Push origin**. 

¡Con esto el perfil de tu proyecto en GitHub se verá increíble!
