# server.py
from flask import Flask, request, jsonify
import csv, os
app = Flask(__name__)
CSV = 'sample_data.csv'
if not os.path.exists(CSV):
    with open(CSV, 'w') as f:
        f.write('device_id,ts,temp,humidity\n')

@app.route('/data', methods=['POST'])
def data():
    j = request.get_json()
    if not j:
        return jsonify({'status':'bad request'}), 400
    with open(CSV, 'a') as f:
        f.write(f"{j.get('device_id')},{j.get('ts')},{j.get('temp')},{j.get('humidity')}\n")
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run()
