from flask import Flask, request, jsonify
import requests
import json
import time

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    numbers = set()

    start_time = time.time()
    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = json.loads(response.text)
                if 'numbers' in data:
                    numbers.update(data['numbers'])
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            pass

    end_time = time.time()
    response_time = end_time - start_time

    return jsonify({
        'numbers': sorted(list(numbers)),
        'response_time': response_time
    })

if __name__ == '__main__':
    app.run(port=8008)
