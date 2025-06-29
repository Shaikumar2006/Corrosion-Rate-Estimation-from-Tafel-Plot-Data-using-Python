import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def analyze_material(df, material):
    data = df[df["Material"] == material]
    data = data.copy()  # avoid SettingWithCopyWarning
    data["log_i"] = np.log10(data["CurrentDensity_uAcm2"])

    # Create folder if needed
    if not os.path.exists("images"):
        os.makedirs("images")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(data["Potential_V"], data["log_i"], marker='o', label=material)
    plt.xlabel("Potential (V)")
    plt.ylabel("log(Current Density) [log10 µA/cm²]")
    plt.title(f"Tafel Plot for {material}")
    plt.grid(True)
    plt.legend()
    plot_path = f"images/tafel_plot_{material.replace(' ', '_')}.png"
    plt.savefig(plot_path)
    plt.show()

    # Regression and corrosion rate
    slope, intercept, *_ = linregress(data["Potential_V"], data["log_i"])
    icorr = 10 ** intercept
    K = 3272
    EW = data["EquivalentWeight_g"].iloc[0]
    rho = data["Density_gcm3"].iloc[0]
    rate = (K * icorr * EW) / rho

    print(f"\n📊 Results for {material}:")
    print(f"i_corr ≈ {icorr:.4f} µA/cm²")
    print(f"Corrosion Rate ≈ {rate:.2f} mm/year")
    print(f"Plot saved at: {plot_path}")
