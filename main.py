import sounddevice as SD
import numpy as np


def play_sine_wave(frequency, duration, sample_rate=44100):
     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
     sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
     sd.play(sine_wave, samplerate=sample_rate)
     sd.wait()

def measure_noise_level(duration=1, sample_rate=44100, threshold_db=70):
     #print("Noise level measurement. Please wait...")

     # Record audio from microphone
     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
     sd.wait()

     # Calculate the average amplitude value
     avg_amplitude = np.mean(np.abs(audio_data))

     # Determination of noise level (in decibels)
     noise_level_db = 20 * np.log10(avg_amplitude)

     print(f"Noise level: {noise_level_db:.2f} dB")

     # Check if the threshold level is exceeded
     if noise_level_db > threshold_db:
         print("Threshold level exceeded! Playing sine wave sound.")
         play_sine_wave(frequency=10000, duration=3)


if __name__ == "__main__":
     while True:
         measure_noise_level()
