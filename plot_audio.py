import matplotlib.pyplot as plt
import numpy as np
import wave

sound = wave.open("happy.wav","rb")
n_frames= sound.getnframes()
frame_rate = sound.getframerate()
signal_wave =  sound.readframes(-1)
sound.close()
time_for_audio = n_frames /frame_rate
print(time_for_audio)

signal_array= np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, time_for_audio, num=n_frames) 

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Graph for my Audio")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, time_for_audio)
plt.show()