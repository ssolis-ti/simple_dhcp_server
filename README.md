# Simple DHCP Server

This is a purely Python DHCP server that does not require any additional libraries or installs other that Python 3.

It was testet under Ubuntu 14 with Python and Windows 7. It does not use any operating system specific Python functions, so it should work when Python 3 works.

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

## Nuevas Mejoras (Fork 2026)

- **Servidor Web Integrado**: Incluye un servidor web Flask que corre junto al servidor DHCP usando `threading` (ejecutable vía `run.py`).
- **Configuración Centralizada**: Se añadió un archivo `config.py` para definir los parámetros del servidor (puerto del servidor web, interfaces de red, IP pool y configuración DHCP).
- **Módulos de Autenticación y Registro**: Nuevos flujos para administrar usuarios y registros.
- **Estructura Modular**: Los componentes web están empaquetados en su propio módulo (`web_server/`).
- **Herramientas de Testeo y Documentación**: Mejora en la documentación y adición de un servidor web con herramientas para testear equipos de red, enlaces Wi-Fi (AP) y conexiones locales sin necesidad de contar con acceso WAN cercano.

### Inicio Rápido e Instrucciones de Uso (Fork)

1. **Instalar Dependencias**: 
   Instala los requerimientos de Python necesarios (Framework Flask y dependencias web):
   ```bash
   pip install -r requirements.txt
   ```

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


Have a look at:

- The [official website][web] for installation and configuration instructions.
- The [source code][source].
- The [project translation on Weblate][weblate].

[web]: https://dhcp.quelltext.eu
[source]: https://github.com/niccokunzmann/simple_dhcp_server/
[weblate]: https://hosted.weblate.org/engage/simple-dhcp-server/
