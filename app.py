from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Render.com Test Webhook",
        "time": datetime.utcnow().isoformat()
    })

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    timestamp = datetime.utcnow().isoformat()
    
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        headers = dict(request.headers)
        
        print(f"[{timestamp}] WEBHOOK RECEIVED")
        print(f"Headers: {headers}")
        print(f"Body: {data}")
        
        return jsonify({
            "status": "success",
            "received_at": timestamp,
            "method": "POST",
            "data": data
        }), 200
    else:
        return jsonify({
            "status": "online",
            "endpoint": "/webhook",
            "methods": ["POST"],
            "time": timestamp
        }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
