import wave

sound = wave.open("happy.wav","rb")#rb =read bits 


print("Number of channels",sound.getnchannels())
print("Number of number frames",sound.getnframes())
print("Frame Rate",sound.getframerate())
print("WIdth ",sound.getsampwidth)


time_audio = sound.getnframes()/  sound.getframerate()
print(time_audio)

frames = sound.readframes(-1) 
sound.close()

copied_sound = wave.open("happyCopy2.wav","wb")

copied_sound.setnchannels(1)
copied_sound.setsampwidth(2)
copied_sound.setframerate(84000.0)

copied_sound.writeframes(frames)
copied_sound.close()









