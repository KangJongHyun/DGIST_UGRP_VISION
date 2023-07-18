import numpy as np
import sounddevice as sd

# Choose a duration for the sound
duration = 1.0  # seconds
# Choose a sample rate
sample_rate = 44100

# Generate a time array
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Generate the first sinusoidal signal (left channel)
freq1 = 440  # Hz
note1 = np.sin(freq1 * t * 2 * np.pi)

# Generate the second sinusoidal signal (center channel)
freq2 = 880  # Hz
note2 = np.sin(freq2 * t * 2 * np.pi)

# Generate the third sinusoidal signal (right channel)
freq3 = 1320  # Hz
note3 = np.sin(freq3 * t * 2 * np.pi)

# Ensure that the values are in the range -1 to 1
note1 = note1 / np.max(np.abs(note1))
note2 = note2 / np.max(np.abs(note2))
note3 = note3 / np.max(np.abs(note3))

# Create the stereo sound with different volumes in the channels
audio_stereo = np.zeros((note1.shape[0], 3))
audio_stereo[:, 0] = note1 * 0.3  # 30% volume in left channel
audio_stereo[:, 1] = note2 * 0.6  # 60% volume in center channel
audio_stereo[:, 2] = note3  # 100% volume in right channel

# Play the sounds simultaneously
sd.play(audio_stereo, sample_rate, blocking=True)

# Wait for playback to finish before exiting
sd.wait()

