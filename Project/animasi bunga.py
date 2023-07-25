import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Buat data untuk animasi
t = np.linspace(0, 2 * np.pi, 120)
x = np.sin(t)
y = np.cos(t)

# Buat figure dan axes
fig, ax = plt.subplots()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Buat titik awal
point, = ax.plot([x[0]], [y[0]], marker="o", color="crimson", markersize=10)

# Buat fungsi untuk mengupdate posisi titik setiap frame
def update(n):
    point.set_data([x[n]], [y[n]])
    return point,

# Buat animasi
anim = FuncAnimation(
    fig, update, frames=np.arange(0, len(x)), interval=50, blit=True
)

plt.show()
