import numpy as np
import sounddevice as sd
import time
import random

def generate_sound(distance, angle_radians, duration, frequency, sample_rate):
    full_audio = np.array([])
    for i in range(int(duration / 0.5)): 
        t = np.linspace(i * 0.5, (i + 1) * 0.5, int(sample_rate * 0.5), False)
        note = np.sin(frequency * t * 2 * np.pi)
        note = note / np.max(np.abs(note))
        attenuation_factor = 1.0 / (distance ** 2)
        left_volume = np.cos(angle_radians)
        right_volume = np.sin(angle_radians)
        fade_samples = int(sample_rate * 0.1)
        fade_window = np.concatenate([np.linspace(0, 1, fade_samples),
                                      np.ones(int(sample_rate * 0.5 - 2 * fade_samples)),
                                      np.linspace(1, 0, fade_samples)])
        left_sound = note * attenuation_factor * left_volume * fade_window
        right_sound = note * attenuation_factor * right_volume * fade_window
        sound = np.array([left_sound, right_sound])
        if i == 0:
            full_audio = sound
        else:
            full_audio = np.hstack([full_audio, sound])
    return full_audio

def create_test_cases():
    duration = 4.0
    frequency = 440
    sample_rate = 44100
    angle_degrees = 45
    angle_radians = np.radians(angle_degrees)

    test_cases = []

    # 거리가 점점 멀어지는 테스트 케이스
    for distance in np.linspace(1, 10, 10):
        test_cases.append(generate_sound(distance, angle_radians, duration, frequency, sample_rate))

    # 각도가 점점 달라지는 테스트 케이스
    for angle_degrees in np.linspace(0, 360, 10):
        angle_radians = np.radians(angle_degrees)
        test_cases.append(generate_sound(5, angle_radians, duration, frequency, sample_rate))

    # 거리와 각도가 모두 점점 달라지는 테스트 케이스
    for distance, angle_degrees in zip(np.linspace(1, 10, 10), np.linspace(0, 360, 10)):
        angle_radians = np.radians(angle_degrees)
        test_cases.append(generate_sound(distance, angle_radians, duration, frequency, sample_rate))
        
    return test_cases

def play_random_sound(test_cases, sample_rate):
    sound = random.choice(test_cases)
    sd.play(sound.T, sample_rate)
    sd.wait()

user_input = input("Enter '1' for tutorial sound, '2' to skip tutorial sound: ")

sample_rate = 44100
test_cases = create_test_cases()

if user_input == '1':
    play_random_sound(test_cases, sample_rate)
elif user_input == '2':
    play_random_sound(test_cases, sample_rate)
else:
    print("Invalid input. Please enter either '1' or '2'.")
