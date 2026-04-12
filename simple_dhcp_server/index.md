# Simple DHCP Server

Este proyecto es un servidor DHCP escrito en Python que asigna direcciones IP a clientes en una red.

## Carpetas

* [docs](#docs)
* [tests](#tests)

## Archivos

* `dhcp.py`: lógica principal del servidor DHCP
* `listener.py`: escucha peticiones DHCP
* `transaction.py`: maneja transacciones DHCP
* `host.py`: representa hosts en la red
* `config.py`: configuración del servidor DHCP

## Conexiones entre archivos

* `dhcp.py` utiliza `listener.py` para escuchar peticiones DHCP
* `transaction.py` utiliza `host.py` para representar hosts en la red
* `listener.py` se conecta con `dhcp.py` para procesar peticiones DHCP

## Clasificación de importancia

* **Crítico**: `dhcp_server.py`, `config.py`
* **Importante**: `transaction.py`, `host.py`, `listener.py`
* **Imperante**: `dhcp.py`