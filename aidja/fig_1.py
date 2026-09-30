import numpy as np
import matplotlib.pyplot as plt

freq = np.logspace(1, 5, 41) #generates 41 logarithmically spaced frequency points 10e1 being 10HZ and 10e5 being 100,000 HZ

#I'm using a dictionary to model the components, since it's faster than createing an object

def lp_omega(freq):
    return 2 * np.pi * freq

def lp_crit_freq(R,C):
    return 1 / ( 2 * np.pi * R * C)

lp_filter = {
    'R': 22.1e3,
    'C': 360e-12,
    'omega': lp_omega,
    'crit_freq': lp_crit_freq
        }

def lp_transfer(omega, R, C):
    H = 1 / (1 + 1j * omega * R * C)  #1j is how to use imaginary numbers in python
    return H


def lp_bode_data():
    lp = lp_transfer(lp_filter['omega'](freq), lp_filter['R'], lp_filter['C'])
    magnitude = np.abs(lp)
    magnitude_to_db = 20 * np.log10(magnitude)
    phase = np.angle(lp, deg=True)

    print(f"{'Frequency (Hz)':>15} {'Magnitude':>12} {'Gain (dB)':>12} {'Phase (deg)':>12}")

    for f, mag, db, ph in zip(freq, magnitude, magnitude_to_db, phase):
        print(f"{f:15.2f} {mag:12.4f} {db:12.2f} {ph:12.2f}")
    print(f"Critical frequency: {lp_filter['crit_freq'](lp_filter['R'],lp_filter['C'])}")

def lp_bode_plot():
    lp = lp_transfer(
            lp_filter['omega'](freq),
            lp_filter['R'],
            lp_filter['C'],
            )
    magnitude = np.abs(lp)
    magnitude_db = 20 * np.log10(magnitude)
    phase = np.angle(lp, deg=True)

    plt.figure(figsize=(10,6))
    plt.semilogx(freq, magnitude_db) #Xaxis = logarithmic and Y axis = lineaer
    plt.xlabel("Frequency (Hz)", fontsize=16)
    plt.ylabel("Gain (dB)", fontsize=16)
    plt.title("Filter #1 - Low Pass BODE PLOT", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("filter_1_bode.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    #Phase Angle graph
    plt.figure(figsize=(10,7))
    plt.semilogx(freq, phase)
    plt.xlabel("Frequency (Hz)",fontsize=16)
    plt.ylabel("Phase (degrees)", fontsize=16)
    plt.title("Filter #1 - Low Pass PHASE PLOT", fontsize=20)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("filter1_phase.png", dpi=300, bbox_inches="tight")
    plt.show()
lp_bode_data()
lp_bode_plot()
