import os, glob, subprocess

files = glob.glob(r'mario_output/*.mid')

for midi in files:
    fname = os.path.basename(midi)
    fname = fname.replace('.mid', '.mp3')
    call = ' '.join(['timidity', midi, '-Ow', '-o', '-', '|', 'lame', '-', '-b', '64', fname])
    subprocess.call(call, shell=True)
