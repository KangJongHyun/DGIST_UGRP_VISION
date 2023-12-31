# DGIST_UGRP_VISION
Spatial Audio와 Real-time detection Algorithm을 이용한 시각장애인용 기기 및 소프트웨어 고안
|배재형|강종현|권남혁|이동건|
|------|---|---|---|
|SoundAudio|SoundAudio|Detection|Detection|

## 1. Spatial Audio test

### 참고 github 사이트
- https://github.com/AudioLabYork/SALTE-audio-renderer : 공간 오디오 청취 실험을 수행하기 위한 전용 오디오 렌더링 엔진과 가상 현실 인터페이스
--------
#### Sound test Code (Simple ex)
```py
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

## 2. Detection test
### 1. cv2 module
cv_yolo_test.ipynb 파일은 yolo v4 버전을 사용한 물체 인식 코드이다.
yolov4.cfg 는 모델 구성 파일이며 coco.names 는 모델이 포함하는 클래스의 이름이 포함된 파일이다.
yolov4.weights 는 모델 가중치 파일이며 용량이 너무 커서 업로드 하지 못 했다.

코드는 yolo 모델을 불러오는 과정, 물체 인식과 바운딩 박스를 설정하는 과정, 연결된 카메라를 인식하고 영상을 실시간으로 받아오는 과정 으로 나누어진 노트북 파일이다.
CPU를 사용하면 상당히 느리지만
GPU를 사용하면 실시간으로 물체 확인이 가능하다.


### 2. example_file
intel 에서 제공해주는 코드 중 잘 동작하며 기능이 있는 것들 위주로 노트북 파일을 만들었다.


### 3. tensorflow
tensorflow 를 사용한 파일이며 에러가 자주 발생하고 요즘 많이 사용되지 않는 모듈이다.


### 4. torch
pytorch 를 사용한 파일이다.


### 5. dataset
직접 사진을 찍어 학습시킬 이미지를 확보하거나 roboflow, 한국 공공데이터 와 같은 사이트에서 다운로드 받아 사용해야한다.
사진을 직접 찍어서 사용하면 라벨링 작업을 해야한다.

## 3. Depth Camera 
#### Getting Start 
-
-
-

## 4. 학습, 실험 환경

### 사진 찍을 물체
사람, 


### 환경


- 실험환경?
    - 필요한 조건
        - 움직이는 위험한 물체(사람, 자전거, 오토바이, 킥보드 등)이 존재하는 환경 vs 정적인 장애물 사이에서 움직이는 환경
        - 평지 vs 기울어져 있거나(언덕) 연속적이지 않은 지형(계단, 인도 차도 사이 단차)
        - 물체 분석
        - 
         
    - 외부
        - 장애물이 많고 평지인 지형 →
        - 장애물이 조금 존재, 지형이 살짝 복잡 → e7 산책로?
    - 내부
        - 정적인 장애물 다수, 평지 → ?
        - 지형이 복잡한 경우 (ex. 계단) → 계단의 경우 감지하고 계단임을 알려준 다음 계단 각각의 높이를 소리로 알려주어 발을 디딜 수 있도록? 또는 계단임을 안다면 알아서 올라간 다음 남은 계단의 수를 알려주는 방식? → 사람이 없는 E3, E7 계단?
        - 물체 구분이 필요한 경우


ㅡㅡㅡ
## 각자 할 일

강종현 - 탐지 정보를 기반으로 실제로 구현되는 코드 작성 - 8월 2일 (수)

권남혁 - 모델 파일 작성, 최적화된 모델 찾기, 물체 뎁스 평균내서 출력하기 - 8월 2일 (수)

배재형 - 실제 물체 소리 적용, 탐지 정보 전처리 - 8월 5일 (일)

이동건 - 정리된 메뉴얼(실험 장소, 실험 환경, 찍을 사진/다음 시간), 바닥 탐지 (8월 7일)



