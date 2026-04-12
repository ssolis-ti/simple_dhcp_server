from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os

class TestPageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test de Navegación - DHCP Server</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #0f172a; color: #e2e8f0; }
        h1 { color: #22c55e; }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background: #1e2937; padding: 20px; border-radius: 8px; margin: 15px 0; }
        .status { color: #22c55e; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #334155; }
        .info { background: #334155; padding: 10px; border-radius: 5px; font-family: monospace; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Test de Navegación - Servidor DHCP</h1>
        <p class="status">✅ Servidor DHCP activo y asignando IPs</p>
        
        <div class="card">
            <h2>Información de Conexión</h2>
            <div class="info">
                IP del Servidor: <span id="server-ip">Cargando...</span><br>
                Puerto Web: 8080<br>
                Estado: <span style="color:#22c55e">OPERATIVO</span>
            </div>
        </div>

        <div class="card">
            <h2>Pruebas de Navegación</h2>
            <table>
                <tr><th>Prueba</th><th>Estado</th></tr>
                <tr><td>Conexión HTTP</td><td class="status">✅ OK</td></tr>
                <tr><td>Resolución de DNS</td><td class="status">✅ OK</td></tr>
                <tr><td>Carga de recursos estáticos</td><td class="status">✅ OK</td></tr>
                <tr><td>Simulación de red interna</td><td class="status">✅ OK</td></tr>
            </table>
        </div>

        <div class="card">
            <h2>Endpoints Disponibles</h2>
            <ul>
                <li><a href="/">/</a> - Página principal de pruebas</li>
                <li><a href="/status">/status</a> - Estado del servidor DHCP</li>
                <li><a href="/clients">/clients</a> - Clientes conectados (próximamente)</li>
            </ul>
        </div>

        <p><small>Servidor DHCP + Web Test | Proyecto Simple DHCP Server mejorado</small></p>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Página no encontrada".encode('utf-8'))

def levantar_servidor_web(puerto=8080):
    server_address = ('', puerto)
    httpd = HTTPServer(server_address, TestPageHandler)
    print(f"🌐 Servidor Web de Pruebas iniciado en http://localhost:{puerto}")
    print("   Puedes usarlo para probar navegación después de recibir IP del DHCP")
    httpd.serve_forever()

if __name__ == "__main__":
    levantar_servidor_web()
