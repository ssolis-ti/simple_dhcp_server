import os
import sys

# Agregar la carpeta "vendor" al PATH de Python para cargar las librerías portables
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor'))

import threading
from simple_dhcp_server.dhcp import DHCPServer, DHCPServerConfiguration
from web_server.app import run_flask_server
import config

def run_custom_dhcp():
    configuration = DHCPServerConfiguration()
    configuration.debug = print
    
    # Aplicar configuración desde config.py
    configuration.bind_address = config.DHCP_BIND_ADDRESS
    configuration.network = config.DHCP_NETWORK
    configuration.subnet_mask = config.DHCP_SUBNET_MASK
    configuration.ip_address_lease_time = config.DHCP_LEASE_TIME
    
    server = DHCPServer(configuration)
    server.run()

def main():
    print("🚀 Iniciando Servidor DHCP y Web...")
    
    # Iniciar servidor DHCP
    dhcp_thread = threading.Thread(target=run_custom_dhcp)
    dhcp_thread.start()
    
    # Iniciar servidor web Flask en la MISMA IP que el DHCP
    flask_thread = threading.Thread(
        target=run_flask_server, 
        kwargs={'host': config.DHCP_BIND_ADDRESS, 'port': config.WEB_PORT}
    )
    flask_thread.start()
    
    # Mantener hilos en ejecución
    dhcp_thread.join()
    flask_thread.join()

if __name__ == "__main__":
    main()
