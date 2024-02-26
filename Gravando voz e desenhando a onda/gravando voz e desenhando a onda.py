#1. importando bibliotecas
import wave
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

#2. gravando áudio
#2.1 definindo parametros do áudio a ser gravado
fpb = 3200
Format = pyaudio.paInt16
Channels = 1
Rate = 16000

#2.2 cria um objeto pra trabalhar

p = pyaudio.PyAudio()
stream = p.open(
    format = Format,
    channels = Channels,
    rate = Rate,
    input = True,
    frames_per_buffer = fpb
)

#2.3 grava de fato o áudio
print ("On Air")
seconds=5
frames=[]
for i in range(0,int(Rate/fpb*seconds)):
    data = stream.read(fpb)
    frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(Channels)
obj.setsampwidth(p.get_sample_size(Format))
obj.setframerate(Rate)
obj.writeframes(b"".join(frames))
obj.close

#3. pegando os dados que nós temos e usando um código feito previamente para desenhar a onda do áudio gravado

#3.1 abrindo o arquivo de áudio gerado
wav = wave.open("output.wav",'r')
raw = wav.readframes(-1)
sampleRate=wav.getframerate()

#3.2 transformando os dados em um arquivo numpy
raw = np.frombuffer(raw, "int16")

#3.3 Desenhando a onda
time=np.linspace(0,len(raw)/sampleRate, num=len(raw))
plt.title("Olha que legal")
plt.plot(time, raw, color ='green')
plt.ylabel("amplitude")
plt.show()

