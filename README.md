# 🔍 Network Scanner - Proyecto INACAP (RA1)

Este proyecto consiste en un escáner de red local desarrollado en **Python**. La herramienta permite realizar un barrido de red (**Ping Sweep**) para detectar equipos activos y posteriormente ejecutar un **escaneo de puertos TCP** en los dispositivos encontrados.

## 👥 Integrantes y Roles
El equipo de trabajo está compuesto por:

* **Hernán Vera** - *Líder de Proyecto* (Gestión de repositorio y coordinación).
* **Matias Peralta** - *Desarrollador* (Implementación de lógica en Python y Sockets).
* **Claudio Zambra** - *Documentador* (Redacción técnica y manuales de uso).

---

## 🚀 Funcionalidades Principales
El script utiliza dos métodos fundamentales de reconocimiento de red:

1.  **Barrido ICMP (Ping Sweep):** Utiliza el comando `ping` del sistema operativo para verificar qué direcciones IP responden dentro del rango configurado (1 al 254).
2.  **Escaneo de Puertos TCP:** Para cada equipo activo detectado, intenta establecer una conexión en puertos críticos:
    * **21** (FTP)
    * **22** (SSH)
    * **80** (HTTP)
    * **443** (HTTPS)
3.  **Manejo de Argumentos:** Incluye soporte inicial para seleccionar objetivos mediante la línea de comandos (parámetro `-t`).

## 🛠️ Requisitos del Sistema

Para que el script funcione correctamente, asegúrate de tener instalado:

1. **Python 3.x**
2. **Permisos de Administrador:** Necesarios para ejecutar comandos de red y abrir sockets sin restricciones del firewall.

## 📖 Instrucciones de Uso

> [!IMPORTANT]
> **Limpieza de Código:** Antes de ejecutar, asegúrate de haber resuelto los conflictos de Git (eliminar las marcas `<<<<<<<`, `=======` y `>>>>>>>`) para que el intérprete de Python no lance errores de sintaxis.

### 1. Ejecución Estándar
Por defecto, el script escaneará el rango de red `192.168.1.x`:
```bash
python escaneoredes.py
2. Uso con Argumentos (En desarrollo)
El script permite definir un objetivo específico:

Bash
python escaneoredes.py -t 192.168.1.1
⚠️ Aviso Legal
Este software ha sido creado con fines exclusivamente educativos para la asignatura de Redes Avanzadas. El uso de herramientas de escaneo en redes ajenas sin autorización previa puede ser ilegal. El equipo no se responsabiliza por el mal uso de esta herramienta.

© 2026 - Grupo CHM - INACAP
