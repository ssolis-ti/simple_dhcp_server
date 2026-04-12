from flask import Flask, render_template_string, jsonify, request
import threading
import subprocess
import platform
from icmplib import ping
import json
import time

app = Flask(__name__)

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DHCP Network Tools - Test de Conectividad</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; }
        h1 { color: #22c55e; text-align: center; }
        .card { background: #1e2937; border-radius: 12px; padding: 20px; margin: 15px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        input, button { padding: 10px; margin: 5px; border-radius: 6px; }
        button { background: #22c55e; color: black; font-weight: bold; border: none; cursor: pointer; }
        button:hover { background: #86efac; }
        pre { background: #0f172a; padding: 15px; border-radius: 8px; overflow-x: auto; max-height: 400px; }
        .status { color: #22c55e; font-weight: bold; }
        .tabs { display: flex; gap: 10px; margin-bottom: 20px; }
        .tab { padding: 10px 20px; background: #334155; border-radius: 6px; cursor: pointer; }
        .tab.active { background: #22c55e; color: black; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 DHCP Network Tools</h1>
        <p class="status">Servidor DHCP Activo • Servidor Web en puerto 80</p>
        
        <div class="card">
            <h2>Pruebas de Conectividad</h2>
            <input type="text" id="target" placeholder="Ingresa IP o dominio (ej: 8.8.8.8 o google.com)" style="width:70%">
            <button onclick="runPing()">Ping</button>
            <button onclick="runTraceroute()">Traceroute</button>
        </div>

        <div class="card">
            <h3>Resultado:</h3>
            <pre id="result">Esperando acción...</pre>
        </div>

        <div class="card">
            <h3>Estado del Servidor DHCP</h3>
            <button onclick="getStatus()">Actualizar Estado</button>
            <pre id="status">Cargando estado...</pre>
        </div>
    </div>

    <script>
        function runPing() {
            const target = document.getElementById('target').value || '8.8.8.8';
            fetch('/api/ping', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({target: target})
            })
            .then(r => r.json())
            .then(data => {
                document.getElementById('result').textContent = data.result;
            });
        }

        function runTraceroute() {
            const target = document.getElementById('target').value || '8.8.8.8';
            fetch('/api/traceroute', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({target: target})
            })
            .then(r => r.json())
            .then(data => {
                document.getElementById('result').textContent = data.result;
            });
        }

        function getStatus() {
            fetch('/api/status')
            .then(r => r.json())
            .then(data => {
                document.getElementById('status').textContent = JSON.stringify(data, null, 2);
            });
        }
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/ping', methods=['POST'])
def api_ping():
    data = request.json
    target = data.get('target', '8.8.8.8')
    try:
        response = ping(target, count=4, timeout=2)
        result = f"Ping a {target}\\n"
        result += f"Paquetes enviados: 4\\n"
        result += f"Recibidos: {response.packets_received}\\n"
        result += f"Pérdida: {response.packet_loss*100:.1f}%\\n"
        result += f"RTT Promedio: {response.avg_rtt:.2f} ms\\n"
        if response.is_alive:
            result += "✅ Host reachable"
        else:
            result += "❌ Host no responde"
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": f"Error en ping: {str(e)}"})

@app.route('/api/traceroute', methods=['POST'])
def api_traceroute():
    data = request.json
    target = data.get('target', '8.8.8.8')
    try:
        cmd = ['tracert', target] if platform.system().lower() == 'windows' else ['traceroute', '-n', '-w', '2', target]
        output = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return jsonify({"result": output.stdout})
    except Exception as e:
        return jsonify({"result": f"Error en traceroute: {str(e)}"})

@app.route('/api/status')
def api_status():
    return jsonify({
        "dhcp_server": "running",
        "web_server": "running",
        "port": 80,
        "message": "Sistema completo operativo - Herramientas de red activas"
    })

def run_flask_server(host='0.0.0.0', port=80):
    print(f"🌐 Servidor Web Flask iniciado en http://{host}:{port}")
    print("   Herramientas disponibles: Ping y Traceroute")
    app.run(host=host, port=port, debug=False)

if __name__ == '__main__':
    run_flask_server()