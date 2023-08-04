import numpy as np
import sounddevice as sd
import time

def generate_sound(distance, angle_radians, duration, frequency, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * t * 2 * np.pi)
    note = note / np.max(np.abs(note))
    attenuation_factor = 1.0 / (distance ** 2)
    left_volume = np.cos(angle_radians)
    right_volume = np.sin(angle_radians)
    fade_samples = int(sample_rate * 0.1)
    fade_window = np.concatenate([np.linspace(0, 1, fade_samples),
                                  np.ones(int(sample_rate * duration - 2 * fade_samples)),
                                  np.linspace(1, 0, fade_samples)])
    left_sound = note * attenuation_factor * left_volume * fade_window
    right_sound = note * attenuation_factor * right_volume * fade_window
    return np.array([left_sound, right_sound])

duration = 0.5
frequency = 440
sample_rate = 44100
angle_degrees = 45
angle_radians = np.radians(angle_degrees)

# 1미터부터 10미터까지 1미터 간격으로 소리 재생
for distance in range(1, 11):
    sound = generate_sound(distance, angle_radians, duration, frequency, sample_rate)
    sd.play(sound.T, sample_rate)
    sd.wait()

time.sleep(3)  # 3초 동안 텀

distance = 5.0  # 초기 위치

full_audio = np.array([])

for i in range(8):  # 4초 동안 코드 진행됨
    audio_stereo = generate_sound(distance, angle_radians, duration, frequency, sample_rate)
    if i == 0:
        full_audio = audio_stereo
    else:
        full_audio = np.hstack([full_audio, audio_stereo])
    distance -= 0.5

sd.play(full_audio.T, sample_rate)
sd.wait()
