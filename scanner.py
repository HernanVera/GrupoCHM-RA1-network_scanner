import socket    # Para hablar con otros computadores
import os        # Para usar el comando 'ping'
import argparse  # Para que el usuario elija qué IP escanear

# Configuramos el menú de opciones
parser = argparse.ArgumentParser(description="Escáner de Red - INACAP")
parser.add_argument("-t", "--target", help="IP a escanear")
args = parser.parse_args()