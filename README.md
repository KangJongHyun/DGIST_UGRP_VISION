# DGIST_UGRP_VISION
Spatial Audio와 Real-time detection Algorithm을 이용한 시각장애인용 기기 및 소프트웨어 고안
|배재형|강종현|권남혁|강종현|
|------|---|---|---|
|SoundAudio|SoundAudio|Detection|Detection|

## 1. Spatial Audio test

### 참고 github 사이트
- https://github.com/AudioLabYork/SALTE-audio-renderer : 공간 오디오 청취 실험을 수행하기 위한 전용 오디오 렌더링 엔진과 가상 현실 인터페이스
--------
#### Sound test Code (Simple ex)
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
# Create stereo sound with different volumes in the channels
audio_stereo = np.zeros((audio.shape[0], 2), dtype=np.int16)
audio_stereo[:, 0] = audio * 0.45  # 45% volume in left channel
audio_stereo[:, 1] = audio  # 100% volume in right channel
# Start playback
play_obj = sa.play_buffer(audio_stereo, 2, 2, sample_rate)
# Wait for playback to finish before exiting
play_obj.wait_done()
# Get the user's guess
user_azimuth = input("Enter your guess for the azimuth (in degrees): ")
user_distance = input("Enter your guess for the distance (in meters): ")
# Print the user's guess
print(f"Your guess for azimuth: {user_azimuth}, for distance: {user_distance}")
```

## 배재형의 생각
카메라 최대 인식거리가 16m정도니깐 안정적으로 100% 인지할 수 있는 거리를 12m라 두자(변경가능).

0.5m? 1m? 정도(변경가능)를 최대 볼륨으로 잡고, 실제 소리가 구면파니깐 거리 제곱에 비례해서 감소하는걸 이용해서 계산을 통해 거리별 소리를 나타내면 좋을 것 같다.(현실과 가상의 괴리가 줄어들어 유저가 학습할 때 편리하다고 예상)

원래는 방위각과 위도 둘다 사용하려 했지만, 강종현: 굳이 위도가 필요한가? → 딱히 필요 없을 듯. 어차피 계단등을 제외하고는 전부 2차원적인 이동이고, 높이를 가진 물체가 보행에 영향을 끼치는 확률은 0에 수렴한다.

강종현이 가져온 simpleaudio 모듈을 보고 생각을 해보겠다. 저 모듈에서 2개 이상의 소리를 융합하는 것이 가능한가?

오늘 아침에 교수님과 이야기를 해보았는데, 주요 내용은 다음과 같다.

+ 소리를 들려주는 방식이 스피커 말고(스피커 거리에 따라서 많이 달라지니) 헤드폰 or 인이어 이어폰은 어떤가?
+ virtual 5.1 audio, 7.1 audio등을 찾아보면 좋을 것 같다.
+ 지금까지 한것은 있는가? → 저번이랑 크게 다를 것은 없지만, 이번주부터 목요일 저녁마다 미팅하기로 했고 다다음주까지 코드 완성을 목표로 잡고 있다.

이번주(오늘) 한 것
+ 효과음 찾기
+ 저번과 다른 HRTF set을 적용시키기
+ 서로 다른 위치의 소리를 합성하기

## 2. Detection test
