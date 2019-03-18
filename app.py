from flask import Flask, render_template, request, Response, send_file
import sys
#sys.path.insert(0, "/VGM-Piano-Composer/")
from VGM_Piano_Composer.predict import generate
app = Flask(__name__)
import time


@app.route('/')
def static_page():
    return render_template('index.html')

@app.route('/default.mid')
def default():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/weights.hdf5', r'VGM_Piano_Composer/data/notes', 500 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='temp.mid')
    temp = open('temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return send_file(temp, mimetype='audio/midi')

@app.route('/ffvii.mid')
def ffvii():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/weights.hdf5', r'VGM_Piano_Composer/data/notes', 500 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='ff7_temp.mid')
    temp = open('ff7_temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return send_file(temp, mimetype='audio/midi')

@app.route('/ocarina.mid')
def ocarina():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/weights.hdf5', r'VGM_Piano_Composer/data/notes', 500 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='oot_temp.mid')
    temp = open('oot_temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return send_file(temp, mimetype='audio/midi')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    