# DGIST_UGRP_VISION
Spatial Audio와 Real-time detection Algorithm을 이용한 시각장애인용 기기 및 소프트웨어 고안
|배재형|강종현|권남혁|강종현|
|------|---|---|---|
|SoundAudio|SoundAudio|Detection|Detection|

## 1. Spatial Audio test

### 참고 github 사이트
- https://github.com/AudioLabYork/SALTE-audio-renderer : 공간 오디오 청취 실험을 수행하기 위한 전용 오디오 렌더링 엔진과 가상 현실 인터페이스

  --------
  Sound test Code (Simple ex)
  ```
!pip install simpleaudio

import numpy as np
import simpleaudio as sa
import math

# Choose a duration for the sound
duration = 1.0  # seconds

# Choose a frequency for the sound
freq = 440  # Hz

# Choose a sample rate
sample_rate = 44100

# Generate a time array
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Generate a sinusoidal signal
note = np.sin(freq * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# Wait for playback to finish before exiting
play_obj.wait_done()

# Get the user's guess
user_azimuth = input("Enter your guess for the azimuth (in degrees): ")
user_distance = input("Enter your guess for the distance (in meters): ")

# Print the user's guess
print(f"Your guess for azimuth: {user_azimuth}, for distance: {user_distance}")

  ```

## 2. Detection test
