import numpy as np
import matplotlib.pyplot as plt

freq = np.logspace(1, 5, 41) #generates 41 logarithmically spaced frequency points 10e1 being 10HZ and 10e5 being 100,000 HZ

#I'm using a dictionary to model the components, since it's faster than createing an object

def hp_omega(freq):
    return 2 * np.pi * freq

def hp_crit_freq(R,C):
    return 1 / ( 2 * np.pi * R * C)

hp_filter = {
    'R': 38.3e3,
    'C': .22e-3,
    'omega': hp_omega,
    'crit_freq': hp_crit_freq
        }

def hp_transfer(omega, R, C):
    H = omega / (omega + (1/(R * C)))  #1j is how to use imaginary numbers in python
    return H


def hp_bode_data():
    hp = hp_transfer(hp_filter['omega'](freq), hp_filter['R'], hp_filter['C'])
    magnitude = np.abs(lp)
    magnitude_to_db = 20 * np.log10(magnitude)
    phase = np.angle(hp, deg=True)

    print(f"{'Frequency (Hz)':>15} {'Magnitude':>12} {'Gain (dB)':>12} {'Phase (deg)':>12}")

    for f, mag, db, ph in zip(freq, magnitude, magnitude_to_db, phase):
        print(f"{f:15.2f} {mag:12.4f} {db:12.2f} {ph:12.2f}")
    print(f"Critical frequency: {lp_filter['crit_freq'](lp_filter['R'],lp_filter['C'])}")

def hp_bode_plot():
    hp = hp_transfer(
            hp_filter['omega'](freq),
            hp_filter['R'],
            hp_filter['C'],
            )
    magnitude = np.abs(lp)
    magnitude_db = 20 * np.log10(magnitude)
    phase = np.angle(lp, deg=True)

    plt.figure(figsize=(10,6))
    plt.semilogx(freq, magnitude_db) #Xaxis = logarithmic and Y axis = lineaer
    plt.xlabel("Frequency (Hz)", fontsize=16)
    plt.ylabel("Gain (dB)", fontsize=16)
    plt.title("Filter #1 - High Pass BODE PLOT", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("plots/filter_2_bode.png", dpi=300, bbox_inches="tight")
    plt.show()
    
    #Phase Angle graph
    plt.figure(figsize=(10,7))
    plt.semilogx(freq, phase)
    plt.xlabel("Frequency (Hz)",fontsize=16)
    plt.ylabel("Phase (degrees)", fontsize=16)
    plt.title("Filter #2 - Hgh Pass PHASE PLOT", fontsize=20)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.savefig("filter2_phase.png", dpi=300, bbox_inches="tight")
    plt.show()
hp_bode_data()
hp_bode_plot()
