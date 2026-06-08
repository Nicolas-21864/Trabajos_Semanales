import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# inciso a
a = [1,1,1,1] #bi
a0 = [1]

wa, Ha = signal.freqz(a, a0, worN=2048)

#Ha_db  = 20 * np.log10(np.abs(Ha))

plt.figure()
plt.plot(wa, np.abs(Ha))
plt.title('Modulo')
plt.xlabel('ω [rad/muestra]')
plt.grid()

plt.figure()
plt.plot(wa, np.unwrap(np.angle(Ha)))
plt.title('Fase')
plt.xlabel('ω [rad/muestra]')
plt.grid()

#%% 

# b
b = [1,1,1,1,1] #bi

wb, Hb = signal.freqz(b, a0, worN=2048)

#Hb_db  = 20 * np.log10(np.abs(Hb))

plt.figure()
plt.plot(wb, np.abs(Hb))
plt.title('Modulo')
plt.xlabel('ω [rad/muestra]')
plt.grid()

plt.figure()
plt.plot(wb, np.unwrap(np.angle(Hb)))
plt.title('Fase')
plt.xlabel('ω [rad/muestra]')
plt.grid()

#%%

# c
c = [1,-1] #bi

wc, Hc = signal.freqz(c, a0, worN=2048)

#Hc_db  = 20 * np.log10(np.abs(Hc))

plt.figure()
plt.plot(wc, np.abs(Hc))
plt.title('Modulo')
plt.xlabel('ω [rad/muestra]')
plt.grid()

plt.figure()
plt.plot(wc, np.unwrap(np.angle(Hc)))
plt.title('Fase')
plt.xlabel('ω [rad/muestra]')
plt.grid()

#%%

# d
d = [1,0,-1] #bi

wd, Hd = signal.freqz(d, a0, worN=2048)

#Hd_db  = 20 * np.log10(np.abs(Hd))

plt.figure()
plt.plot(wd, np.abs(Hd))
plt.title('Modulo')
plt.xlabel('ω [rad/muestra]')
plt.grid()

plt.figure()
plt.plot(wd, np.unwrap(np.angle(Hd)))
plt.title('Fase')
plt.xlabel('ω [rad/muestra]')
plt.grid()




plt.show()
