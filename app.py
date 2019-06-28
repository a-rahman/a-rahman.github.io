from flask import Flask, render_template, request, Response, send_file, jsonify
import sys
import time
import glob
import random
from serving import generate_tokens
import encoder

app = Flask(__name__)

ff7_files = glob.glob(r'ff7_output/*.mid')
oot_files = glob.glob(r'oot_output/*.mid')
mario_files = glob.glob(r'mario_output/*.mid')

enc = encoder.get_encoder('345M', 'models')


@app.route('/')
def static_page():
    return render_template('index.html')


@app.route('/ffvii.mid')
def ffvii():
    temp = open(random.choice(ff7_files), 'rb')
    return Response(temp, mimetype='audio/midi')


@app.route('/ocarina.mid')
def ocarina():
    temp = open(random.choice(oot_files), 'rb')
    return Response(temp, mimetype='audio/midi')


@app.route('/mario.mid')
def mario():
    temp = open(random.choice(mario_files), 'rb')
    return Response(temp, mimetype='audio/midi')


@app.route('/text', methods=['POST'])
def generate_text():
    if request.form:
        input_text = enc.encode(request.form['input'])
        tokens = generate_tokens(input_text)
        text = enc.decode(tokens[0])
    return jsonify({'output': text})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run()
