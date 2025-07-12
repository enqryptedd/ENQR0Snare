from flask import Flask, request
app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive():
    data = request.data
    with open("ogs.txt", "ab") as f:
        f.write(data + b"\n")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
