from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import random
app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')
ERROR_COUNT = Counter('app_errors_total', 'Total Errors')
@app.route('/')
def home():
    REQUEST_COUNT.inc()

    # Simulate random error (30% chance)
    if random.random() < 0.3:
        ERROR_COUNT.inc()
        return "Error occurred!", 500
    
    return "Assessment:Monitoring app running!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)