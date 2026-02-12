import matplotlib.pyplot as plt
import numpy as np

# Piezoelektrik enerji hasadı simülasyonu
time = np.linspace(0, 10, 1000)
# Yaya trafiği etkisini simüle eden düzensiz voltaj verisi
voltage = 5 * np.sin(2 * np.pi * 0.5 * time) * np.exp(-0.1 * time) + np.random.normal(0, 0.2, 1000)
voltage = np.abs(voltage)

# Profesyonel Mühendislik Stili
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(time, voltage, color='#00d4ff', linewidth=1.5, label='Gerilim Çıkışı (mV)')
ax.fill_between(time, voltage, color='#00d4ff', alpha=0.2)

ax.set_title('Simülasyon: Yaya Trafiğinden Piezoelektrik Enerji Hasadı', fontsize=16, fontweight='bold', color='white', pad=20)
ax.set_xlabel('Zaman (Saniye)', fontsize=12, color='#cccccc')
ax.set_ylabel('Üretilen Gerilim (mV)', fontsize=12, color='#cccccc')

ax.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Sağ alta "Bertan Sert | Engineering Portfolio" imzası
plt.text(0.95, 0.05, 'Bertan Sert | Engineering Portfolio', transform=ax.transAxes, 
         fontsize=10, color='gray', alpha=0.5, ha='right')

plt.legend(loc='upper right', frameon=False)
plt.tight_layout()

plt.show() # Grafiği ekranda göster