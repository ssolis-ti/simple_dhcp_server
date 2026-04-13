# Simple DHCP Server
[English](#english) | [Español](#español)

---

## English

This is a purely Python DHCP server. Originally, it required no external libraries. With the 2026 Fork, some dependencies (like Flask) were added, but they are now **vendored locally** inside the `vendor/` folder so you DO NOT need to install anything via `pip`. Just run the script, making the project fully portable.

It was tested under Ubuntu 14 with Python and Windows 7. It does not use any operating system specific Python functions, so it should work when Python 3 works.

![images/dhcpgui.png](images/dhcpgui.png)  
dhcpgui lists MAC address, IP address and host name.

This DHCP server program will assign IP addresses ten seconds after it received packets from clients. So it can be used in networks that already have a dhcp server running.

This Python DHCP server

- shows clients in the network
- lists IP address, Mac address and host name
- highlights recently refreshed/added clients
- assigns IP addresses 10 seconds later than usual DHCP servers
- remembers addresses in the `hosts.csv` file.
- can be configured to serve all DHCP options using Python

### New Improvements (Fork 2026)

- **Integrated Web Server**: Includes a Flask web server that runs alongside the DHCP server using `threading` (executable via `run.py`).
- **Centralized Configuration**: A `config.py` file was added to define server parameters (web server port, network interfaces, IP pool, and DHCP configuration).
- **Authentication and Registration Modules**: New flows to manage users and registrations.
- **Modular Structure**: The web components are packaged in their own module (`web_server/`).
- **Testing Tools and Documentation**: Improved documentation and the addition of a web server with tools to test network equipment, Wi-Fi links (AP), and local connections without needing nearby WAN access.

### Quick Start and Usage Instructions (Fork)

1. **Dependencies Pre-installed**: 
   All required packages (Flask, Scapy, etc.) are already included locally in the `vendor/` folder. **No internet or pip installation is required!**

2. **Configure Network and Ports**:
   Open the `config.py` file and edit the interface or IP where you want to listen, as well as the DHCP segment you are going to distribute.
   - `DHCP_BIND_ADDRESS` = your static IP or local network.
   - `DHCP_NETWORK` / `DHCP_SUBNET_MASK` = the DHCP subnet and network mask.

3. **Run the Unified Server**:
   Since DHCP requires special permissions, run the main script in your terminal (as Administrator or `root` in Linux):
   ```bash
   python run.py
   ```
   *This will start the DHCP Server to distribute IPs and the Web Server (usually on `http://<Your-Ip>:5000`) simultaneously. From the web panel, you can perform network tests or register new devices.*

Have a look at:

- The [official website][web] for installation and configuration instructions.
- The [source code][source].
- The [project translation on Weblate][weblate].

---

## Español

Este es un servidor DHCP en Python. Originalmente no requería bibliotecas externas. Con el Fork 2026 se añadieron dependencias (como Flask), pero ahora vienen **incluidas localmente** en la carpeta `vendor/`. NO es necesario instalar nada a través de `pip`, lo cual hace al proyecto totalmente portable y listo para usar offline.

Fue probado bajo Ubuntu 14 con Python y Windows 7. No utiliza ninguna función de Python específica del sistema operativo, por lo que debería funcionar siempre que Python 3 funcione.

![images/dhcpgui.png](images/dhcpgui.png)  
dhcpgui lista la dirección MAC, la dirección IP y el nombre de host.

Este programa de servidor DHCP asignará direcciones IP diez segundos después de recibir paquetes de los clientes. Por lo tanto, se puede utilizar en redes que ya tienen un servidor DHCP en ejecución.

Este servidor DHCP en Python

- muestra los clientes en la red
- lista la dirección IP, dirección MAC y nombre de host
- resalta los clientes actualizados/añadidos recientemente
- asigna direcciones IP 10 segundos más tarde que los servidores DHCP habituales
- recuerda las direcciones en el archivo `hosts.csv`
- se puede configurar para proporcionar todas las opciones DHCP usando Python

### Nuevas Mejoras (Fork 2026)

- **Servidor Web Integrado**: Incluye un servidor web Flask que corre junto al servidor DHCP usando `threading` (ejecutable vía `run.py`).
- **Configuración Centralizada**: Se añadió un archivo `config.py` para definir los parámetros del servidor (puerto del servidor web, interfaces de red, IP pool y configuración DHCP).
- **Módulos de Autenticación y Registro**: Nuevos flujos para administrar usuarios y registros.
- **Estructura Modular**: Los componentes web están empaquetados en su propio módulo (`web_server/`).
- **Herramientas de Testeo y Documentación**: Mejora en la documentación y adición de un servidor web con herramientas para testear equipos de red, enlaces Wi-Fi (AP) y conexiones locales sin necesidad de contar con acceso WAN cercano.

### Inicio Rápido e Instrucciones de Uso (Fork)

1. **Dependencias Preinstaladas**: 
   Todos los paquetes necesarios (Flask, Scapy, etc.) ya están incluidos de forma local en la carpeta `vendor/`. **¡No se requiere internet ni instalación con pip!**

2. **Configurar la Red y Puertos**:
   Abre el archivo `config.py` y edita la interfaz o IP donde quieres escuchar, así como el segmento DHCP que vas a repartir.
   - `DHCP_BIND_ADDRESS` = tu IP estática o red local.
   - `DHCP_NETWORK` / `DHCP_SUBNET_MASK` = la subred y máscara de red del DHCP.

3. **Ejecutar el Servidor Unificado**:
   Dado que el DHCP requiere permisos especiales, ejecuta el script principal en tu terminal (como Administrador o `root` en Linux):
   ```bash
   python run.py
   ```
   *Esto iniciará el Servidor DHCP para repartir IPs y el Servidor Web (usualmente en `http://<Tu-Ip>:5000`) de forma simultánea. Desde el panel web podrás hacer pruebas de red o registrar nuevos dispositivos.*

Échale un vistazo a:

- El [sitio web oficial][web] para las instrucciones de instalación y configuración.
- El [código fuente][source].
- La [traducción del proyecto en Weblate][weblate].

[web]: https://dhcp.quelltext.eu
[source]: https://github.com/niccokunzmann/simple_dhcp_server/
[weblate]: https://hosted.weblate.org/engage/simple-dhcp-server/
