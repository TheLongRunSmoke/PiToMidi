## PiToMidi

Pi in musical representation. It sounds fun, right? I think so too, and wrote this python script. It's get a text file with many numbers and turn it in MIDI file. That file can be played with any synthesizer.


#### Using
You need Python 2.7 for run this.


1. First of all, clone this repo.

  ```
  git clone https://github.com/TheLongRunSmoke/PiToMidi.git
  ```
2. Install midiutil lib.

  ```
  git clone https://github.com/TheLongRunSmoke/midiutil.git
  cd midutil
  python setup.py install
  ```
3. Run.

  ```
  PiToMidi.py
  ```
It's use first txt in directory. You can specify input txt, by:

  ```
  PiToMidi.py input.txt
  ```
and output MIDI, by:

  ```
  PiToMidi.py input.txt output.mid
  ```


#### Additional
If you want make video for your music, use ```pden.py```. This script generate bunch of pics, add one element from txt on each. It's needed Pillow: ```pip install Pillow```


### Have fun!
