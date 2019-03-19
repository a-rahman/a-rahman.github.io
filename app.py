from flask import Flask, render_template, request, Response, send_file
import sys
#sys.path.insert(0, "/VGM-Piano-Composer/")
from VGM_Piano_Composer.predict import generate
app = Flask(__name__)
import time


@app.route('/')
def static_page():
    return render_template('index.html')

@app.route('/ffx.mid')
def default():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/ffx.hdf5', r'VGM_Piano_Composer/data/ffx', 125 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='ffx_temp.mid')
    temp = open('ffx_temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return Response(temp, mimetype='audio/midi')

@app.route('/ffvii.mid')
def ffvii():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/ff7.hdf5', r'VGM_Piano_Composer/data/ff7', 125 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='ff7_temp.mid')
    temp = open('ff7_temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return Response(temp, mimetype='audio/midi')

@app.route('/ocarina.mid')
def ocarina():
    t0 = time.time()
    model_file, note_file, song_length = r'VGM_Piano_Composer/ocarina.hdf5', r'VGM_Piano_Composer/data/ocarina', 125 
    midi_stream = generate(model_file, note_file, song_length)
    midi_stream.write('midi', fp='oot_temp.mid')
    temp = open('oot_temp.mid', 'rb')
    print("It took {} to run".format(time.time()-t0))
    return Response(temp, mimetype='audio/midi')

if __name__ == '__main__':
    app.run()
    