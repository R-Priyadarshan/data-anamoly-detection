# device_simulator.py
import time, requests, random
SERVER = "http://127.0.0.1:5000/data"
NUM_DEVICES = 5
INTERVAL = 0.5

def gen_reading(device_id):
    base_temp = 25 + device_id * 0.5
    temp = base_temp + random.gauss(0, 0.5)
    humidity = 40 + random.gauss(0, 2)
    return {"device_id": int(device_id), "temp": float(round(temp,3)), "humidity": float(round(humidity,3)), "ts": time.time()}

if __name__ == '__main__':
    print('Starting simulator -> posting to', SERVER)
    while True:
        for d in range(NUM_DEVICES):
            payload = gen_reading(d)
            try:
                requests.post(SERVER, json=payload, timeout=1)
            except Exception as e:
                print('post failed', e)
        time.sleep(INTERVAL)
