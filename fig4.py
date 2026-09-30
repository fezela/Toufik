import numpy as np
import matplotlib.pyplot as plt

freq = np.logspace(1, 5, 41) #generates 41 logarithmically spaced frequency points 10e1 being 10HZ and 10e5 being 100,000 HZ

#I'm using a dictionary to model the components, since it's faster than createing an object

def omega(freq):
    return 2 * np.pi * freq

def crit_freq(R,C):
    return 1 / ( 2 * np.pi * R * C)

bandpass_filter = {
    'R1': 38.3e3,
    'C1': .22e-6,
    'R2': 22.1e3,
    'C2': 360e-12,
    'R3': 220,
    'omega': omega,
    'crit_freq': crit_freq
        }

def h_transfer(omega, R1, C1, R2, C2, R3):
    rp = (R1 * R3)/(R1 + R3)
    s = 1j * omega  #1j is how to use imaginary numbers in python
    H = s * rp * C1 /(1 + s * (rp * C1 + rp*C2 + R2*C1) + s**2*rp*R2*C1*C2)
    return H


def bode_data():
    h = h_transfer(
            bandpass_filter['omega'](freq), 
            bandpass_filter['R1'], 
            bandpass_filter['C1'], 
            bandpass_filter['R2'], 
            bandpass_filter['C2'],
            bandpass_filter['R3'],
            )
    magnitude = np.abs(h)
    magnitude_to_db = 20 * np.log10(magnitude)
    phase = np.angle(h, deg=True)

    print(f"{'Frequency (Hz)':>15} {'Magnitude':>12} {'Gain (dB)':>12} {'Phase (deg)':>12}")

    for f, mag, db, ph in zip(freq, magnitude, magnitude_to_db, phase):
        print(f"{f:15.2f} {mag:12.4f} {db:12.2f} {ph:12.2f}")
    print(f"Critical frequency 1: {bandpass_filter['crit_freq'](bandpass_filter['R1'],bandpass_filter['C1'])}")
    print(f"Critical frequncy 2: {bandpass_filter['crit_freq'](bandpass_filter['R2'], bandpass_filter['C2'])}")

def bode_plot():
    h = h_transfer(
            bandpass_filter['omega'](freq),
            bandpass_filter['R1'],
            bandpass_filter['C1'],
            bandpass_filter['R2'],
            bandpass_filter['C2'],
            bandpass_filter['R3']
            )
    magnitude = np.abs(h)
    magnitude_db = 20 * np.log10(magnitude)
    phase = np.angle(h, deg=True)

    plt.figure(figsize=(10,6))
    plt.semilogx(freq, magnitude_db) #Xaxis = logarithmic and Y axis = lineaer
    plt.xlabel("Frequency (Hz)", fontsize=16)
    plt.ylabel("Gain (dB)", fontsize=16)
    plt.title("Filter #4 - Band Pass BODE PLOT", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("plots/filter_4_bode.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    #Phase Angle graph
    plt.figure(figsize=(10,7))
    plt.semilogx(freq, phase)
    plt.xlabel("Frequency (Hz)",fontsize=16)
    plt.ylabel("Phase (degrees)", fontsize=16)
    plt.title("Filter #4 - Band Pass PHASE PLOT", fontsize=20)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("plots/filter_4_phase.png", dpi=300, bbox_inches="tight")
    plt.show()
#bode_data()
bode_plot()
