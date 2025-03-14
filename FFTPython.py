import numpy as np
import matplotlib

# Set backend for compatibility
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Disable interactive mode for better performance
plt.ioff()
from matplotlib.widgets import Slider, Button, RadioButtons
from scipy.fftpack import fft, ifft

# Setup figure and layout
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
plt.subplots_adjust(left=0.18, bottom=0.25, right=0.95, top=0.9, hspace=0.3)

# Signal parameters
sample_rate = 1000  # Hz
duration = 1.0  # seconds
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Default component values
f1_init, f2_init, f3_init = 5, 10, 15  # Hz
a1_init, a2_init, a3_init = 1.0, 0.5, 0.2  # Amplitudes


# Core signal generator function
def generate_signal(f1, f2, f3, a1, a2, a3):
    return (a1 * np.sin(2 * np.pi * f1 * t) +
            a2 * np.sin(2 * np.pi * f2 * t) +
            a3 * np.sin(2 * np.pi * f3 * t))


# Initialize with default parameters
signal = generate_signal(f1_init, f2_init, f3_init, a1_init, a2_init, a3_init)


# FFT computation helper
def compute_fft(signal):
    N = len(signal)
    yf = fft(signal)
    # Get positive frequencies only
    xf = np.linspace(0.0, sample_rate / 2, N // 2)
    return xf, 2.0 / N * np.abs(yf[:N // 2])


# Time domain visualization
line_time, = ax1.plot(t, signal, 'b-')
ax1.set_title('Time Domain Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.set_xlim([0, duration])
ax1.grid(True)

# Frequency domain visualization
xf, yf = compute_fft(signal)
line_freq, = ax2.plot(xf, yf, 'r-')
ax2.set_title('Frequency Domain (FFT)')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')
ax2.set_xlim([0, 50])  # Limit view to relevant frequencies
ax2.grid(True)

# Frequency control sliders
ax_f1 = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_f2 = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_f3 = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_f1 = Slider(ax_f1, 'Freq 1 (Hz)', 0, 30.0, valinit=f1_init)
slider_f2 = Slider(ax_f2, 'Freq 2 (Hz)', 0, 30.0, valinit=f2_init)
slider_f3 = Slider(ax_f3, 'Freq 3 (Hz)', 0, 30.0, valinit=f3_init)

# Amplitude control sliders
ax_a1 = plt.axes([0.05, 0.15, 0.05, 0.03])
ax_a2 = plt.axes([0.05, 0.1, 0.05, 0.03])
ax_a3 = plt.axes([0.05, 0.05, 0.05, 0.03])
slider_a1 = Slider(ax_a1, 'A1', 0, 1.0, valinit=a1_init, orientation='horizontal')
slider_a2 = Slider(ax_a2, 'A2', 0, 1.0, valinit=a2_init, orientation='horizontal')
slider_a3 = Slider(ax_a3, 'A3', 0, 1.0, valinit=a3_init, orientation='horizontal')


# Slider event handler
def update(val):
    # Get current values from sliders
    f1 = slider_f1.val
    f2 = slider_f2.val
    f3 = slider_f3.val
    a1 = slider_a1.val
    a2 = slider_a2.val
    a3 = slider_a3.val

    # Regenerate the signal
    signal = generate_signal(f1, f2, f3, a1, a2, a3)

    # Update time domain plot
    line_time.set_ydata(signal)

    # Update frequency domain plot
    xf, yf = compute_fft(signal)
    line_freq.set_ydata(yf)

    # Redraw
    fig.canvas.draw_idle()


# Connect sliders to update function
slider_f1.on_changed(update)
slider_f2.on_changed(update)
slider_f3.on_changed(update)
slider_a1.on_changed(update)
slider_a2.on_changed(update)
slider_a3.on_changed(update)

# Reset button
reset_ax = plt.axes([0.8, 0.01, 0.1, 0.03])
reset_button = Button(reset_ax, 'Reset')


def reset(event):
    slider_f1.reset()
    slider_f2.reset()
    slider_f3.reset()
    slider_a1.reset()
    slider_a2.reset()
    slider_a3.reset()


reset_button.on_clicked(reset)

# Waveform selector
waveform_ax = plt.axes([0.04, 0.7, 0.08, 0.15])
waveform_radio = RadioButtons(waveform_ax, ('Sin', 'Square', 'Sawtooth'))


def waveform_change(label):
    # Get current values from sliders
    f1 = slider_f1.val
    f2 = slider_f2.val
    f3 = slider_f3.val
    a1 = slider_a1.val
    a2 = slider_a2.val
    a3 = slider_a3.val

    # Generate signal based on waveform type
    if label == 'Sin':
        signal = generate_signal(f1, f2, f3, a1, a2, a3)
    elif label == 'Square':
        signal = (a1 * np.sign(np.sin(2 * np.pi * f1 * t)) +
                  a2 * np.sign(np.sin(2 * np.pi * f2 * t)) +
                  a3 * np.sign(np.sin(2 * np.pi * f3 * t)))
    elif label == 'Sawtooth':
        signal = (a1 * (2 * (f1 * t % 1) - 1) +
                  a2 * (2 * (f2 * t % 1) - 1) +
                  a3 * (2 * (f3 * t % 1) - 1))

    # Update time domain plot
    line_time.set_ydata(signal)

    # Update frequency domain plot
    xf, yf = compute_fft(signal)
    line_freq.set_ydata(yf)

    # Redraw
    fig.canvas.draw_idle()


waveform_radio.on_clicked(waveform_change)

# Main title
plt.figtext(0.5, 0.97, 'Interactive Fourier Transform Visualizer',
            ha='center', va='center', fontsize=16, fontweight='bold')

# Display the interactive figure
plt.show(block=True)
