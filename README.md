# ShelterFeels

ShelterFeels is a project involving RapsberryPi. The code here pertains to a specific object that can perform voice recognition and NFC tag reading. It has a simple gui user interface and, as feedback, controls neopixel LEDs.

The project was created by students as part of a collaboration between Freie Universität Berlin and Kunsthochschule Berlin-Weißensee.

In emotriowheel you will find basic first attempts involving an Arduino.
The shelterfeels directory contains the actual meat of project.

## Installation and running
Installation will be difficult, because the code is closely connected to the physical object we build. That said, if you're willing to overcome a lot of hardware problems, we advice you to read and understand the code thoroughly before doing anything with it.

You need python3.10 and the requirements listed in requirements.txt (which is yet incomplete). Doing `pip install -r requirments.txt` will get you there some of the way, but you are likely going to need some extra work to get some packages working.

To run, simply execute run.py with python as sudo: `sudo python run.py`

## Recognition app

You should have FFMPEG installed on your PC to work with audio files. https://ffmpeg.org/download.html
We can use text summarization (creates longer texts) or keywords extraction which is more fitting.
If your mic has more than 2 channels, audio is written only from first two. If you gave mono mic, channels are duplicated.

There's an option to do the processing on a server with inference_remote.


## GUI

Tkinter needs to be installed extra with something like `sudo apt-get install python3-tk`.
The GUI is conceptualized as an object that shows different slide. Each slide gets its own bit of code.

## NFC

-

## LED

-
