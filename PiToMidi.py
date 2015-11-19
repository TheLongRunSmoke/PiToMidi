from midiutil.MidiFile import MIDIFile
import sys
import os.path
sys.path.append('libs')
from utils import *

# This tuple contains notes representation.
# From H3(0) to D5(9). Refer to MIDI-format if you want to change this.
notes = (47, 48, 50, 52, 53, 55, 57, 59, 60, 62)

fromFile, toFile = argv_resolver(sys.argv)
MIDI = MIDIFile(1)
track = 0
time = 0
MIDI.addTrackName(track,time,fromFile[0:-4])
MIDI.addTempo(track,time,180)
track = 0
channel = 0
time = 0
duration = 1
volume = 100
with open(fromFile) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if is_number(c):
        pitch = notes[int(c)]
        time += 1
        duration = int(c)
        MIDI.addNote(track,channel,pitch,time,duration,volume)
        lastChar = c
        c
binfile = open(toFile, 'wb')
MIDI.writeFile(binfile)
binfile.close()
print 'Ready!'
