from flask import Flask,Response

app = Flask(__name__)


@app.route('/play/wav')
def play_stream():
    

def generate():
    with open('content/Pink Pather.wav', rb) as wav:
        data = fwav


if __name__ == '__main__':
    app.run(debug=True)