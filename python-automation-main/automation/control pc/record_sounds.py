import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100

my_recording = sounddevice.rec(frames=seconds * fps,samplerate=fps,channels=1)
sounddevice.wait()
write("output.mp3",fps,my_recording)