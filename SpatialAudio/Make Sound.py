import numpy as np
import sounddevice as sd

duration = 10.0 
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)
note = np.sin(frequency * t * 2 * np.pi)
note = note / np.max(np.abs(note))
distance = float(input("Enter the distance from the sound source (in meters): "))

angle_degrees = float(input("Enter the direction in degrees (0 to 90): "))

angle_radians = np.radians(angle_degrees)

attenuation_factor = 1.0 / (distance ** 2)

left_volume = np.cos(angle_radians)
right_volume = np.sin(angle_radians) 
left_sound = note * attenuation_factor * left_volume
right_sound = note * attenuation_factor * right_volume
audio_stereo = np.array([left_sound, right_sound])
sd.play(audio_stereo.T, sample_rate)
sd.wait()
