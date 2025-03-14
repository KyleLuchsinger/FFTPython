# Fourier Transform Visualizer

An interactive tool for visualizing and exploring Fourier transforms with real-time manipulation of signal components.

![Fourier Transform Visualizer](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Fourier2_-_restoration1.jpg/220px-Fourier2_-_restoration1.jpg)

## Overview

This application provides an intuitive interface for understanding the relationship between time domain signals and their frequency domain representations. Users can manipulate multiple frequency components in real-time and observe how changes affect both domains simultaneously.

## Features

- **Interactive Signal Manipulation**: Adjust frequencies and amplitudes of up to three signal components with sliders
- **Real-time Visualization**: Observe immediate changes in both time and frequency domains
- **Multiple Waveform Types**: Switch between sine, square, and sawtooth waveforms
- **Fast Fourier Transform (FFT)**: View the frequency spectrum of your custom signals
- **Adjustable Parameters**: Modify component frequencies up to 30Hz and amplitudes between 0-1

## Requirements

- Python 3.6+
- NumPy
- Matplotlib
- SciPy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/KyleLuchsinger/FFTPython.git
cd FFTPython
```

2. Install the required dependencies:
```bash
pip install numpy matplotlib scipy
```

## Usage

Run the application:
```bash
python FFTPython.py
```

### Controls

- **Frequency Sliders (Freq 1-3)**: Adjust the frequency of each component (0-30Hz)
- **Amplitude Sliders (A1-3)**: Adjust the amplitude of each component (0-1)
- **Waveform Selection**: Choose between Sine, Square, and Sawtooth waveforms
- **Reset Button**: Return all parameters to default values

## How It Works

The application generates a composite signal from three components with adjustable frequencies and amplitudes. It then computes the Fast Fourier Transform (FFT) to display the frequency spectrum of the signal. The interactive controls allow you to experiment with different combinations and observe the relationships between time and frequency domains.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
