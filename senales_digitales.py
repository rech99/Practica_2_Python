import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

import matplotlib.pyplot as plt

seno = SinSignal (freq= 40, amp= 1, offset=0)
coseno = CosSignal (freq=75, amp=1.3, offset=0)

waveSeno = seno.make_wave (duration=1, start=0, framerate=11025)
waveCoseno = coseno.make_wave (duration=1, start=0, framerate=11025)

waveResultante = waveSeno + waveCoseno

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

waveSeno.plot()
waveCoseno.plot()

plt.show()

waveResultante.plot()

plt.show()

