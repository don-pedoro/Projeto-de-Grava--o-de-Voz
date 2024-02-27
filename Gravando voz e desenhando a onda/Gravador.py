#importando bibliotecas
import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
gravacao=pyaudio.PyAudio()

#Avisa que a gravação vai começar usando o comando print
print("Gravando, digite ctrl c para parar")

#
stream = gravacao.open(
    input=True,
    format=pyaudio.paInt32,
    channels=1,
    rate=44000,
    frames_per_buffer=1024
)

frames=[]
try:
    while True:
        bloco=stream.read(1024)
        frames.append(bloco)
except KeyboardInterrupt:
    pass
stream.start_stream()
stream.close()
gravacao.terminate()
arquivo = wave.open('gravação.wav','wb')
arquivo.setnchannels(1)
arquivo.setframerate(44000)
arquivo.setsampwidth(gravacao.get_sample_size(pyaudio.paInt32))
arquivo.writeframes(b''.join(frames))
arquivo.close()


wav = wave.open("gravação.wav",'r')
raw = wav.readframes(-1)
sampleRate=wav.getframerate()

# transformando os dados em um arquivo numpy
raw = np.frombuffer(raw, "int32")

#Desenhando a onda
time=np.linspace(0,len(raw)/sampleRate, num=len(raw))
plt.title("Olha que legal")
plt.plot(time, raw, color ='green')
plt.ylabel("amplitude")
plt.show()