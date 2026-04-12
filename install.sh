"\"#!/bin/bash

# Instalar dependencias
echo \"🔧 Instalando dependencias...\"
pip install -r requirements.txt

# Copiar archivos de configuración
echo \"📂 Copiando archivos de configuración...\"
cp config.py simple_dhcp_server/
cp -r web_server simple_dhcp_server/

# Iniciar el sistema
echo \"🚀 Iniciando Servidor DHCP y Web...\"
python simple_dhcp_server/run.py
\""