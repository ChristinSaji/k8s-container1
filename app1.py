from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/store-file', methods=['POST'])
def store_file():
    data = request.get_json()
    if not data or 'file' not in data or 'data' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    file_name = data['file']
    file_data = data['data']
    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    try:
        with open(f'/christin_PV_dir/{file_name}', 'w') as f:
            f.write(file_data)
        return jsonify({"file": file_name, "message": "Success."})
    except Exception as e:
        return jsonify({"file": file_name, "error": "Error while storing the file to the storage."}), 500

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'file' not in data or 'product' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400

    file_name = data['file']
    product = data['product']
    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."}), 400
    if not os.path.exists(f'/christin_PV_dir/{file_name}'):
        return jsonify({"file": file_name, "error": "File not found."}), 404

    response = requests.post('http://k8s-container2:6001/sum', json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

# test