from flask import Flask, render_template
from prometheus_client import start_http_server, Counter
import threading

# Crear la aplicación de Flask
app = Flask(__name__)

# Definir una métrica para contar el número de solicitudes
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def index():
    # Incrementar el contador Prometheus para cada solicitud GET a "/"
    REQUESTS.labels(method='GET', endpoint='/').inc()
    return render_template('index.html')

def start_prometheus_server():
    # Ejecuta el servidor de métricas Prometheus en un hilo separado
    start_http_server(8000)

if __name__ == '__main__':
    # Iniciar el servidor Prometheus en segundo plano
    threading.Thread(target=start_prometheus_server).start()

    # Ejecutar la aplicación Flask
    app.run(host='0.0.0.0', port=5000)
