"""web_integration.py
Módulo de integración entre el servidor DHCP y el servidor web de pruebas.
Levanta un servidor web estático una vez que el servidor DHCP está activo.
"""

import threading
import time
from web_server.web_server import levantar_servidor_web

class WebIntegration:
    def __init__(self):
        self.web_thread = None
        self.web_port = 8080
        self.running = False

    def start_web_server(self):
        """Inicia el servidor web en un hilo separado"""
        if self.web_thread and self.web_thread.is_alive():
            print("⚠️  El servidor web ya está en ejecución.")
            return

        self.running = True
        self.web_thread = threading.Thread(
            target=self._run_web_server,
            daemon=True,
            name="WebTestServer"
        )
        self.web_thread.start()
        print(f"🌐 Servidor Web de Pruebas iniciado en puerto {self.web_port}")
        print(f"   → Accede desde el navegador: http://localhost:{self.web_port}")

    def _run_web_server(self):
        """Ejecuta el servidor web"""
        try:
            levantar_servidor_web(self.web_port)
        except Exception as e:
            print(f"❌ Error en servidor web: {e}")

    def stop(self):
        """Detiene el servidor web (nota: HTTPServer no se detiene fácilmente)"""
        self.running = False
        print("🛑 Servidor web marcado para detención.")


# Instancia global
web_integration = WebIntegration()