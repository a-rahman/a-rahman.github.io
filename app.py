from flask import Flask, render_template, request, Response, send_file
import sys
app = Flask(__name__)
import time
import glob
import random


ff7_files = glob.glob(r'ff7_output/*.mid')
oot_files = glob.glob(r'oot_output/*.mid')


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    