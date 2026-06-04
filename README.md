# 🔌 Simple DHCP Server & Flask Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3" />
  <img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License" />
  <img src="https://img.shields.io/badge/Portability-Offline--First-success?style=for-the-badge" alt="Portable" />
</p>

<p align="center">
  <a href="#english-version">🇬🇧 English</a> •
  <a href="#versión-en-español">🇪🇸 Español</a>
</p>

---

## 🇬🇧 English Version

This is a lightweight, pure Python DHCP server. Originally, it required no external libraries. With the **2026 Fork**, additional features (like a Flask web dashboard) were integrated. All dependencies are now **vendored locally** inside the `vendor/` directory, meaning the server is **100% portable, offline-first, and requires no `pip install` commands**.

### 🌟 Key Features

* **Visual Client Dashboard:** Lists MAC addresses, IP leases, and hostnames in real-time.
* **Smart Delay Assignment:** Assigns IP addresses 10 seconds later than standard DHCP servers, allowing it to safely coexist in networks that already have a running DHCP server.
* **Persistent Leases:** Saves IP allocations locally to a `hosts.csv` file.
* **Bridges Local Connections:** Perfect for testing network equipment, Wi-Fi access points (APs), and local setups without WAN access.

### 🚀 Fork 2026 Enhancements

* **Threaded Flask Server:** Runs a Flask web server side-by-side with the DHCP service using native Python `threading` (executable via `run.py`).
* **Centralized Configuration:** Configured via `config.py` (manage port, bind address, netmask, lease time, and IP pools easily).
* **Modular Codebase:** Organizes web views and dashboard functions under the `web_server/` module.
* **Vendored Dependencies:** Portability ensured by placing Flask, Scapy, and other modules in `vendor/` to allow zero-config execution.

### 🛠️ Quick Start

#### 1. Configuration
Open `config.py` and adjust the binding interface and IP range:
```python
# Server Configuration
DHCP_BIND_ADDRESS = "192.168.1.1"   # Your static IP
DHCP_NETWORK = "192.168.1.0"        # Target subnet
DHCP_SUBNET_MASK = "255.255.255.0"  # Subnet Mask
DHCP_LEASE_TIME = 300               # Lease time in seconds
WEB_PORT = 80                       # Web Panel Port
```

#### 2. Running the Server
> [!IMPORTANT]
> Running a DHCP server requires binding to privileged ports. You **must** run the script with administrative privileges.

* **Windows (Administrator PowerShell/CMD):**
  ```bash
  python run.py
  ```
* **Linux / macOS:**
  ```bash
  sudo python run.py
  ```
*This starts both the DHCP server and the Web Dashboard (on `http://<DHCP_BIND_ADDRESS>:<WEB_PORT>`).*

---

## 🇪🇸 Versión en Español

Este es un servidor DHCP ligero desarrollado puramente en Python. Originalmente no requería librerías externas. Con el **Fork 2026**, se integraron funcionalidades adicionales (como un panel web con Flask). Todas las dependencias vienen **empaquetadas localmente** dentro del directorio `vendor/`, lo que hace que el servidor sea **100% portable, autónomo y listo para usar sin necesidad de `pip install`**.

### 🌟 Características Principales

* **Panel de Control Visual:** Muestra direcciones MAC, IPs asignadas y nombres de host de clientes en tiempo real.
* **Asignación Retardada Inteligente:** Asigna direcciones IP 10 segundos después de recibir la solicitud, lo que le permite coexistir de forma segura en redes que ya poseen un servidor DHCP activo.
* **Arrendamientos Persistentes:** Registra y recuerda las asignaciones locales en el archivo `hosts.csv`.
* **Ideal para Laboratorios:** Excelente herramienta para testear equipos de red, puntos de acceso Wi-Fi (AP) y conexiones locales sin requerir salida WAN.

### 🚀 Mejoras del Fork 2026

* **Servidor Flask Concurrente:** Ejecuta la interfaz web de forma paralela al servicio DHCP mediante hilos nativos (`threading`) a través del archivo `run.py`.
* **Configuración Centralizada:** Control total mediante `config.py` (edita puertos, subredes, máscaras, IPs de escucha y tiempos de arrendamiento).
* **Código Modularizado:** Estructura limpia que independiza la interfaz web en la carpeta `web_server/`.
* **Cero Instalaciones:** Contiene librerías como Flask y Scapy en `vendor/` para ejecutar el servidor inmediatamente fuera de línea.

### 🛠️ Inicio Rápido

#### 1. Configuración
Abre el archivo `config.py` y define los parámetros del servidor:
```python
# Configuración del Servidor
DHCP_BIND_ADDRESS = "192.168.1.1"   # Tu IP estática local
DHCP_NETWORK = "192.168.1.0"        # Subred del DHCP
DHCP_SUBNET_MASK = "255.255.255.0"  # Máscara de subred
DHCP_LEASE_TIME = 300               # Tiempo de arriendo (segundos)
WEB_PORT = 80                       # Puerto de la interfaz web
```

#### 2. Ejecutar el Servidor
> [!IMPORTANT]
> Los servidores DHCP requieren unirse a puertos con privilegios elevados. **Es obligatorio** ejecutar la aplicación con permisos de administrador.

* **Windows (PowerShell/CMD como Administrador):**
  ```bash
  python run.py
  ```
* **Linux / macOS:**
  ```bash
  sudo python run.py
  ```
**Esto iniciará concurrentemente el servidor DHCP y el panel web en `http://<DHCP_BIND_ADDRESS>:<WEB_PORT>`.*

---

## 🔗 Project References / Referencias

* [Official Website / Sitio Web Oficial][web]
* [Original Repository / Repositorio Original][source]
* [Translations / Traducciones Weblate][weblate]

[web]: https://dhcp.quelltext.eu
[source]: https://github.com/niccokunzmann/simple_dhcp_server/
[weblate]: https://hosted.weblate.org/engage/simple-dhcp-server/
