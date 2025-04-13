from flask import Flask
from prometheus_client import start_http_server, Counter
import time

# Crear la aplicación de Flask
app = Flask(__name__)

# Definir una métrica para contar el número de solicitudes
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def hello():
    # Incrementar el contador cada vez que se haga una solicitud al endpoint
    REQUESTS.labels(method='GET', endpoint='/').inc()
    return "Hello, World!"

if __name__ == '__main__':
    # Iniciar un servidor HTTP para servir las métricas en el puerto 8000
    start_http_server(5000)
    
    # Iniciar la aplicación Flask en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
