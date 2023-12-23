# Noise Level Measurement and Sine Wave Player

This Python script utilizes the `sounddevice` library to measure the noise level through the microphone and play a sine wave sound if the noise level exceeds a specified threshold.

## Requirements

- Python 3
- NumPy
- Sounddevice

Install the required libraries using the following:

```bash
pip install numpy sounddevice
```

# Customization
You can customize the script by modifying the following parameters:

- `duration`: Duration of the noise level measurement in seconds.  
- `sample_rate`: Sampling rate for audio recording.  
- `threshold_db`: Threshold level in decibels. If the noise level exceeds this threshold, the sine wave sound will be played.  
- `frequency`: Frequency of the sine wave sound played when the threshold is exceeded.

Feel free to adjust these parameters based on your preferences.
